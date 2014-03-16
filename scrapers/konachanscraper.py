from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException


class KonachanScraper(GenericImageScraper):
    identifier = "konachan.com"

    def find_image_link(self) -> str:
        try:
            return self._soup.find_all("img", **{'id': 'image', 'class': 'image'})[0].get('src')
        except IndexError:
            raise ImageNotFoundException()