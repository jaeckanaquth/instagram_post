# Instagram Automatic Posting

This is a Python script `main.py` that enables automatic posting on Instagram. The script randomly selects a type of content (such as a book, a new book, a review book, etc.) from a predefined list and posts it on Instagram. The specific content and related information are imported from separate files based on the selected type.

## Prerequisites

Before running the script, make sure you have the following prerequisites:

- Python 3.x installed on your system.
- Required Python packages: `instabot`, `PIL`, `moviepy`.
- Instagram account credentials: username and password.

## Getting Started

1. Clone or download the project repository.
2. Install the required Python packages by running the following command:
   ```
   pip install instabot Pillow moviepy
   ```
3. Open the `config.py` file and enter your Instagram account credentials.
4. Place your content files (images or videos) in the appropriate folders within the `E:/Books` directory.
5. Open the `main.py` file and run the script.

## How It Works

The `import_book()` function selects a random content type from a list of available types. It then imports the corresponding file and calls the relevant function to handle the posting process.

The `post_box()` function, imported from `book_box.py`, is an example of a content-specific function. It takes the file paths of all the content of the "book_box" type and processes them for posting on Instagram. The function uses the `instabot` package to log in to your Instagram account and upload the content.

Note: The other content-specific functions (`post_new_book()`, `post_review_book()`, etc.) follow a similar structure and can be implemented in separate files accordingly.

## Customization

1. To add or modify the available content types, edit the `lst` and `file_type` lists in the `import_book()` function.
2. For each content type, create a separate file (e.g., `new_book.py`, `review_book.py`) and define the corresponding `post_*` function.
3. Customize the content-specific functions to process and upload the content based on your requirements.

## Troubleshooting

If any errors occur during the posting process, the script will print an error message and wait for 1000 seconds before attempting to import and post another random content. You can modify this behavior by adjusting the sleep time (`sleep(1000)`) or implementing alternative error handling mechanisms.

## Note

Ensure that you have the necessary permissions and rights to post content on Instagram using automated scripts. Respect Instagram's terms of service and usage policies to avoid any account restrictions or suspensions.

For any additional questions or assistance, please contact the script author.
