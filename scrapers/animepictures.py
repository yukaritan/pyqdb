import json

from downloader import Downloader
from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException


class AnimePicturesScraper(GenericImageScraper):
    identifier = "anime-pictures.net"

    def scrape_site(self) -> str:
        """This site requires login"""

        with open('credentials/animepictures.json', 'r') as file:
            # The contents of the file is expected to be something along the lines of
            # {"login": "waifu-chan", "password": "muh_seacritz!!"}
            # where "login" and "password" are the names of the fields used in the login form on the website.
            credentials = json.load(file)

        cookies = Downloader("http://anime-pictures.net/login/submit").login(**credentials)
        return Downloader(self._url).post(cookies=cookies)

    def find_image_link(self) -> str:
        try:
            sublink = self._soup.find_all('div', id='big_preview_cont')[0].a.get('href')
            return "http://anime-pictures.net" + sublink
        except (IndexError, AttributeError):
            raise ImageNotFoundException()