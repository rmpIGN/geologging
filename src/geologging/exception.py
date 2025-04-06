from ._typing import SupportsGeoInterface


class GeoException(Exception):

    def __init__(self, location: SupportsGeoInterface, *args):
        super().__init__(*args)
        self.__geo_interface__ = location
