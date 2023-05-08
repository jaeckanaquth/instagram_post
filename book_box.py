import glob, os
from text_gen import post_text
from instabot import Bot
import config
from PIL import Image
import moviepy.editor as moviepy

def post_box(all_box_path):
    all_box = [i.split("\\")[-1] for i in all_box_path]
    all_box = [i.replace(".mp4", "") for i in all_box]
    company = [i.split(" - ")[0] for i in all_box]
    all_months = [i.split(" - ")[-1] for i in all_box]
    all_box = [i.split(" - ")[1] for i in all_box]

    bot = Bot()
    bot.login(username=config.username, password=config.password)
    
    box = all_box[0]
    month = all_months[0]
    company = company[0]

    context_for_text = f"Write me a Instagram post for of the new subsciption box from @{company} on theme {box} to my collection for the {month}, explain a little bit of the theme and add a related question at the end which people can answer in the comment section. Add ten hastags to the post. Seperate the tags from the text."

    text_vid = post_text(context_for_text) 
    thumbnail_vid = "E:/Books/book_box/" + company + ".jpg"
    image = Image.open(thumbnail_vid)
    image = image.convert("RGB")
    new_image = image.resize((1080, 1920))
    os.rename(thumbnail_vid, "gen_images/deletables/" + company + ".jpg")
    new_image.save(thumbnail_vid)

    bot.upload_video(all_box_path[0].replace("\\", "/"), caption=text_vid, thumbnail=thumbnail_vid)

    os.remove(all_box_path[0])
    try:
        os.remove(all_box_path[0] + "jpg")
    except:
        pass