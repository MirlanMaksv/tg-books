import os
import argparse

CHANNEL = "python_textbooks"
KEY_WORDS = ["Computer vision", "Machine learning"]
EXTENSIONS = [".pdf"]


descr = "Book downloader from telegram chats"
parser = argparse.ArgumentParser(description=descr)

parser.add_argument("-a", "--action", type=str, required=True,
                    help="Download books or just list their names")
parser.add_argument("-c", "--channel", type=str, default=CHANNEL, required=False,
                    help="Channel to search in")
parser.add_argument("-kw", "--key-words", nargs="+", default=KEY_WORDS, required=False,
                    help="Key words to search, ex: 'Computer vision' 'Machine learning'")
parser.add_argument("-e", "--extensions", nargs="+", default=EXTENSIONS, required=False,
                    help="File extensions")

args = parser.parse_args()
args.key_words = list(map(lambda x: x.lower(), args.key_words))
args.path = args.channel + "-downloads/"
