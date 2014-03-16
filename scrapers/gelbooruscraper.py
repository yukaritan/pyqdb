from bs4 import Tag

from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException


class GelbooruScraper(GenericImageScraper):
    identifier = "gelbooru.com"

    @staticmethod
    def _terms(tag: Tag) -> bool:
        return tag.name == 'a' and tag.get_text() == 'Original image'

    def find_image_link(self) -> str:
        try:
            return self._soup.find_all(self._terms)[0].get('href')
        except IndexError:
            raise ImageNotFoundException()