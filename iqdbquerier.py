from downloader import Downloader


class IQDBQuerier:
    """Posts an image to IQDB, downloads and returns the response"""

    downloader = Downloader("http://iqdb.org/")
    services = ("service[]", [0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13])  # Cross every checkbox.
                                                                     # I may have to take a few out because
                                                                     # they require login..

    @staticmethod
    def post(image_path: str) -> str:
        """Posts an image to IQDB, downloads and returns the response"""

        file = open(image_path, 'rb')
        return IQDBQuerier.downloader.post(services=IQDBQuerier.services,
                                           files={'file': file})
