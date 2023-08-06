IMAGE_BASE_PATH = "https://www.cruisemapper.com/"

SHIPS_URL = "https://www.cruisemapper.com/map/ships.json"
SHIP_URL = "https://www.cruisemapper.com/map/ship.json"

REQUIRED_HEADERS = {"X-Requested-With": "XMLHttpRequest",
                    "User-Agent": "Mozilla/5.0 (compatible: pyCruiseMapper; https://kumig.it/kumitterer/pycruisemapper)"}

TEMP_REGEX = "(-?\d+\.?\d*) ?°C"
HTML_REGEX = "<.*?>"
DEGREES_REGEX = "(\d+) ?°"
SPEED_REGEX = "\/ ?(\d+.?\d*) ?m\/s"
GUST_REGEX = "Gust: (\d+.?\d*) ?m\/s"