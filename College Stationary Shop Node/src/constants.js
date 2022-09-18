const Constants = {
    MAX_CLOTHING_ITEMS_QTY : 2,
    MAX_STATIONARY_ITEMS_QTY : 3,
    MIN_PURCHASE_AMOUNT : 1000,
    MIN_EXTRA_DISCOUNT_AMOUNT : 3000,
    EXTRA_DISCOUNT_PERCENTAGE : 0.05,
    WAVIER_TAX_PERCENTAGE : 0.1
}


const QuantityReturnEnum = {
    ITEM_ADDED : "ITEM_ADDED",
    ERROR_QUANTITY_EXCEEDED : "ERROR_QUANTITY_EXCEEDED"
}

const TShirtEnum = {
    price: 1000,
    discount: 0.10
}   

const JacketEnum = {
    price: 2000,
    discount: 0.05
}

const CapEnum = {
    price: 500,
    discount: 0.20
}

const NotebookEnum = {
    price: 200,
    discount: 0.20
}

const PensEnum = {
    price: 300,
     discount: 0.10
}    

const MarkersEnum = {
    price :500,
    discount: 0.05
}

module.exports.QuantityReturnEnum = QuantityReturnEnum;
module.exports.Constants = Constants;

module.exports.TShirtEnum = TShirtEnum;

module.exports.CapEnum = CapEnum;
module.exports.JacketEnum = JacketEnum;
module.exports.NotebookEnum = NotebookEnum;
module.exports.PensEnum = PensEnum;
module.exports.MarkersEnum = MarkersEnum;