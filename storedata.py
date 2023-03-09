import json
import os
import subprocess
import time

jsonFile = os.path.join(os.getcwd(), "projects/tags.json")


text = "yours and architecture and moma"


with open(jsonFile,'r') as tags:
    jsonObj = json.load(tags)
    for obj in jsonObj:
        if obj in text:
            
            for i in range(len(jsonObj[obj])):
                print(jsonObj[obj][i])

                command = os.path.join("C:/Users/joris/OneDrive/Documenten/post-digital-media-ecologies/projects/",jsonObj[obj][i])
                subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                time.sleep(0.5)
            




