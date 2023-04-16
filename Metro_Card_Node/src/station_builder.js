const {
    BaseStation
} = require('./base')
const {
    OutputPrefix
} = require('./constants')


class MetroStation extends BaseStation {
    constructor(name) {
        super(name)
    }

    addPassenger = function(token, passenger_type, discount) {
        return super.addPassenger(token, passenger_type, discount)
    }

    printSummary = function() {
        console.log(OutputPrefix.TOTAL_COLLECTION,
            this.getName(), this.getEarnings(), this.getDiscountsGiven())
        console.log(OutputPrefix.PASSENGER_TYPE_SUMMARY)
        for (let passenger of this.getPassengersList()) {
            console.log(passenger[0], passenger[1])
        }
    }
}



class StationBuilder {
    #station_pool // All stations

    constructor() {
        this.#station_pool = new Map()
    }

    addStation = function(station) {
        if (this.#station_pool.has(station.getName())) {
            return false
        }
        this.#station_pool[station.getName()] = station
        return true
    }

    getStation = function(station_name) {
        return this.#station_pool.get(station_name)
    }

    getAllStations = function() {
        let stations = new Array.from(this.#station_pool.values())
        return stations
    }
}


modules.exports = {
    StationBuilder,
    MetroStation
}