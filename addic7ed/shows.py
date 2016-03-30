import requests

from bs4 import BeautifulSoup
from fuzzywuzzy import process
from termcolor import colored


class Shows:
    def __init__(self):
        print(colored("Fetching shows list, please wait...", "yellow"))
        data = requests.get("http://www.addic7ed.com/index.php").text
        soup = BeautifulSoup(data, "html.parser")
        self.list = [str(x.text) for x in
                     soup.find(id="qsShow").find_all("option")]

    def get(self, name):
        return process.extractOne(name, self.list)[0]
