from datetime import datetime, timedelta
from typing import Optional, List, Tuple
from locale import setlocale, LC_ALL

import re

from .location import Location
from .cruise import Cruise
from .flag import Flag
from .shipline import ShipLine
from ..const import IMAGE_BASE_PATH, TEMP_REGEX, HTML_REGEX, DEGREES_REGEX, SPEED_REGEX, GUST_REGEX


class Ship:
    id: Optional[int]
    name: Optional[str]
    url: Optional[str]
    url_deckplans: Optional[str]
    url_staterooms: Optional[str]
    image: Optional[str]
    flag: Optional[Flag]
    line: Optional[ShipLine]
    spec_length: Optional[int]  # stored in meters
    spec_passengers: Optional[int]
    year_built: Optional[int]
    last_report: Optional[str]
    imo: Optional[int]
    mmsi: Optional[int]
    latitude: Optional[float]
    longitude: Optional[float]
    cog: Optional[int]  # Course over Ground
    sog: Optional[int]  # Speed over Ground
    heading: Optional[int]
    timestamp: Optional[datetime]
    icon: Optional[int]
    hover: Optional[str]
    cruise: Optional[Cruise]
    path: Optional[List[Optional[Location]]]
    ports: Optional[List[Optional[Tuple[Optional[datetime], Optional[Location]]]]]
    destination: Optional[str]
    eta: Optional[datetime]
    current_temperature: Optional[float]  # Celsius
    minimum_temperature: Optional[float]  # Celsius
    maximum_temperature: Optional[float]  # Celsius
    wind_degrees: Optional[float]
    wind_speed: Optional[float]  # m/s
    wind_gust: Optional[float]  # m/s
    localtime: Optional[str]

    @classmethod
    def from_dict(cls, indict: dict):
        obj = cls()

        obj.id = indict.get("id")
        obj.name = indict.get("name", indict.get("ship_name"))
        obj.url = indict.get("url")
        obj.url_deckplans = indict.get("url_deckplans")
        obj.url_staterooms = indict.get("url_staterooms")

        if "image" in indict:
            obj.image = f"{IMAGE_BASE_PATH}{indict.get('image')}"

        if "flag" in indict:
            obj.flag = Flag(
                code=indict["flag"].get("code"),
                name=indict["flag"].get("name")
            )
        elif "ship_flag" in indict:
            obj.flag = Flag(
                code=indict.get("ship_flag")
            )

        if "line" in indict:
            obj.line = ShipLine(
                id=int(indict["line"]["id"]),
                title=indict["line"].get("title"),
                url=indict["line"].get("url")
            )
        elif "ship_line_id" in indict:
            obj.line = ShipLine(
                id=indict.get("ship_line_id"),
                title=indict.get("ship_line_title")
            )

        if "spec_length" in indict:
            parts = indict["spec_length"].split("/")
            for part in parts:
                if "m" in part:
                    try:
                        obj.spec_length = float(part.strip().split()[0])
                    except:
                        pass

        if "spec_passengers" in indict:
            obj.spec_passengers = int(indict["spec_passengers"])

        if "year_of_built" in indict:  # Those field names... 🤦
            obj.year_built = int(indict["year_of_built"])

        obj.last_report = indict.get("last_report")

        if "imo" in indict:
            obj.imo = int(indict["imo"])

        if "mmsi" in indict:
            obj.mmsi = int(indict["mmsi"])

        if "lat" in indict and "lon" in indict:
            obj.location = Location(indict["lat"], indict["lon"])

        if "cog" in indict:
            obj.cog = int(indict["cog"])

        if "sog" in indict:
            obj.sog = int(indict["sog"])

        if "heading" in indict:
            obj.heading = int(indict["heading"])

        if "ts" in indict:
            obj.timestamp = datetime.fromtimestamp(indict[ts])

        obj.icon = indict.get("icon")
        obj.hover = indict.get("hover")

        if "cruise" in indict:
            obj.cruise = Cruise.from_dict(indict["cruise"])

        if "path" in indict:
            if "points" in indict["path"]:
                obj.path = list()

                for point in indict["path"]["points"]:
                    lon, lat = point
                    obj.path.append(Location(lat, lon))

            if "ports" in indict["path"]:
                obj.ports = list()

                for port in indict["path"]["ports"]:
                    if "dep_datetime" in port:
                        departure = datetime.strptime(
                            port["dep_datetime"], "%Y-%m-%d %H:%M:%S")
                    else:
                        departure = None

                    if "lat" in port and "lon" in port:
                        location = Location(port["lat"], port["lon"])
                    else:
                        location = None

                    obj.ports.append(departure, location)

        obj.destination = indict.get("destination")

        if "eta" in indict:
            try:
                previous = setlocale(LC_ALL)
                setlocale(LC_ALL, "C")
                obj.eta = datetime.strptime(date_string, "%d %B, %H:%M")
                setlocale(LC_ALL, previous)
            except:
                obj.eta = None

        if "weather" in indict:
            temp_regex = re.compile(TEMP_REGEX)
            html_regex = re.compile(HTML_REGEX)
            degrees_regex = re.compile(DEGREES_REGEX)
            speed_regex = re.compile(SPEED_REGEX)
            gust_regex = re.compile(GUST_REGEX)

            if "temperature" in indict["weather"]:
                obj.current_temperature = float(re.search(temp_regex, re.sub(
                    html_regex, "", indict["weather"]["temperature"])).groups()[0])
            if "wind" in indict["weather"]:
                try:
                    obj.wind_degrees = int(
                        re.search(degrees_regex, indict["weather"]["wind"]).groups()[0])
                except:
                    pass

                try:
                    obj.wind_speed = float(
                        re.search(speed_regex, indict["weather"]["wind"]).groups()[0])
                except:
                    pass

                try:
                    obj.wind_gust = float(
                        re.search(speed_regex, indict["weather"]["wind"]).groups()[0])
                except:
                    pass

                obj.localtime = indict["weather"].get("localtime")

        return obj

    def __repr__(self):
        return self.__dict__.__repr__()
