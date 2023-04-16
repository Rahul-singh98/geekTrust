const { PassengerCharges, MetroCharges } = require('./constants')
const { MetroCard, TokenBuilder } = require("./token_builder")
const { MetroStation, StationBuilder } = require('./station_builder')


class MetroAuthority {
    #travelling_passengers // Passengers set
    #tokens // tokens
    #stations // stations

    constructor() {
        this.#travelling_passengers = new Set()
        this.#tokens = TokenBuilder()
        this.#stations = StationBuilder()
        this.initial_stations()
    }

    initial_stations = function() {
        this.addStation("CENTRAL")
        this.addStation("AIRPORT")
    }

    addStation = function(name) {
        n_station = MetroStation(name)
        this.#stations.addStation(n_station)
    }

    addToken = function(id, balance) {
        n_token = MetroCard(id, balance)
        this.#tokens.addToken(n_token)
    }

    checkIn = function(token_id, passenger_type, station_name) {
        discount = this.getDiscounts(token_id, passenger_type)
        token = this.#tokens.getToken(token_id)
        station = this.#stations.getStation(station_name)
        station.addPassenger(token, PassengerCharges[passenger_type], discount)
    }

    getDiscounts = function(token_id, passenger_type) {
        discount = 0
        if (token_id in this.#travelling_passengers) {
            discount = (
                PassengerCharges[passenger_type].value * MetroCharges.DISCOUNT_PCT.value)
            this.#travelling_passengers.remove(token_id)
        }
        else this.#travelling_passengers.add(token_id)
        return Number.int(discount)
    }

    print_summary = function() {
        for(let station of this.#stations.getAllStations()) {
            station.printSummary()
        }
    }
}


modules.exports = { MetroAuthority }