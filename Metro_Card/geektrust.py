import sys
import src
from src import InputPrefix,  BalanceIndexes, CheckInIndexes


def read_file(filepath, callback):
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

    authority = src.MetroAuthority()

    def callback(line: str):
        row = line.split(' ')
        if row[0] == InputPrefix.BALANCE.value:
            authority.addToken(row[BalanceIndexes.ID.value], int(
                row[BalanceIndexes.AMT.value]))
        elif row[0] == InputPrefix.CHECK_IN.value:
            authority.checkIn(
                row[CheckInIndexes.T_ID.value],
                row[CheckInIndexes.P_TYPE.value],
                row[CheckInIndexes.S_NAME.value],
            )
        elif row[0] == InputPrefix.PRINT_SUMMARY.value:
            authority.print_summary()
    
    read_file(filepath, callback)


if __name__ == "__main__":
    getInput()
