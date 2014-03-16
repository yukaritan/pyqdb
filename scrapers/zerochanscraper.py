from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException


class ZerochanScraper(GenericImageScraper):
    identifier = "zerochan.net"

    def find_image_link(self) -> str:
        try:
            return self._soup.find_all("div", id='large')[0].a.get('href')
        except (IndexError, AttributeError):
            raise ImageNotFoundException()
