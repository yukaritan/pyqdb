from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException


class YandereScraper(GenericImageScraper):
    identifier = "yande.re"

    def find_image_link(self) -> str:
        try:
            return self._soup.find("a", id='highres-show').get('href')
        except (IndexError, AttributeError):
            raise ImageNotFoundException()