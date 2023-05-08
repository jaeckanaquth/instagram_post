from instabot import Bot
import glob, os
import config
from text_gen import post_text
from PIL import Image


def post_started_book(all_started_books_path):
	paths = []
	all_books = [i.split("\\")[-1] for i in all_started_books_path]
	all_books = [i.replace(".jpg", "").replace(".png", "") for i in all_books]
	all_book_names = [i.split(" - ")[0] for i in all_books]
	all_authors = [i.split(" - ")[1] for i in all_books]
	all_type = [i.split(" - ")[2] for i in all_books]
	all_ratings = [i.split(" - ")[3] for i in all_books]
	for i in range(len(all_book_names)):
		if all_book_names[0] == all_book_names[i]:
			paths.append(all_started_books_path[i])
		else:
			pass

	bot = Bot()
	bot.login(username=config.username, password=config.password)

	theme = all_book_names[0]
	author = all_authors[0]
	rating = all_ratings[0]
	type = all_type[0]

	image = Image.open(all_started_books_path[0])
	image = image.convert("RGB")
	new_image = image.resize((1080, 1920))
	os.rename(all_started_books_path[0], )
	new_image.save(all_started_books_path[0])
    

	context_for_text = f"Write me a Instagram post for of the book {theme} from {author} (I started reading this book), explain {type} and theme. Add ten hastags to the post. Seperate the tags from the text."

	text_img = post_text(context_for_text)

	if len(paths) > 1:
		bot.album_upload(paths, caption=text_img)
	else:
		bot.photo_upload(paths[0], caption=text_img)

	for i in paths:
		os.remove(i)

