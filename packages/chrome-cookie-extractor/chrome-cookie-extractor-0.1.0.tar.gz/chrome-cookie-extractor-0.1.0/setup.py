import re
from setuptools import setup
 
 
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('src/chrome_cookie_extractor/chrome_cookie_extractor.py').read(),
    re.M
    ).group(1)
 
 
with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")
 
 
setup(
    name = "chrome-cookie-extractor",
    packages = ["src.chrome_cookie_extractor"],
    entry_points = {
        "console_scripts": ['chrome-cookie-extractor = src.chrome_cookie_extractor.chrome_cookie_extractor:main']
        },
    version = version,
    description = "exports your cookies to the Netscape cookie file format which is compatible with wget, curl, youtube-dl and more.",
    long_description = long_descr,
    author = "a.Krone",
    author_email = "ahustinkrone@gmail.com",
    url = "https://github.com/KroneCorylus/chrome-cookie-extractor",
    )