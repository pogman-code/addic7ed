from termcolor import colored

from .parser import Addic7edParser
from .file_crawler import FileCrawler
from .logger import init_logger
from .config import Config


def addic7ed():
    try:
        init_logger()
        Config.load()
        main()
    except (EOFError, KeyboardInterrupt, SystemExit):
        print(colored("\nBye!", "yellow"))
        exit(0)


def main():
    crawler = FileCrawler()
    parser = Addic7edParser()
    print(colored("Found %d show(s)" % len(crawler.episodes), "green"),
          end="\n\n")

    for filename, ep in crawler.episodes.items():
        subs = parser.parse(**ep.infos)

        print(ep)

        if not subs:
            print(colored("No subtitles for %s" % filename, "red"), end="\n\n")
            continue

        for i, sub in enumerate(subs):
            print("[%s] %s" % (colored(i, "yellow"), sub))

        if Config.dry_run:
            print()
            continue
        else:
            version = input('Download number?(auto for auto-download) ')
            if not version:
                print(colored("Nothing to do!", "yellow"),
                      end="\n\n")
                continue
            if version == 'auto':
                version = 0
                for i in range(1, len(subs)):
                    if (subs[i].downloads > subs[version].downloads or
                    subs[i].completion == 'Completed' and
                    subs[version].completion != 'Completed'):
                        version = i

            try:
                if Config.rename != "sub":
                    filename = subs[int(version)].download(ep.dir)
                    if filename and Config.rename == "video":
                        print(ep.rename(filename))
                else:
                    filename = subs[int(version)] \
                        .download(ep.dir, "%s.srt" % ep.filename)
                print(colored("Downloaded %s subtitle file" %
                              filename, "green"), end="\n\n")
            except Exception as e:
                print(colored(e, "red"),
                      end="\n\n")
