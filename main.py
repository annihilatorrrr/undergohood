from argparse import ArgumentParser
from sys import exit as exiter

from pyrogram import Client

pbot = Client("pyrocil", 0, "", bot_token="", no_updates=True)
parser = ArgumentParser(description="Pyro Downloader !")
parser.add_argument("file_id", type=str, help="File id of the file.")
parser.add_argument("name", type=str, help="File name to be given to the downloaded media.")

args = parser.parse_args()
try:
    pbot.start()
except:
    exiter(1)
if file_id := args.get("file_id"):
    try:
        print(await pbot.download_media(file_id, file_name=args.get("name"), block=True))
        pbot.stop()
        exiter(0)
    except Exception:
        pass
exiter(1)
