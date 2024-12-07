// https://fhnw.mit-license.org

import os
import sys
import urllib.parse

def update(path):
    dirs = os.path.dirname(path) # "Hardware/Microcontrollers"
    base = os.path.basename(path) # "Adafruit_Feather_M4_Express.md"
    name = os.path.splitext(base)[0].replace('_', ' ')

    body = "# " + name + "\n"
    body += "If there are no [open requests](../../../../issues?"
    query = {
        "q": "is:issue is:open \"" + name + "\" in:title"
    }
    body += urllib.parse.urlencode(query)
    body += ") you're welcome to [borrow this](../../../../issues/new?"
    issue = {
        "title": "Borrow request for " + name,
        "body": "1 piece of [this](../blob/main/" + path + ") for ~2 weeks."
    }
    body += urllib.parse.urlencode(issue)
    body += ")."

    ok = input("update " + path + "? [y|n|q] ")
    if ok == "y":
        assert os.path.getsize(item_path) == 0
        with open(path, "w") as file:
            file.write(body)
        #print(body)
        #print("\n")
    elif ok == "q":
        sys.exit(0)

root_dir = "."
for topic in os.listdir(root_dir):
    topic_dir = root_dir + "/" + topic;
    if os.path.isdir(topic_dir) and topic != ".git":
        #print(topic)
        for subtopic in os.listdir(topic_dir):
            subtopic_dir = topic_dir + "/" + subtopic;
            if os.path.isdir(subtopic_dir):
                #print("\t\t" + subtopic)
                for item in os.listdir(subtopic_dir):
                        item_path = subtopic_dir + "/" + item
                        if item_path.endswith(".md") and os.path.getsize(item_path) == 0:
                            #print("\t\t\t" + item)
                            update(item_path)
