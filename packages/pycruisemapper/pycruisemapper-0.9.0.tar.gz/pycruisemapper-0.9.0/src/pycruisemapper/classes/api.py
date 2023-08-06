from .http import HTTPRequest
from .ship import Ship
from ..const import SHIPS_URL, SHIP_URL

from urllib.parse import urlencode
from datetime import datetime
from typing import List, Dict

import json


class CruiseMapper:
    def request_ships(self, **kwargs) -> List[Dict]:
        payload = {
            "minLat": kwargs.get("min_lat", -90),
            "maxLat": kwargs.get("max_lat", 90),
            "minLon": kwargs.get("min_lon", -180),
            "maxLon": kwargs.get("max_lon", 180),
            "filter": ",".join(kwargs.get("filter", [str(i) for i in range(100)])),
            "zoom": kwargs.get("zoom", ""),
            "imo": kwargs.get("imo", ""),
            "mmsi": kwargs.get("mmsi", ""),
            "t": int(kwargs.get("timestamp", datetime.now().timestamp()))
        }

        request = HTTPRequest(f"{SHIPS_URL}?{urlencode(payload)}")

        return json.loads(request.open().read())

    def request_ship(self, **kwargs) -> Dict:
        payload = {
            "imo": kwargs.get("imo", ""),
            "mmsi": kwargs.get("mmsi", ""),
            "zoom": kwargs.get("zoom", "")
        }

        request = HTTPRequest(f"{SHIP_URL}?{urlencode(payload)}")

        return json.loads(request.open().read())

    def get_ships(self, **kwargs) -> List[Ship]:
        """Get data on all ships using ships.json endpoint

        Note that **kwargs don't seem to have any influence here, so if you
        need a particular vessel by IMO or MMSI, first get all ships by simply
        calling get_ships(), then use a filter on the output like this:

            MeinSchiff1 = list(filter(lambda x: x.imo == 9783564))[0]

        You may then pass that object into fill_ship() to retrieve additional
        data from the ship.json endpoint.

        Returns:
            List[Ship]: A list of Ship objects for all ships
        """

        return [Ship.from_dict(d) for d in self.request_ships(**kwargs)]

    def get_ship(self, **kwargs) -> Ship:
        """Get data on a single ship using ship.json endpoint.

        Note that this lacks some important information, so you would almost
        always want to get all ships through get_ships(), then pass the returned
        Ship object to fill_ship() to add the information retrieved by get_ship(). 

        Returns:
            Ship: Ship object with the data returned by ship.json
        """
        return Ship.from_dict(self.request_ship(**kwargs))

    def fill_ship(self, ship: Ship) -> Ship:
        """Add missing data to Ship object retrieved from get_ships

        Args:
            ship (Ship): "Raw" Ship object as returned from get_ships

        Returns:
            Ship: Ship object with data from both get_ships and get_ship
        """

        if not (ship.imo or ship.mmsi):
            raise ValueError("Ship object has no identifier, cannot process")
        
        details = self.get_ship(mmsi=ship.mmsi, imo=ship.imo)
        ship.__dict__.update({k: v for k, v in details.__dict__.items() if v is not None})
        return ship
