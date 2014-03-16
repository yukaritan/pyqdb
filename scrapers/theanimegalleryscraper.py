from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException


class TheAnimeGalleryScraper(GenericImageScraper):
    identifier = "theanimegallery.com"

    def find_image_link(self) -> str:
        try:
            sublink = self._soup.find_all("div", **{'class': 'download'})[0].a.get('href')
            return "http://www.theanimegallery.com" + sublink
        except (IndexError, AttributeError):
            raise ImageNotFoundException()