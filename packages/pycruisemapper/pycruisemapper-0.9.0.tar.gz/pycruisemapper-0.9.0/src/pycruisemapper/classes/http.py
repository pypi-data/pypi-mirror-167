from urllib.request import Request, urlopen

from ..const import REQUIRED_HEADERS


class HTTPRequest(Request):
    def __init__(self, url, *args, **kwargs):
        super().__init__(url, *args, **kwargs)
        self.headers.update(REQUIRED_HEADERS)

    def open(self):
        return urlopen(self)
