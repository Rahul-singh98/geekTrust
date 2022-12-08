from unittest import TestCase, main

import src
from src import station_builder


class Test_StationBuilder(TestCase):

    def setUp(self) -> None:
        self._station_builder = station_builder.StationBuilder()
        station = src.MetroStation("CENTRAL")
        self._station_builder.addStation(station)
        return super().setUp()

    def tearDown(self) -> None:
        del self._station_builder
        return super().tearDown()

    def test_addStation(self):
        station = src.MetroStation("AIRPORT")
        self.assertTrue(
            self._station_builder.addStation(station))

    def test_addStation2(self):
        station = src.MetroStation("CENTRAL")
        self.assertFalse(
            self._station_builder.addStation(station))

    def test_getStation(self):
        self.assertIsNotNone(self._station_builder.getStation("CENTRAL"))

    def test_getAllStations(self):
        sz = len(self._station_builder.getAllStations())
        self.assertEqual(sz, 1)


if __name__ == "__main__":
    main()
