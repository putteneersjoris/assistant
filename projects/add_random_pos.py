import os
import random


basePath = os.path.join(os.getcwd(),"base/base.png")

counter = 0
for file in os.listdir(os.getcwd()):
    if file.endswith(".jpg") or file.endswith(".png"):
        counter += 1
        x = random.random()*500
        y = random.random()*600
        print(file)
        os.system(f"magick convert  {basePath}  {file} -geometry +{x}+{y} -composite {file}_a.png")
        # for i in range(len(file)):
            