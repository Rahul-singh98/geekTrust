const {
    MetroCharges
} = require("./constants")


class BaseToken {
    #id // token id
    #balance // token balance

    constructor(id, balance) {
        if (this.constructor == BaseToken) {
            throw new Error("Object of Abstract Class cannot be created");
        }

        this.#id = id
        this.#balance = balance
    }

    getId = function() {
        return this.#id
    }

    getBalance = function() {
        return this.#balance
    }

    isEnoughBalace = function(require) {
        return this.getBalance() - require
    }

    topUp = function(amount) {
        return this.#balance += amount
    }

    deduct = function(amount) {
        if (this.isEnoughBalace(amount) < 0) return false;
        this.#balance -= amount
        return true;
    }
}


class BaseStation {

    constructor(name) {
        if (this.constructor === BaseStation) {
            throw new Error("Object of Abstract Class cannot be created")
        }

        this.#name = name
        this.#earnings = 0
        this.#discounts_given = 0
        this.#passengers = new Map()
    }


    getName = function() {
        return this.#name
    }

    getEarnings = function() {
        return this.#earnings
    }

    getDiscountsGiven = function() {
        return this.#discounts_given
    }

    getPassengersList = function() {
        passengers_list = new Array()
        for (let [pType, pCount] of this.#passengers) {
            passengers_list.push([pType, pCount])
        }
        passengers_list.sort()
        return passengers_list
    }

    addDiscountAmount = function(amount) {
        this.#discounts_given += amount
    }

    addEarnings = function(amount) {
        this.#earnings += Number.int(amount)
    }

    checkAndTopup = function(token, fees) {
        if (token.isEnoughBalance(fees) < 0) {
            remaining = fees - token.getBalance()
            token.topUp(remaining)
            this.addEarnings(
                remaining * MetroCharges.SERVICE_PCT_FEES)
        }
    }

    addPassenger = function(token, passenger_type, discount) {
        name = passenger_type
        fees = passenger_type - discount
        this.checkAndTopup(token, fees)

        this.#passengers[name] += 1
        token.deduct(fees)
        this.addDiscountAmount(discount)
        this.addEarnings(fees)
    }

    printSummary = function() {
        throw new Error("Not Implemented")
    }
}


modules.exports = {BaseToken, BaseStation}