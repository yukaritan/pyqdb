from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException


class SankakuComplexScraper(GenericImageScraper):
    identifier = "sankakucomplex.com"

    def find_image_link(self) -> str:
        try:
            return self._soup.find("a", id='highres').get('href')
        except IndexError:
            raise ImageNotFoundException()