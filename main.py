from argparse import ArgumentParser
from contextlib import suppress
from shutil import rmtree
from sys import exit as exiter
from sys import version_info

from pyrogram import Client

if version_info[0] < 3 or version_info[1] < 11:
    exiter("Python version is lower than: 3.11.x!")

parser = ArgumentParser(description="Pyro Downloader !",
                        add_help=True,
                        exit_on_error=True)
parser.add_argument("token", type=str, help="Tg bot token.")
parser.add_argument("file_id", type=str, help="File id of the file.")
parser.add_argument("fname",
                    type=str,
                    help="File name to be given to the downloaded media.",
                    nargs="?")

args = parser.parse_args()
pbot = Client(
    "pyrocil",
    6,
    "eb06d4abfb49dc3eeb1aeb98ae0f581e",
    bot_token=args.token,
    no_updates=True,
)
err, a = 1, ""
try:
    pbot.start()
except Exception:
    parser.exit(1, "Couldn't start the client!\n")
with suppress(Exception):
    if fname := args.fname:
        a = f"{pbot.download_media(args.file_id, file_name=fname)}\n"
    else:
        a = f"{pbot.download_media(args.file_id)}\n"
    err = 0
pbot.stop(True)
if err:
    rmtree("./downloads", ignore_errors=True)
    rmtree("/downloads", ignore_errors=True)
    parser.exit(1, "Something went Wrong with downloading!\n")
else:
    parser.exit(0, a)
