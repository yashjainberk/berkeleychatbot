import requests
from bs4 import BeautifulSoup


class Majors:
    def __init__(self, url):
        self.url = url
        self.majors = []
        self.major = BeautifulSoup(requests.get(url).content, 'html.parser')

    def store_majors(self):
        try:
            i = 0
            for m in self.major.select("li"):
                if i > 51:
                    self.majors.append(m.text)
                else:
                    i += 1
        except Exception as exc:
            exc.printStackTrace()

    def get_majors(self):
        return self.majors
