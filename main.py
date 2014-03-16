from iqdbparser import IQDBParser
from iqdbquerier import IQDBQuerier
from scrapers.animepictures import AnimePicturesScraper
from scrapers.danbooruscraper import DanbooruScraper
from scrapers.eshuushuuscraper import EShuuShuuScraper
from scrapers.gelbooruscraper import GelbooruScraper
from scrapers.genericimagescraper import GenericImageScraper
from scrapers.imagenotfoundexception import ImageNotFoundException
from scrapers.konachanscraper import KonachanScraper
from scrapers.mangadrawingscraper import MangaDrawingScraper
from scrapers.sankakucomplexscraper import SankakuComplexScraper
from scrapers.theanimegalleryscraper import TheAnimeGalleryScraper
from scrapers.yanderescraper import YandereScraper
from scrapers.zerochanscraper import ZerochanScraper


def get_scraper(link: str) -> GenericImageScraper:
    scrapers = [MangaDrawingScraper,
                EShuuShuuScraper,
                GelbooruScraper,
                KonachanScraper,
                SankakuComplexScraper,
                TheAnimeGalleryScraper,
                YandereScraper,
                DanbooruScraper,
                AnimePicturesScraper,
                ZerochanScraper]

    for scraper in scrapers:
        if scraper.identifier in link:
            return scraper(link)

    return None


def main():

    print("Talking to iqdb...")
    raw = IQDBQuerier.post("testdata/dat assu.jpg")

    print("Parsing response...")
    iqdbparser = IQDBParser(raw)

    # Grab all the links
    results = iqdbparser.get_all_matches()
    for result in results:
        print(result)

        link = result['link']

        # Given the link in the result, pick a scraper to find our link
        scraper = get_scraper(link)

        # If we found a scraper, let's use it
        if scraper:
            try:
                print(scraper.find_image_link())
            except ImageNotFoundException:
                print("Image not found.")

        else:
            print("We're missing a scraper for this site")

        # Make the result nice and easy on the eyes (yeah, right)
        print()


if __name__ == '__main__':
    main()