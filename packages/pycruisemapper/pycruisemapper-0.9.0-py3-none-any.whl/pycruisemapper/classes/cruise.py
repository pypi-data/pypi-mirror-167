from typing import Optional, List, Tuple

from datetime import datetime


class Cruise:
    name: Optional[str]
    url: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    itinerary: Optional[List[Optional[Tuple[str, str]]]]

    @property
    def days(self) -> Optional[int]:
        if self.end_date and self.start_date:
            return (self.end_date - self.start_date).days

    @classmethod
    def from_dict(cls, indict: dict):
        obj = cls()
        obj.name = indict.get("name")
        obj.url = indict.get("url")
        obj.start_date = indict.get("start_date")
        obj.end_date = indict.get("end_date")

        if "itinerary" in indict:
            obj.itinerary = []

            for item in indict["itinerary"].values():
                obj.itinerary.append((item["port"], item["date"]))

        return obj

    def __repr__(self):
        return self.__dict__.__repr__()
