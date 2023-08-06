"""Native host app for the COW web extension - main module"""
from base64 import b64encode
from json import dumps, loads
from pathlib import Path
from struct import pack, unpack
from sys import argv, stdin, stdout
from typing import Any, Optional, cast

import click
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

APP_MANIFEST_IN = """
{{
  "name": "ki.dour.cow.host",
  "description": "Host for the COW web extension",
  "path": "{app_path}",
  "type": "stdio",
  "allowed_extensions": [ "cow@ki-dour.org" ]
}}
"""


def get_message() -> Optional[dict[str, Any]]:
    """Read the next message comming from the web extension

    Return:
        The message as a dictionnary, None if the connection was closed.

    """
    raw_length = stdin.buffer.read(4)

    if not raw_length:
        return None

    message_length = unpack("=I", raw_length)[0]
    message = stdin.buffer.read(message_length).decode("utf-8")
    return cast(dict[str, Any], loads(message))


def send_message(message_type: str, **kwargs: Any) -> None:
    """Send a message to the web extension

    Arguments:
        message_type: Type of the message
        **kwargs: key-values of the message to send
    """
    encoded_content = dumps(dict(type=message_type, **kwargs)).encode("utf-8")
    encoded_length = pack("=I", len(encoded_content))
    stdout.buffer.write(encoded_length)
    stdout.buffer.write(encoded_content)
    stdout.buffer.flush()


def send_update(path: Path, expanded_path: Path) -> None:
    """Send a file updated message to the web extension.

    Arguments:
        path: Path of the file for which to send an update message.

    """
    message = {
        "path": str(path),
    }

    if expanded_path.is_file():
        with open(expanded_path, "rb") as file:
            file_content = file.read()
        message["content"] = b64encode(file_content).decode("ascii")

    send_message("UPDATE", **message)


class ChangeHandler(FileSystemEventHandler):  # type: ignore
    """Handler notified of watched files changes."""

    def __init__(self, path: Path, expanded_path: Path) -> None:
        self.path = path
        self.expanded_path = expanded_path
        self.observer = Observer()
        self.observer.schedule(self, expanded_path)
        self.observer.start()

    def on_modified(self, event: Any) -> None:
        send_update(self.path, self.expanded_path)

    def stop(self) -> None:
        """Shutdown this observer"""
        self.observer.stop()
        self.observer.join()


def handle_message(change_handlers: dict[Path, ChangeHandler]) -> bool:
    """Handle a message comming from the web extension

    Return:
        True if a message was handled, False if the connection was closed.

    """
    message = get_message()
    if not message:
        return False

    message_type = message["type"]
    if message_type == "WATCH":
        path = Path(message["path"])
        expanded_path = path.expanduser()
        if expanded_path.is_file() and path not in change_handlers:
            change_handlers[path] = ChangeHandler(path, expanded_path)
        send_update(path, expanded_path)
    else:
        raise Exception(f"Unknown message type : {message_type}")

    return True


def host() -> int:
    """cow-web-ext native app host entry point"""

    change_handlers: dict[Path, ChangeHandler] = {}
    while True:
        try:
            if not handle_message(change_handlers):
                break
        except Exception as ex:  # pylint: disable=broad-except
            send_message(
                "MESSAGE", content=f"Error in native file watcher : {ex}", level="ERROR"
            )

    for handler in change_handlers.values():
        handler.stop()

    return 0


@click.group()
def cli() -> None:
    """Cow web extension command line utilites"""


@cli.command()
def install() -> None:
    """Install the native app host in firefox."""
    app_path = Path(f"{argv[0]}-host")
    app_manifest_dir = Path.home() / ".mozilla/native-messaging-hosts/"
    app_manifest_dir.mkdir(parents=True, exist_ok=True)
    app_manifest = APP_MANIFEST_IN.format(app_path=str(app_path))

    with open(
        app_manifest_dir / "ki.dour.cow.host.json", "w", encoding="utf-8"
    ) as destination:
        destination.write(app_manifest)
