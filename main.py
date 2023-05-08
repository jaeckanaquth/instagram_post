import random
import glob
from time import sleep
def import_book():
    global count
    lst = ["book_box", "new_book", "review_books", "box_items", "other_vid", "started_book"]
    file_type = [".mp4", ".jpg", ".jpg", ".jpg", ".mp4", ".jpg"]
    final_list = []
    dct = {}
    
    for k, i in enumerate(lst):
        dct[i]= {'path':glob.glob("E:/Books/" + i + "/*" + file_type[k]), 'file_type':file_type[k], 'file_name':i}

        if len(dct[i]['path']) != 0:
            final_list.append(i)
    posting = random.choice(final_list)

    try:
        print(dct[posting]['file_name'])
        if posting == "book_box":
            from book_box import post_box
            post_box(dct[posting]['path'])
        elif posting == "new_book":
            from new_book import post_new_book
            post_new_book(dct[posting]['path'])
        elif posting == "review_books":
            from review_book import post_review_book
            post_review_book(dct[posting]['path'])
        elif posting == "box_items":
            from box_items import post_box_items
            post_box_items(dct[posting]['path'])
        elif posting == "other_vid":
            from other_vid import post_other_vid
            post_other_vid(dct[posting]['path'])
        elif posting == "started_book":
            from started_book import post_started_book
            post_started_book(dct[posting]['path'])
    except Exception as e:
        print(f"This went wrong: {e}")
        sleep(1000)
        import_book()
import_book()