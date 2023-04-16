const MetroCharges = {
    SERVICE_PCT_FEES: 0.02,
    DISCOUNT_PCT: 0.5
}

const PassengerCharges = {
    ADULT: 200,
    SENIOR_CITIZEN: 100,
    KID: 50
}

const InputPrefix = {
    BALANCE: "BALANCE",
    CHECK_IN: "CHECK_IN",
    PRINT_SUMMARY: "PRINT_SUMMARY"
}

const BalanceIndexes = {
    ID: 1,
    AMT: 2
}

const CheckInIndexes = {
    T_ID: 1,
    P_TYPE: 2,
    S_NAME: 3
}

const OutputPrefix = {
    TOTAL_COLLECTION: "TOTAL_COLLECTION",
    PASSENGER_TYPE_SUMMARY: "PASSENGER_TYPE_SUMMARY"
}

module.exports = Object.freeze({
    MetroCharges: MetroCharges,
    PassengerCharges: PassengerCharges,
    InputPrefix: InputPrefix,
    BalanceIndexes: BalanceIndexes,
    CheckInIndexes: CheckInIndexes,
    OutputPrefix: OutputPrefix
})