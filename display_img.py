from PIL import Image
import os
import json
import subprocess
import time





# command = "C:/Users/joris/OneDrive/Documenten/post-digital-media-ecologies/projects/3.gif"
# command2 = "C:/Users/joris/OneDrive/Documenten/post-digital-media-ecologies/projects/1.jpg"



# p = subprocess.Popen(f"{command2}", stdout=subprocess.PIPE, shell=True)
# time.sleep(1)
# p.kill()
# print("lll")









# function to check if Image Eye exists
def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())


# check if image eye exists every 2 minutes and then delete all instances of that program ( so it does not xclog up ram)
starttime = time.time()
while True:
    while process_exists("Image Eye.exe") == True:
        os.system('taskkill /IM "Image Eye.exe"')   
        print("program exioss")

    time.sleep(20.0 - ((time.time() - starttime) % 20.0))




