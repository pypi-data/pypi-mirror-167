# pyCruiseMapper

Python package for retrieving data on (cruise) ships from cruisemapper.com

This is a very basic implementation, and it might stay like this, but I still
wanted to share it in case anyone finds it useful. I can't promise that I will
keep this package updated or that it's going to work forever as is, though.

I wanted to keep it simple, so this package has no dependencies outside the
standard library. Tested on Python 3.10.6 only, but should work on any >= 3.8.

## Basic Usage

```python
from pycruisemapper import CruiseMapper

cruisemapper = CruiseMapper()

# First, retrieve basic data on all ships
# Returns a list of Ship objects

all_ships = cruisemapper.get_ships()

# Then, select the ship(s) you are interested in from that list

meinschiff1 = list(filter(lambda x: x.imo == 9783564))[0]

# You may want to retrieve additional information of a ship's current status
# Pass the Ship object into fill_ship and it will return an object with details

meinschiff1 = cruisemapper.fill_ship(meinschiff1)

# You can now access things like the current location or temperature

location = meinschiff1.location # .latitude/.longitude
temperature = meinschiff1.current_temperature # returned in °C

# Check the class definitions in /classes/*.py to see all possible attributes
```