import glob, os
from text_gen import post_text
from instabot import Bot
import config
from PIL import Image


def post_other_vid(all_other_path):
    all_other = [i.split("\\")[-1] for i in all_other_path]
    theme = [i.replace(".mp4", "") for i in all_other]

    bot = Bot()
    bot.login(username=config.username, password=config.password)

    theme = theme[0]
    context_for_text = f"Write me a Instagram post for {theme}, explain a little bit of the theme and add a related question at the end which people can answer in the comment section. Add ten hastags to the post. Seperate the tags from the text."

    text_vid = post_text(context_for_text) 
    thumbnail_vid = "E:/Books/other_vid/" + theme + ".jpg"
    image = Image.open(thumbnail_vid)
    image = image.convert("RGB")
    new_image = image.resize((1080, 1920))
    os.rename(thumbnail_vid, "gen_images/deletables/" + theme + ".jpg")
    new_image.save(thumbnail_vid)
    bot.upload_video(all_other_path[0], caption=text_vid, thumbnail=thumbnail_vid)

    os.remove(all_other_path[0])