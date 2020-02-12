'''
Using
https://github.com/wikimedia/mediawiki-api-demos/blob/master/python/upload_file_from_url.py

Pulls from list of files from txt and loops it through Fandom.com to get files.

'''

import requests

URL = ""
Username = ""
Password = ""
srcPath =  "https://warframe.fandom.com/wiki/Special:FilePath/"
FilesList = "Files.txt"


S = requests.Session()

PARAMS_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_1)
DATA = R.json()
LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]
PARAMS_2 = {
    "action": "login",
    "lgname": Username,
    "lgpassword": Password,
    "format": "json",
    "lgtoken": LOGIN_TOKEN
}

R = S.post(URL, data=PARAMS_2)

PARAMS_3 = {
    "action": "query",
    "meta":"tokens",
    "format":"json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]


F = open(FilesList, "r")
filelist = F.readlines()
F.close();

for line in filelist:
    filename = line.strip()
    url = srcPath + filename

    print(filename + ': ' + url)
    PARAMS_4 = {
    "action": "upload",
    "filename": filename,
    "url": url,
    "format": "json",
    "token": CSRF_TOKEN,
    "ignorewarnings": 1
    }
    R = S.post(URL, data=PARAMS_4)
    DATA = R.json()

print("Done.")

