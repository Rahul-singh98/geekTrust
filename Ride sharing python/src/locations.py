from math import sqrt
from dataclasses import dataclass


@dataclass
class Location:
    def __init__(self, x: int, y: int):
        """Geographical location class which requires x, y

        Parameters:
        -----------
            x: int
                represents the X coordinate
            y: int
                represents the Y coordinate
        """
        self.x = x
        self.y = y

    def distance(self, other):
        """Returns the Euclidean distance between a, b"""
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def within_distance(self, other, max_distance):
        return self.distance(other) <= max_distance
