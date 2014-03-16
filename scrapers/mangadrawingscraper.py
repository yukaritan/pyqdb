from bs4 import BeautifulSoup

from downloader import Downloader

from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException


# Mangadrawing.net puts you on a landing page where the image is shown on yet another page, and
# they use forms to redirect you to it. Ugly workaround inc.


class MangaDrawingScraper(GenericImageScraper):
    identifier = "mangadrawing.net"

    def find_image_link(self) -> str:
        try:
            forms = [form for form in self._soup.find_all('form')
                     if 'name' in form.attrs and form.attrs['name'] == 'download']
            subpage = Downloader(forms[0].get('action')).geturl()
            return BeautifulSoup(subpage).find('div', id='image').find('img').get('src')

        except (IndexError, AttributeError):
            raise ImageNotFoundException()
