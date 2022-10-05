from sys import argv
from src.constants import InputConstants

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    with open(file_path, 'r') as f:
        for line in f:
            line.replace('\n', '')
            if line.startswith(InputConstants.BOOK.name):
                pass
            elif line.startswith(InputConstants.ADDITIONAL.name):
                pass
            elif line.startswith(InputConstants.REVENUE.name):
                pass
    
if __name__ == "__main__":
    main()