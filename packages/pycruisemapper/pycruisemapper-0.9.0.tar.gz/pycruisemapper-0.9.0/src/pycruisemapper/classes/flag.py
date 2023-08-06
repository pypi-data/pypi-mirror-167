from typing import Optional


class Flag:
    code: str
    name: str

    def __init__(self, code: str, name: Optional[str] = None):
        self.code = code
        self.name = name

    def __repr__(self):
        return self.__dict__.__repr__()
