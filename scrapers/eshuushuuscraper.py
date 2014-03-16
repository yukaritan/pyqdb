from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException


class EShuuShuuScraper(GenericImageScraper):
    identifier = "e-shuushuu.net"

    def find_image_link(self) -> str:
        try:
            sublink = self._soup.find_all("a", **{'class': 'thumb_image'})[0].get('href')
            return "http://e-shuushuu.net" + sublink
        except (IndexError, AttributeError):
            raise ImageNotFoundException()
