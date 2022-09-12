# Import Libraries
from sys import argv
from src import *
from src.constants import *


def get_inputs() -> list:
    if(len(argv) != 2):
        raise Exception("File path not entered")
    file_path = argv[1]
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    return lines


# Main Driver function
def main():
    lines = get_inputs()
    subscriptions_object = Subscriptions()
    for line in lines:
        line = line.split(' ')
        if line[0] == START_SUBSCRIPTION:
            subscriptions_object.stringToDatetime(line[1])
        elif line[0] == ADD_SUBSCRIPTION:
            subscriptions_object.add_subscription(line[1], line[2])
        elif line[0] == ADD_TOPUP:
            subscriptions_object.add_topup(line[1], int(line[2]))
        else:
            subscriptions_object.print_renewal_details()


if __name__ == "__main__":
    main()