from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException


class TheAnimeGalleryScraper(GenericImageScraper):
    identifier = "theanimegallery.com"

    def find_image_link(self) -> str:
        try:
            sublink = self._soup.find("div", **{'class': 'download'}).a.get('href')
            return "http://www.theanimegallery.com" + sublink
        except (IndexError, AttributeError):
            raise ImageNotFoundException()