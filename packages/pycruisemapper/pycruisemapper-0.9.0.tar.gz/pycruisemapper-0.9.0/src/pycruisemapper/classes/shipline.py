from typing import Optional


class ShipLine:
    id: int
    title: str
    url: Optional[str]

    def __init__(self, id: int, title: str, url: Optional[str] = None):
        self.id = id
        self.title = title
        self.url = url

    def __repr__(self):
        return self.__dict__.__repr__()