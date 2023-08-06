# chrome-cookie-extractor

Exports your cookies to the Netscape cookie file format which is compatible with wget, curl, youtube-dl and more.

## INSTALL

```
pip install chrome-cookie-extractor
```

## Usage

```
chrome-cookie-extractor -u twitch.tv
```

## Options

```
    -o <outputfile>, --output=<outputfile>        change the location and name of the output file.
    -p <profile>, --profile=<profile>             change the default profile.
    -s, --silent                                  do not print cookies.
    -l, --logonly                                 do not generate a cookie file, only display print them.
    -v, --version                                 show version
```

## Diferent directory for the user data directory

This software will search for the cookies inside the default location of the user data directory for Google Chrome,
The default location(linux) is in ~/.config :
~/.config/google-chrome
this can be overridden with the environment variable $CHROME_CONFIG_HOME

```
    EXPORT CHROME_CONFIG_DIR=/usr/local/google-chrome
```
