from instabot import Bot
import glob, os
from PIL import Image
from text_gen import post_text
import config


def post_items(all_item_path):
    item_path = [i.split("\\")[-1] for i in all_item_path]
    items = [i.replace(".jpg", "") for i in item_path]
    theme = [i.split(" - ")[-2] for i in items]
    designers = [i.split(" - ")[-1] for i in items]
    designers = [i.split("  ")[0] for i in designers]
    company = [i.split(" - ")[0] for i in items]
    box = [i.split(" - ")[1] for i in items]
    item = [i.split(" - ")[2] for i in items]
    paths = []
    for i in range(len(all_item_path)):
        if item[0] == item[i] and  box[0] == box[i]:
            paths.append(all_item_path[i])


    bot = Bot()
    bot.login(username=config.username, password=config.password)

    theme = theme[0]
    company = company[0]
    box = box[0]
    item = item[0]
    designer = designers[0]

    context_for_text = f"Write me a Instagram post for light bookish text. Add ten hastags to the post. Seperate the tags from the text for {theme}, @{company}, {box}, {item} by @{designer}"
    text_img = post_text(context_for_text)

    image = Image.open(all_item_path[0])
    image = image.convert("RGB")
    new_image = image.resize((1080, 1920))
    os.rename(all_item_path[0], "gen_images\deletables" + item_path[0])
    new_image.save(all_item_path[0])
    

    if len(paths) > 1:
        bot.upload_album(paths, caption=text_img)
    else:
        bot.upload_photo(paths[0], caption=text_img)
        
    for i in paths:
        os.remove(i)

