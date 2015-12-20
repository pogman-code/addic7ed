#! /usr/bin/env python3

from parser import Addic7edParser
from file_crawler import FileCrawler


crawler = FileCrawler()
parser = Addic7edParser()

for filename,v in crawler.episodes.items():
    subs = parser.parse(**v.infos)

    if not subs:
        print("No subtitles for %s" % filename)
        continue

    print(filename)
    for i, sub in enumerate(subs):
        print("[%s] %s" % (i, sub))

    try:
        version = input('Download number? ')
    except (KeyboardInterrupt, SystemExit):
        print("\nOK...")
        exit(0)

    print()
    if not version:
        continue

    try:
        filename = subs[int(version)].download()
        if filename:
            v.rename(filename)
    except Exception as e:
        print(e)
