import re
import requests

from bs4 import BeautifulSoup
from termcolor import colored
from fuzzywuzzy import fuzz

from addic7ed.constants import ADDIC7ED_URL
from addic7ed.config import Config


class Addic7edParser:
    def parse(self, serie, season, episode, group):
        url = "%s/serie/%s/%s/%s" % (
            ADDIC7ED_URL,
            serie,
            season,
            episode
        )
        data = requests.get("%s/%s" % (url, Config.lang["code"])).text
        soup = BeautifulSoup(data, "html.parser")

        tables = soup.find_all("table", attrs={"class": "tabel95"})

        subs = []
        for table in tables:
            inner_table = table.find("table", attrs={"class": "tabel95"})
            if inner_table:
                subs.append(Subtitle(inner_table,
                                     "%s/%s" % (url, "addic7ed"),
                                     group))
        return sorted(subs,
                      key=lambda s: (s.match_ratio, s.downloads),
                      reverse=True)


class Subtitle:
    def __init__(self, html_table, referer, best_group):
        self.html = html_table
        self.referer = referer

        self.release = self._extract_release()
        self.match_ratio = fuzz.ratio(self.release.split(" ")[-1].upper(),
                                      best_group.upper())
        self.language = self._extract_language()
        self.completion = self._extract_completion()
        self.comment, self.various = self._extract_comment()
        m = re.search(r"([0-9]+) Downloads", self.various)
        self.downloads = int(m.group(1))
        self.link = self._extract_link()

    def download(self, dir, filename=None):
        if self.completion != "Completed":
            raise IncompleteError()

        subs = requests.get(self.link, headers={"Referer": self.referer})

        if not filename:
            filename = re.search(r'"(.*)"',
                                 subs.headers["Content-Disposition"]).group(1)
            filename = re.sub(r"\.%s.*Addic7ed\.com" %
                              re.escape(self.release.replace("Version ", "")),
                              "",  filename)
            filename = re.sub(r'[<>:"/\\|?*]', '', filename).strip()
        if Config.keep_lang:
            f = open("%s/%s.%s%s" % (dir, filename[:-4],
                                     Config.lang["iso"],
                                     filename[-4:]), 'wb')
        else:
            f = open("%s/%s" % (dir, filename), 'wb')
        f.write(subs.content)
        f.close()
        return filename[:-4]

    def _extract_release(self):
        return self.html.find("td", attrs={"class": "NewsTitle"}) \
            .get_text(strip=True).split(",")[0]

    def _extract_language(self):
        return self.html.find("td", attrs={"class": "language"}) \
            .get_text(strip=True)

    def _extract_completion(self):
        return self.html.find("td", attrs={"width": "19%"}) \
            .get_text(strip=True)

    def _extract_comment(self):
        tds = self.html.find_all("td", attrs={"class": "newsDate"})
        return (tds[0].get_text(strip=True),
                tds[1].get_text(strip=True).replace("Â", ""))
        #  Damn, this replace() call sucks balls

    def _extract_link(self):
        return "%s%s" % (ADDIC7ED_URL,
                         self.html.find_all("a", attrs={
                             "class": "buttonDownload"
                         })[-1].get("href"))

    def __str__(self):
        complete = "green" if (self.completion == "Completed") else "red"
        return ("%s"  # " (%s)"
                "\n    %s | %s"
                "\n    %s"
                "\n    %s") % (
            colored(self.release, "white", attrs=['bold']),
            # colored("%02d%%" % self.match_ratio,
            #         "red" if self.match_ratio < 75 else "green"),
            self.language,
            colored(self.completion, complete),
            colored(self.comment, "white", attrs=["dark"]),
            colored(self.various, "white", attrs=["dark"])
        )


class IncompleteError(Exception):
    """ Raised when trying to download incomplete subtitle """
    def __str__(self):
        return "Can't download incomplete subtitle file..."
