/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function (address) {
    return address.replace(/\./g, "[.]")
};

let address = "255.100.50.0"
let res = defangIPaddr(address)
console.log(res)