import re
import requests

from bs4 import BeautifulSoup
from serie_process import post_process
from constants import ADDIC7ED_URL, LANG


class Addic7edParser:
    def parse(self, serie, season, episode):
        url = "http://www.addic7ed.com/serie/%s/%s/%s" % (
            serie,
            season,
            episode
        )
        data = requests.get("%s/%s" % (url, LANG)).text
        soup = BeautifulSoup(data, "html.parser")

        tables = soup.find_all("table", attrs={"class": "tabel95"})

        subs = []
        for table in tables:
            inner_table = table.find("table", attrs={"class": "tabel95"})
            if inner_table:
                subs.append(Subtitle(inner_table, "%s/%s" % (url, "addic7ed")))
        return subs


class Subtitle:
    def __init__(self, html_table, referer):
        self.html = html_table
        self.referer = referer

        self.release = self._extract_release()
        self.language = self._extract_language()
        self.completion = self._extract_completion()
        self.comment, self.various = self._extract_comment()
        self.link = self._extract_link()

    def download(self):
        if self.completion != "Completed":
            raise IncompleteError()

        subs = requests.get(self.link, headers={"Referer": self.referer})
        filename = re.search(r'"(.*)"',
                             subs.headers["Content-Disposition"]).group(1)
        filename = re.sub(r"\.%s.*Addic7ed\.com" % self.release.split(" ")[1],
                          "",  filename)
        filename = post_process(filename)
        f = open(filename, 'w')
        f.write(subs.text)
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
        return \
    """%s
    %s
    %s
    %s
    %s
    """ % (self.release,
             self.language,
             self.completion,
             self.comment,
             self.various)


class IncompleteError(Exception):
    """ Raised when trying to download incomplete subtitle """
    def __str__(self):
        return "Can't download incomplete subtitle file..."
