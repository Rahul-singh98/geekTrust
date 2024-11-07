import sys
from src import System


def read_file(filepath, callback):
    """Used to read file line by line and each time calls to callback"""
    with open(filepath, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            line = line.strip()
            if callable(callback):
                callback(line)


def getInput(filepath=None):
    """
        Reads inputs from commandline argument or 
        optionally from an file(for testing)

        Args:
            filepath(str, optional): input file name
            Default is none
    """
    if filepath is None:
        filepath = sys.argv[-1]

    system = System()

    def callback(line: str):
        cols = line.split(' ')
        if cols[0] == "ADD_DRIVER":
            system.add_driver(cols[1], int(cols[2]), int(cols[3]))

        elif cols[0] == "ADD_RIDER":
            system.add_rider(cols[1], int(cols[2]), int(cols[3]))

        elif cols[0] == "MATCH":
            system.match(cols[1])

        elif cols[0] == "START_RIDE":
            system.start_ride(cols[1], int(cols[2]), cols[3])

        elif cols[0] == "STOP_RIDE":
            system.stop_ride(cols[1], int(cols[2]), int(cols[3]), int(cols[4]))

        elif cols[0] == "BILL":
            system.bill(cols[1])

        else:
            print("Unknown input provided.")

    read_file(filepath, callback)


if __name__ == "__main__":
    getInput()
