// import {Builder} from "./src/product_builder.js"
const product_builder = require("./src/product_builder.js")
const fs = require("fs")

const filename = process.argv[2]

fs.readFile(filename, "utf8", (err, data) => {
    if (err) throw err
    var inputLines = data.toString().split("\n")
    builder = new product_builder.Builder();

    for(let i = 0; i < inputLines.length; i++) {
        inputLines[i] = inputLines[i].replace("\r", '');
        line = inputLines[i].split(' ');
        if(line[0] == "ADD_ITEM") {
            builder.add_item(line[1], parseFloat(line[2]));
        } else {
            builder.print_bill();
        }
    }
})
