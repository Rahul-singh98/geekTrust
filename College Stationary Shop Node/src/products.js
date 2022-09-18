const constants = require('./constants.js')

class IProduct {
    constructor(price, discount) {
        this.price = price
        this.discount = discount
        this.max_purchase_qty = 0
        this.qty = 0
    }

    check_max_limit(qty) {
        return this.qty >= this.max_purchase_qty;
    }

    set_quantity(qty) {
        if(this.check_max_limit(qty)) {
            this.qty = qty;
            return true;
        } else {
            return false;
        }
    }

    get_total_cost() {
        return this.price * this.qty;
    }

    get_discount_price() {
        return this.get_total_cost() * this.discount;
    }
}


class ClothingPolicy extends IProduct{
    constructor(price, discount) {
        super(price, discount);
        this.set_max_limit()
    }

    set_max_limit() {
        this.max_purchase_qty = constants.Constants.MAX_CLOTHING_ITEMS_QTY;
    }
}


class StationaryPolicy extends IProduct {
    constructor(price, discount) {
        super(price, discount);
        this.set_max_limit()
    }

    set_max_limit() {
        this.max_purchase_qty = constants.Constants.MAX_STATIONARY_ITEMS_QTY;
    }
}


class TShirt extends ClothingPolicy {
    constructor() {
        super(constants.TShirtEnum.price, constants.TShirtEnum.discount);
    }
}

class Jacket extends ClothingPolicy {
    constructor() {
        super(constants.JacketEnum.price, constants.JacketEnum.discount);
    }
}

class Cap extends ClothingPolicy {
    constructor() {
        super(constants.CapEnum.price, constants.CapEnum.discount);
    }
}

class Notebook extends StationaryPolicy {
    constructor() {
        super(constants.NotebookEnum.price, constants.NotebookEnum.discount);
    }
}

class Pens extends StationaryPolicy {
    constructor() {
        super(constants.PensEnum.price, constants.PensEnum.discount);
    }
}

class Markers extends StationaryPolicy {
    constructor() {
        super(constants.MarkersEnum.price, constants.MarkersEnum.discount);
    }
}

module.exports.TShirt = TShirt
module.exports.Cap = Cap
module.exports.Jacket = Jacket

module.exports.Notebook = Notebook
module.exports.Pens = Pens
module.exports.Markers = Markers