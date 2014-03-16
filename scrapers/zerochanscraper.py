from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException


class ZerochanScraper(GenericImageScraper):
    identifier = "zerochan.net"

    def find_image_link(self) -> str:
        try:
            return self._soup.find("div", id='large').a.get('href')
        except (IndexError, AttributeError):
            raise ImageNotFoundException()
