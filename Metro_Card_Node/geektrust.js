const fs = require("fs")
const {
    MetroAuthority
} = require('./src/core')
const {
    InputPrefix, BalanceIndexes
} = require("./src/constants")

const filename = process.argv[2]

fs.readFile(filename, "utf8", (err, data) => {
    if (err) throw err
    var inputLines = data.toString().split("\n")
    let authority = MetroAuthority()

    for (let line in inputLines) {
        line = line.replace('\n', '')
        row = row.split(' ')

        if (row[0] === InputPrefix.BALANCE) {
            authority.addToken(row[BalanceIndexes.ID], Number.int(
                row[BalanceIndexes.AMT]))
        } else if (row[0] === InputPrefix.CHECK_IN) {
            authority.checkIn(
                row[CheckInIndexes.T_ID],
                row[CheckInIndexes.P_TYPE],
                row[CheckInIndexes.S_NAME],
            )
        } else if (row[0] === InputPrefix.PRINT_SUMMARY)
            authority.print_summary()
    }

})