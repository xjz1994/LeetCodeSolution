/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function (n) {
    let str = n.toString();
    let product = 1;
    let sum = 0
    for (let i = 0; i < str.length; i++) {
        let curNum = Number(str[i]);
        sum = sum + curNum;
        product = product * curNum;
    }
    return product - sum;
};

let n = 4421;
let res = subtractProductAndSum(n);
console.log(res);