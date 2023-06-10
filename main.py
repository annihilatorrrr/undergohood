from contextlib import suppress
from argparse import ArgumentParser
from shutil import rmtree
from sys import exit as exiter

from pyrogram import Client

parser = ArgumentParser(description="Pyro Downloader !", add_help=True, exit_on_error=True)
parser.add_argument("token", type=str, help="Tg bot token.")
parser.add_argument("file_id", type=str, help="File id of the file.")
parser.add_argument("fname", type=str, help="File name to be given to the downloaded media.", nargs="?")

args = parser.parse_args()
pbot = Client("pyrocil", 6, "eb06d4abfb49dc3eeb1aeb98ae0f581e", bot_token=args.token, no_updates=True)
try:
    pbot.start()
except:
    exiter(1)
err = 1
if file_id := args.file_id:
    with suppress(Exception):
        if fname := args.fname:
            print(pbot.download_media(file_id, file_name=fname, block=True))
        else:
            print(pbot.download_media(file_id, block=True))
        err = 0
pbot.stop(True)
if err:
    rmtree("./downloads", ignore_errors=True)
    rmtree("/downloads", ignore_errors=True)
    exiter(1)
else:
    exiter(0)
