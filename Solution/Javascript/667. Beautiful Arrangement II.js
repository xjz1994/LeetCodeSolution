/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var constructArray = function (n, k) {
    let res = [];
    for (let i = 1, j = n; i <= j;) {
        if (k > 1) {
            res.push(k-- % 2 ? i++ : j--);
        } else {
            res.push(i++);
        }
    }
    return res;
};

let n = 3;
let k = 2;
let res = constructArray(n, k);
console.log(res);