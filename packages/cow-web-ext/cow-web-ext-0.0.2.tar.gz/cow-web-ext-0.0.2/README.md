# Content Override & Watch

Allows to redirect request to a local file content, and enable live-reloading
url mapped to local files.

# Installation

This extension requires a native host app. To install it :

```
pip install cow-web-ext
```

To configure mapping from remote url to local file, go to the extension
settings and add pattern. The right pattern will be replaced by the left string
to obtain a file name, using Javascript Regex replace.

For example, if you load CSS files from http://example.com/css/file-name.css
and it's stored in your ~/project/static/css/file-name.css, set url pattern to

https:\/\/example.com\/css/(.*)

and file template to

~/project/static/css/$1
