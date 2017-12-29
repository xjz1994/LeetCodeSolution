// /**
//  * @param {number} x
//  * @param {number} n
//  * @return {number}
//  */
// var myPow = function (x, n) {
//     return Math.pow(x, n);
// };

/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function (x, n) {
    if (n < 0) {
        x = 1 / x
        n = -n
    }
    pow = 1
    while (n) {
        if (n & 1) {
            pow *= x
        }
        x *= x
        n = n >> 1;
    }
    return pow;
};

let x = 2.00000;
let n = 10;
let res = myPow(x, n);
console.log(res);