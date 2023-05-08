from instabot import Bot
import glob, os
import config
from PIL import Image
from image_gen import post_images
from text_gen import post_text, image_text

def post_story(all_review_path):
    bot = Bot()
    bot.login(username=config.username, password=config.password)

    gen

