/**
 * @param {number[]} bits
 * @return {boolean}
 */

var isOneBitCharacter = function(bits) {
    let str = bits.join("").replace(/(1.)/g,"#");
    return str[str.length-1] == 0;
};

let bit = [1,0,0]
let arr = [1, 1, 1, 0];
let res = isOneBitCharacter(arr);
console.log(res);