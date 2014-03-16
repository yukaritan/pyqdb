from bs4 import BeautifulSoup

from downloader import Downloader


class GenericImageScraper:
    """
    Provides a constructor and two functions, find_image_link() -> str, and scrape_site() -> str.
    The constructor accepts a URL for the site you want scraped, and tries to turn it into beautiful soup,
    which is then stored in self._soup.

    Scrape_site is only here in case it needs overridages, but the base implementation should
    suffice in most cases. It downloads a URL and returns whatever response it gets.

    Find_image_link goes through self._soup and returns a link, as per here undefined magic.
    In other words, it's up to you to figure out how to do it.
    """

    identifier = ""

    def __init__(self, url: str):
        self._url = url
        self._soup = BeautifulSoup(self.scrape_site())

    def scrape_site(self) -> str:
        return Downloader(self._url).geturl()

    def find_image_link(self) -> str:
        """
        This is where the magic happens.
        Override this function in a site specific scraper, and make sure it returns exactly one string;
        the link for the picture.
        """
        raise NotImplementedError()