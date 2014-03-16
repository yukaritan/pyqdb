from urllib import request

import requests


class Downloader:
    """Talks to serrvers, asks them questions, brings you the responses!"""

    def __init__(self, url: str):
        self._url = url

        # Let's pretend we're not a bot
        self._headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"}

    def geturl(self) -> str:
        """Fetches the URL supplied in the constructor"""

        req = request.Request(url=self._url, headers=self._headers)
        with request.urlopen(req) as f:
            return f.read().decode('utf-8', 'ignore')

    def login(self, **data: dict) -> dict:
        """Logs into a site and returns the resulting cookies"""

        return requests.post(self._url, data=data).cookies

    def post(self, cookies: dict=None, files: dict=None, **form: dict) -> str:
        """Sends form data and files"""

        response = requests.post(url=self._url,
                                 cookies=cookies or {},
                                 files=files or {},
                                 data=form)

        return response.content.decode()