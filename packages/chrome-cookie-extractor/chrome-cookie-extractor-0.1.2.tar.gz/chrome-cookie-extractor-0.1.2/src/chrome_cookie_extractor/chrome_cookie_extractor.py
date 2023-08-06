#!/usr/bin/python
import sys 
import getopt
import os
import sqlite3
import csv
import json
from pycookiecheat import chrome_cookies
from os import scandir


__version__ = "0.1.2"
__description__= "exports your cookies to the Netscape cookie file format which is compatible with wget, curl, youtube-dl and more."
help = "chrome-cookie-extractor " + __description__ + """
USAGE: chrome-cookie-extractor -u <url>
MANDATORY:
    -u <url>, --url=<url>                         url from where extract the cookies  
OPTIONS:
    -o <outputfile>, --output=<outputfile>        change the location and name of the output file.
    -p <profile>, --profile=<profile>             change the default profile to another.
    -s, --silent                                  not print cookies on terminal.
    -l, --logonly                                 not generate file.

ENVIRONMENT VARIABLES:
    CHROME_CONFIG_DIR: Use this environment variable to overide the default location (~/.config/google-chome) like this
    EXPORT CHROME_CONFIG_DIR=/usr/local/google-chrome
    
Thanks pycookiecheat(https://github.com/n8henrie/pycookiecheat)
By Krone
"""

outputfile = "cookies.tsv"
silent = False
logonly = False
chromedir =  os.getenv('CHROME_CONFIG_DIR') or os.path.expanduser("~/.config/google-chrome/")
profiledir = chromedir + "Default"
class ProfileNotExist(Exception):
    pass
class CookiesFileNotFound(Exception):
    pass
class MissingUrl(Exception):
    pass


def find(base, filenames, depth):
    hits = []
    def find_in_dir_subdir(direc, currentdepth, maxdepth):
        if currentdepth > maxdepth:
            return
        content = scandir(direc)
        for entry in content:
            if entry.name in filenames:
                hits.append([os.path.join(direc, entry.name),direc])
            elif entry.is_dir():
                try:
                    find_in_dir_subdir(os.path.join(direc, entry.name), currentdepth + 1, maxdepth)
                except UnicodeDecodeError:
                    print("Could not resolve " + os.path.join(direc, entry.name))
                    continue
                except PermissionError:
                    print("Skipped " + os.path.join(direc, entry.name) + ". I lacked permission to navigate")
                    continue

    if not os.path.exists(base):
        return
    else:
        find_in_dir_subdir(base, 0, depth)

    return hits


def getUrls(url: str):
    clean_url=url.removeprefix("http://").removeprefix("https://").removeprefix("www.").split("/", 1)[0]
    www_url="http://www." + clean_url
    http_url="http://" + clean_url
    sql_url = """%.""" + clean_url
    return www_url, http_url, sql_url
def getQuery(url: str):
    return '''
    SELECT 
        host_key,
        path,
        is_secure,
        name,
        ((expires_utc/1000000)-11644473600), 
        CASE WHEN host_key like "''' + url  + '''" THEN TRUE ELSE FALSE END 
    FROM 
        cookies 
    WHERE 
        host_key like "%.twitch.tv" 
    ORDER BY host_key, name
'''
def getProfileDirByName(name: str):
    result = find(chromedir, ["Preferences"], 1)
    for preferences, profiledir in result:
        f = open(preferences)
        data = json.load(f)
        if name == data["profile"]["name"]:
            return profiledir
    for preferences, profiledir in result:
        if profiledir.rsplit("/",1)[1] == name:
            return profiledir
    return None

def main():
    argv=sys.argv[1:]
    global profiledir, outputfile, silent, logonly
    url = None
    profile = None
    try:
        opts, args = getopt.getopt(argv,"u:o:p:sl",["url=","output=","profile=","silent","logonly"])
        for opt, arg in opts:
            if opt == '-h':
                print(help)
                sys.exit()
            elif opt in ("-o", "--output"):
                print(opts,opt)
                outputfile = os.path.expanduser(arg)
            elif opt in ("-p", "--profile"):
                profile = arg
            elif opt in ("-u", "--url"):
                url = arg
            elif opt in ("-s", "--silent"):
                silent = True
            elif opt in ("-l", "--logonly"):
                logonly = True
        if not url:
            raise MissingUrl("Missing URL check usage with chrome-cookie-extractor -h")
        if profile:
            chromedir = getProfileDirByName(profile)
            if not chromedir:
                raise ProfileNotExist("Profile do not exists: " + profile)
            if not os.path.exists(chromedir + "/Cookies"):
                raise CookiesFileNotFound("Cookies file do not exists:" + chromedir + "/Cookies")
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
    except ProfileNotExist as er:
        print(er)
        sys.exit(3)
    except MissingUrl as er:
        print(er)
        sys.exit(3)
    except Exception as er:
        print(er)
        sys.exit(3)
   
    www_url, http_url, sql_url = getUrls(url)
    cookie_file = profiledir + '/Cookies'
    a = chrome_cookies(www_url, cookie_file=cookie_file)
    b = chrome_cookies(http_url, cookie_file=cookie_file)
    a.update(b)
    decrypted_cookies = a
    conn = sqlite3.connect(cookie_file)
    sql = getQuery(sql_url)
    if not logonly:
        with open(outputfile, 'w', encoding='US-ASCII', newline='') as tsv_file:
                tsv_writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
                tsv_writer.writerow(["# Netscape HTTP Cookie File"])
                tsv_writer.writerow(["# This file is generated by chrome-cookie-extrator for youtube-dl.  Do not edit."])
                tsv_writer.writerow("")
                for host_key, path, is_secure, name, _exptime, _subdomain in conn.execute(sql):
                    tsv_writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
                    exptime = max(_exptime, 0)
                    secure = str(bool(is_secure)).upper()
                    subdomain = str(bool(_subdomain)).upper()
                    tsv_writer.writerow([host_key, subdomain, path, secure, exptime, name,decrypted_cookies.get(name)])
                    if not silent:
                        print(host_key, subdomain, path, secure, exptime, name,decrypted_cookies.get(name), sep='\t')
        print("");
        print("cookies exported: " + outputfile)
    else:
        for host_key, path, is_secure, name, _exptime, _subdomain in conn.execute(sql):
            exptime = max(_exptime, 0)
            secure = str(bool(is_secure)).upper()
            subdomain = str(bool(_subdomain)).upper()
            print(host_key, subdomain, path, secure, exptime, name,decrypted_cookies.get(name), sep='\t')

    conn.close()



