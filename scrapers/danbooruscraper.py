from bs4 import Tag

from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException



# There is no easy way to identify a download link, other than that it's inside a <li>-tag,
# trailing the string "Size:"...


class DanbooruScraper(GenericImageScraper):
    identifier = "danbooru.donmai.us"

    @staticmethod
    def _terms(tag: Tag) -> bool:
        return tag.name == 'li' and 'Size:' in tag.get_text()

    def find_image_link(self) -> str:
        try:
            sublink = self._soup.find(self._terms).a.get('href')
            return "http://danbooru.donmai.us" + sublink
        except (IndexError, AttributeError):
            raise ImageNotFoundException()