# chrome-cookie-extractor
Exports your cookies to the Netscape cookie file format which is compatible with wget, curl, youtube-dl and more.

## Usage

```
chrome-cookie-extractor -u twitch.tv
```

## Options
```
-o <outputfile>, --output=<outputfile>        change the location and name of the output file.
-p <profile>, --profile=<profile>             change the default profile to another.
-s, --silent                                  not print cookies on terminal.
-l, --logonly                                 not generate file.
```