/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortedSquares = function (A) {
    A.sort((a, b) => {
        return a * a - b * b;
    });
    let res = A.map((ele) => { return ele * ele });
    return res;
};