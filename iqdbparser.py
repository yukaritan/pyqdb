from bs4 import BeautifulSoup, Tag


class IQDBParser:
    """Takes horrid IQDB code and spits out dicts containing the best and additional matches."""

    def __init__(self, raw: str):
        self._soup = BeautifulSoup(raw)

    def get_best_match(self) -> dict:
        """Returns the best match"""

        tables = self._soup.find_all("table")
        for table in tables:
            if "Best match" in table.get_text():
                return self.parse_match(table)

    def get_additional_matches(self) -> dict:
        """Returns all the additional matches"""

        tables = self._soup.find_all("table")
        for table in tables:
            if "Additional match" in table.get_text():
                yield self.parse_match(table)

    def get_all_matches(self) -> dict:
        """Calls the other two funcitons and yields the results"""

        yield self.get_best_match()
        for match in self.get_additional_matches():
            yield match

    @staticmethod
    def parse_match(match: Tag) -> dict:
        """The following code is objectively shit, and prone to breaking. I blame IQDB's horrendous HTML."""

        rows = match.find_all('tr')
        link = rows[1].td.a.get("href")
        thumb = rows[1].td.img.get("src")
        size = tuple(int(n) for n in rows[3].td.get_text().split(' ')[0].split('×'))
        similarity = int(rows[4].get_text().split('%')[0])

        return {"link": link,
                "thumb": thumb,
                "size": size,
                "similarity": similarity}