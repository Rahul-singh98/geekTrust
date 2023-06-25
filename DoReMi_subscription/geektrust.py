# Import Libraries
from sys import argv
from src.services.subscription_service import SubscriptionsService


EXPECTED_ARGS = 2


def main():
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    """
    if len(argv) != EXPECTED_ARGS:
        raise Exception("File path not entered")

    subscription_service = SubscriptionsService()
    file_path = argv[1]

    with open(file_path, "r") as file:
        for line in file:
            command, *args = line.split()
            func = getattr(subscription_service, command.lower())
            func(*args)


if __name__ == "__main__":
    main()
