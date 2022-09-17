from sys import argv
from src import *

def main():
    """
    Sample code to read inputs from the file
    """
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]

    builder = product_builder.Builder()

    with open(file_path, 'r') as f:
        for row in f.readlines():
            row = row.replace("\n", "")
            columns = row.split(' ')

            if columns[0].startswith("ADD_ITEM"):
                builder.add_item(columns[1], int(columns[2]))

            else:
                builder.print_bill()
    
if __name__ == "__main__":
    main()