/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function (n) {
    let res = [];
    let symmetryCount = 0;
    let addZero = false;
    if (n % 2 == 0) {
        symmetryCount = n / 2;
    } else {
        symmetryCount = (n - 1) / 2;
        addZero = true;
    }
    for (let i = 1; i <= symmetryCount; i++) {
        res.push(i);
        res.push(-i);
    }
    if (addZero) {
        res.push(0);
    }
    return res;
};