from termcolor import colored

from .parser import Addic7edParser
from .file_crawler import FileCrawler

crawler = FileCrawler()
parser = Addic7edParser()


def addic7ed():
    for filename, v in crawler.episodes.items():
        subs = parser.parse(**v.infos)

        print(colored("\n%s - Season %02d Episode %02d (%s)" % (
            v.infos["serie"].replace("_", " ").title(),
            v.infos["season"],
            v.infos["episode"],
            filename
        ), "blue"))

        if not subs:
            print(colored("No subtitles for %s" % filename, "red"))
            continue

        for i, sub in enumerate(subs):
            print("[%s] %s" % (colored(i, "yellow"), sub))

        try:
            version = input('Download number? ')
        except (KeyboardInterrupt, SystemExit):
            print(colored("\nBye!", "yellow"))
            exit(0)

        if not version:
            print(colored("Nothing to do!", "yellow"))
            continue

        try:
            filename = subs[int(version)].download()
            if filename:
                v.rename(filename)
        except Exception as e:
            print(colored(e, "red"))
