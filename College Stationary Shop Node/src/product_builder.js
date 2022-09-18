const constants = require('./constants.js')
const products_pack = require('./products.js')


class Builder {
    constructor() {
        this.__products = {
            "TSHIRT" : products_pack.TShirt,
            "JACKET" : products_pack.Jacket,
            "CAP" : products_pack.Cap,
            "NOTEBOOK" : products_pack.Notebook,
            "PENS": products_pack.Pens,
            "MARKERS" : products_pack.Markers
        }
        this._product_list = [];
    }

    get_product(product, product_name) {
        product = new this.__products[product_name]();
    }

    set_quantity(product, qty) {
        return product.set_quantity(qty);
    }

    add_item(product_name, qty) {
        let product = null;
        this.get_product(product, product_name)
        console.log(product)
        if(this.set_quantity(product, qty)) {
            this._product_list.push(product);
            console.log(constants.QuantityReturnEnum.ITEM_ADDED);
        } else {
            console.log(constants.QuantityReturnEnum.ERROR_QUANTITY_EXCEEDED)
        }
    }
    
    get_subtotal() {
        total = 0;
        this._product_list.forEach(product => {
            total += product.get_total_cost();
        });

        return total;
    }

    get_discount_value() {
        total = 0.0;
        this._product_list.forEach(product => {
            total += product.get_discount_price();
        });

        return total;
    }

    deduct_tax(total_amount) {
        return total_amount * constants.Constants.WAVIER_TAX_PERCENTAGE;
    }

    print_bill() {
        total_discount = 0.0;
        total_amount = this.get_subtotal()

        if(total_amount >= constants.Constants.MIN_PURCHASE_AMOUNT) {
            total_discount = this.get_discount_value()
            total_amount -= total_discount
        }

        if(total_amount >= constants.Constants.MIN_EXTRA_DISCOUNT_AMOUNT) {
            extra_discount = total_amount * constants.Constants.EXTRA_DISCOUNT_PERCENTAGE;
            total_discount += extra_discount;
            total_amount -= extra_discount
        }

        console.log("TOTAL_DISCOUNT", total_discount);
        console.log("TOTAL_AMOUNT_TO_PAY", this.deduct_tax(total_amount));
    }
}

module.exports.Builder = Builder;