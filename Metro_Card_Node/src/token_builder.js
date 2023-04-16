const {
    BaseToken
} = require("./base")


class MetroCard extends BaseToken {
    /**
     * Metrocard constructor.
     * @param {Number.int} id
     * @param {String} name
     * @returns
     */
    constructor(id, balance) {
        super(id, balance);
    }

    /**
     * Deduct method deducts money from the card.
     * @param {Number.int} amount 
     * @returns 
     */
    deduct(amount) {
        return super.deduct(amount)
    }

    isEnoughBalance(required) {
        return super.isEnoughBalance(required)
    }

    topUp(amount) {
        return super.topUp(amount)
    }

}


class TokenBuilder {
    #token_pool //

    constructor() {
        this.#token_pool = new Map()
    }

    getAllTokens() {
        let tokens = new Array.from(this.#token_poll.values())
        return tokens
    }

    addToken(token) {
        if (this.#token_pool.has(token))
            return
        
        let token = new MetroCard()
        this.#token_pool[token.getId()] = token
        return true
    }

    getToken(token_id) {
        return this.#token_pool.get(token_id)
    }
}

modules.exports = {
    TokenBuilder
}