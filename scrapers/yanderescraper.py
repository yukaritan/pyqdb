from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException


class YandereScraper(GenericImageScraper):
    identifier = "yande.re"

    def find_image_link(self) -> str:
        try:
            return self._soup.find_all("a", id='highres-show')[0].get('href')
        except (IndexError, AttributeError):
            raise ImageNotFoundException()