class Location:
    latitude: float
    longitude: float

    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return self.__dict__.__repr__()
