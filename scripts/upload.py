import hashlib
from algoliasearch.search_client import SearchClient
import os

client = SearchClient.create(os.getenv("ALGOLIA_CLIENT"), os.getenv("ALGOLIA_SECRET"))
index = client.init_index("documentation")

basedir = "../docs"
for dirname in os.listdir(basedir):
    if "md" not in dirname:
        continue

    to_upload = []
    filename = dirname.split(".")[0:-1]
    fileread = "%s/%s" % (basedir, dirname)

    print("Reading %s" % dirname)
    with open(fileread, "r") as tmp:
        data = tmp.read().split("\n")
    
        wrappeditem = {}
        curitem = ""
        for item in data:
            if item.startswith("#"):
                if curitem:
                    to_upload.append(wrappeditem)
                    
                # Priority based on title
                title = " ".join(item.split("# ")[1:])
                priority = 5
                for char in item:
                    if char == "#":
                        priority -= 1
    
                # Hash is used for prioritizing the search
                title_hash = hashlib.md5(("%s_%s" % (filename, title)).encode("utf-8")).hexdigest()
                wrappeditem = {
                    "title": title.strip(),
                    "data": "",
                    "url": "https://shuffler.io/docs/%s#%s" % (filename, title.replace(" ", "_").lower()),
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
    
    print(to_upload)
    print(len(to_upload))
    ret = index.save_objects(to_upload)
    print(ret)
