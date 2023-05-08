from instabot import Bot
import glob, os
import config
from text_gen import post_text
from PIL import Image

def post_new_book(books_path):
	all_books = books_path.split("\\")[-1]
	all_books = [i.replace(".jpg", "") for i in all_books]
	all_book_names = [i.split(" - ")[0] for i in all_books]
	all_authors = [i.split(" - ")[1] for i in all_books]
	all_authors = [i.split("  ")[0] for i in all_authors]
	paths = []
	for i in range(len(all_book_names)):
		if all_book_names[0] == all_book_names[i]:
			paths.append(books_path[i])

	
	bot = Bot()
	bot.login(username=config.username, password=config.password)

	book_name = all_book_names[0]
	author = all_authors[0]

	image = Image.open(books_path[0])
	image = image.convert("RGB")
	new_image = image.resize((1080, 1920))
	os.remove(books_path[0])
	new_image.save(books_path[0])

	context_for_text = f"Write me a Instagram post for of the new book {book_name}, {author} to my collection, explain the theme and the plot and add a related question at the end which people can answer in the comment section. Add ten hastags to the post. Seperate the tags from the text."

	text_img = post_text(context_for_text)

	if len(paths) > 1:
		bot.upload_album(paths, caption=text_img)
	else:
		bot.upload_photo(paths[0], caption=text_img)

	for i in paths:
		os.remove(i)

