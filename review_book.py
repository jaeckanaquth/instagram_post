from instabot import Bot
import glob, os
import config
from PIL import Image
from image_gen import post_images
from text_gen import post_text, image_text

def post_review_book(all_review_path):
	print("entering post_review_book")
	all_books = [i.split("\\")[-1] for i in all_review_path]
	all_books = [i.replace(".jpg", "").replace(".png", "") for i in all_books]
	all_book_names = [i.split(" - ")[0] for i in all_books]
	all_authors = [i.split(" - ")[1] for i in all_books]
	all_type = [i.split(" - ")[2] for i in all_books]
	all_ratings = [i.split(" - ")[3] for i in all_books]

	bot = Bot()
	bot.login(username=config.username, password=config.password)

	theme = all_book_names[0]
	author = all_authors[0]
	rating = all_ratings[0]
	type = all_type[0]

	image = Image.open(all_review_path[0].replace("\\", "/"))
	image = image.convert("RGB")
	new_image = image.resize((1080, 1350))
	os.rename(all_review_path[0].replace("\\", "/"), "gen_images/deletables/" + all_books[0] + '.jpg')
	new_image.save(all_review_path[0].replace("\\", "/"))

	context_for_text = f"Write me a Instagram post for of the book {theme} from {author} (I give it {rating}/5 stars), explain {type} and theme. Add ten hastags to the post. Seperate the tags from the text."
	context_for_prompt = f"Write me a prompt for creating a digital art scene from the book {theme} from {author} and mention the book is {type}. Keep the prompt simple!"

	text_img = post_text(context_for_text)
	gen_img, gen_img_path = post_images("review", theme, image_text(context_for_prompt))

	try:
		album_path = [all_review_path[0], gen_img_path]
	except:
		album_path = [all_review_path[0], f"gen_images/review_books/{theme}.jpg"]

	bot.album_upload(album_path, caption=text_img)

	os.remove(all_review_path[0])

