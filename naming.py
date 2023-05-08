import glob, os
from os import startfile


all_path = glob.glob("E:/Books/*/V*")
for i in range(len(all_path)):
    new_path = all_path[i].split("\\")
    startfile(all_path[i])
    path = new_path[0] + "/" + new_path[1] + "/" + new_path[2] + "/" + input() + + ".mp4"
    try:
        os.rename(all_path[i], path)
    except:
        os.rename(all_path[i], f'E:/{path}')

all_path = glob.glob("E:/Books/*/P*.jpg")
all_path = [i.replace("\\", "/") for i in all_path]
for i in range(len(all_path)):
    new_path = all_path[i].split("/")
    startfile(all_path[i])
    path = new_path[0] + "/" + new_path[1] + "/" + new_path[2] + "/" + input() + ".jpg"
    os.rename(all_path[i], path)
