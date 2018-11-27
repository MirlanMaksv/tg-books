import os
from telethon import TelegramClient, sync, utils
from telethon.tl.types import InputMessagesFilterDocument
from parser import args


def filter_by_name(doc):
    doc_name = get_name(doc).lower()
    mapped = map(lambda key_word: key_word in doc_name, args.key_words)
    return any(mapped)


def filter_by_ext(doc):
    return get_extension(doc) in args.extensions


def get_extension(doc):
    return os.path.splitext(get_name(doc))[1]


def get_name(doc):
    if doc.media.document and doc.media.document.attributes \
            and doc.media.document.attributes[0]:
        return doc.media.document.attributes[0].file_name

    return ""


def handle():
    client = TelegramClient("sessions", API_ID, API_KEY)

    try:
        client.start()

        docs = client.get_messages(args.channel, None, filter=InputMessagesFilterDocument)
        books = list(filter(filter_by_name, docs))
        if args.extensions:
            books = list(filter(filter_by_ext, books))

        total = len(books)
        print("Total number of books {}".format(total))

        print("Start downloading books? y/n")
        agree = input()

        if agree == "y":
            for i, book in enumerate(books):
                book_name = get_name(book)
                print("Downloading {index} of {total} | {name}".format(index=i+1, total=total, name=book_name))

                book.download_media(args.path + book_name)

    finally:
        client.disconnect()


API_ID = os.environ["TG_API_ID"]
API_KEY = os.environ["TG_API_HASH"]

if __name__ == "__main__":
    handle()
