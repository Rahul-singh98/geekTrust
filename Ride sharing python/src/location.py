class Location:
    """Location which stores x and y co-ordinates."""

    def __init__(self, x: int, y: int):
        """Contructor of Location.

        Parameters:
        -----------
            x (int): x coordinate
            y (int): y coordinate    
        """
        self._x = x
        self._y = y
