from components import GetSnippet, PushSnippet, Language

import argparse
from os import path

parser = argparse.ArgumentParser(description="Codehub CLI app")
parser.add_argument("-g", "--get", type=str, required=False, metavar='', help="use this for getting snippet by ID ")
parser.add_argument("-a", "--app", type=str, required=False, metavar='', help="Scripts name")
parser.add_argument("-t", "--title", type=str, required=False, metavar='', help="Title")
parser.add_argument("-d", "--desc", type=str, required=False, metavar='', help="details or description")
parser.add_argument("-l", "--lang", type=str, required=False, metavar='', help="Scripts name")
parser.add_argument("-e", "--error", type=str, required=False, metavar='', help="Log|Bug (as string not a file)")

args = parser.parse_args()

if args.get is not None:
    req_snippet = GetSnippet(args.get)
    get_callback = req_snippet.get()
    try:
        print(get_callback['link'])
    except KeyError:
        print("couldn't find any snippet with mentioned ID")
    exit()


if not path.isfile(args.app):
    print(f"Couldn't find any file named as {args.app}")
    exit()

with open(args.app, "r") as user_file:
    req = PushSnippet(args.title, user_file.read(), args.lang, args.desc, args.error)
    call_back = req.push()
    print(f"Done !\nhere is your link {call_back['link']}")