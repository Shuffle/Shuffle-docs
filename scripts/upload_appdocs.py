# Uploads appdocs from OpenAPI apps and Python apps to Algolia for searchability
# Based on upload.py (normal docs)

import os
import hashlib
import requests
from algoliasearch.search_client import SearchClient
from algoliasearch.exceptions import RequestException

client = SearchClient.create(os.getenv("ALGOLIA_CLIENT"), os.getenv("ALGOLIA_SECRET"))
index = client.init_index("documentation")
appindex = client.init_index('appsearch')

def get_algolia_image(appname):
    results = appindex.search(appname)

    for item in results["hits"]:
        if appname.lower() in item["name"].lower():
            return item["image_url"]

    return ""

basedir = "../../OpenAPI-security-definitions/docs"
validurls = []
for dirname in os.listdir(basedir):
    if "md" not in dirname:
        continue

    if ".swo" in dirname or ".swp" in dirname:
        continue

    to_upload = []
    filename = "".join(dirname.split(".")[0:-1])
    fileread = "%s/%s" % (basedir, dirname)

    #print("Reading %s" % dirname)
    with open(fileread, "r") as tmp:
        try:
            data = tmp.read().split("\n")
        except UnicodeDecodeError as e:
            print("Error loading %s: %s" % (dirname, e))
            continue
    
        wrappeditem = {}
        curitem = ""
        for item in data:
            if item.startswith("#"):
                if curitem:
                    if wrappeditem["title"] != "Table of contents":
                        if wrappeditem["ref_url"] not in validurls:
                            print("REF: %s, doc: %s" % (filename, wrappeditem["ref_url"]))
                            ret = requests.get(wrappeditem["ref_url"])
                            #print("RET: %d - %s" % (ret.status_code, wrappeditem["ref_url"]))
                            if ret.status_code != 200:
                                print("SKIPPING %s (doesn't exist)" % wrappeditem["ref_url"])
                                break
                            else:
                                validurls.append(wrappeditem["ref_url"])

                        #if filename == "datadog":
                        to_upload.append(wrappeditem)
                    
                # Priority based on title
                title = "%s: %s" % (filename.capitalize(), " ".join(item.split("# ")[1:]).strip())
                image = get_algolia_image(filename)

                priority = 0
                for char in item:
                    if char == "#":
                        priority -= 1

                # Hash is used for prioritizing the search
                title_hash = hashlib.md5(("%s_%s" % (filename, title)).encode("utf-8")).hexdigest()
                wrappeditem = {
                    "filename": filename,
                    "title": title.strip(),
                    "name": title.strip(),
                    "data": "",
                    "url": "https://shuffler.io/apps/%s?tab=docs#%s" % (filename, title.replace(" ", "_").lower()),
                    "urlpath": "/apps/%s?tab=docs#%s" % (filename, title.replace(" ", "_").lower()),
                    "url_hash": title.replace(" ", "_").lower(),
                    "objectID": title_hash,
                    "priority": priority,
                    "image_url": image,
                    "ref_url": "https://github.com/shuffle/openapi-apps/blob/master/docs/%s.md" % filename,
                }
                curitem = item
                #continue
    
            if item:
                curitem += item+"\n"
                try:
                    wrappeditem["data"] += item
                except KeyError:
                    wrappeditem["data"] = item
    
    if len(to_upload) > 0:
        try:
            print("Uploading: %s" % to_upload)
            ret = index.save_objects(to_upload)
            print("%s: %d objects" % (filename, len(to_upload)))
        except RequestException as e:
            print("ERROR: %s: %d objects: %s" % (filename, len(to_upload), e))
