import os
import hashlib
import requests
from algoliasearch.search_client import SearchClient

client = SearchClient.create(os.getenv("ALGOLIA_CLIENT"), os.getenv("ALGOLIA_SECRET"))
index = client.init_index("documentation")

basedir = "../docs"
validurls = []
for dirname in os.listdir(basedir):
    if "md" not in dirname:
        continue

    to_upload = []
    filename = "".join(dirname.split(".")[0:-1])
    fileread = "%s/%s" % (basedir, dirname)

    #print("Reading %s" % dirname)
    with open(fileread, "r") as tmp:
        data = tmp.read().split("\n")
    
        wrappeditem = {}
        curitem = ""
        for item in data:
            if item.startswith("#"):
                if curitem:
                    if wrappeditem["title"] != "Table of contents":
                        if wrappeditem["ref_url"] not in validurls:
                            ret = requests.get(wrappeditem["ref_url"])
                            #print("RET: %d - %s" % (ret.status_code, wrappeditem["ref_url"]))
                            if ret.status_code != 200:
                                print("SKIPPING %s" % wrappeditem["ref_url"])
                                break
                            else:
                                validurls.append(wrappeditem["ref_url"])

                        to_upload.append(wrappeditem)
                    
                # Priority based on title
                title = " ".join(item.split("# ")[1:]).strip()
                priority = 5
                for char in item:
                    if char == "#":
                        priority -= 1
    
                # Hash is used for prioritizing the search
                title_hash = hashlib.md5(("%s_%s" % (filename, title)).encode("utf-8")).hexdigest()
                wrappeditem = {
                    "filename": filename,
                    "title": title.strip(),
                    "data": "",
                    "url": "https://shuffler.io/docs/%s#%s" % (filename, title.replace(" ", "_").lower()),
                    "urlpath": "/docs/%s#%s" % (filename, title.replace(" ", "_").lower()),
                    "objectID": title_hash,
                    "priority": priority,
                    "ref_url": "https://github.com/frikky/shuffle-docs/blob/master/docs/%s.md" % filename,
                }
                curitem = item
                continue
    
            if item:
                curitem += item+"\n"
                try:
                    wrappeditem["data"] += item
                except KeyError:
                    wrappeditem["data"] = item
    
    if len(to_upload) > 0:
        print("%s: %d objects" % (filename, len(to_upload)))
        ret = index.save_objects(to_upload)
