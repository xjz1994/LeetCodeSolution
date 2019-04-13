/**
 * @param {number[]} A
 * @param {number} K
 * @return {number[]}
 */
var addToArrayForm = function (A, K) {
    let res = [];
    let arrK = K.toString().split("").map(e => Number(e));
    let isCarry = false;
    let idxK = arrK.length - 1;
    let idxA = A.length - 1;
    while (idxK >= 0 || idxA >= 0 || isCarry == true) {
        let numA = A[idxA] || 0;
        let numK = arrK[idxK] || 0;
        let curBit = numA + numK;
        if (isCarry) {
            curBit += 1;
            isCarry = false;
        }
        if (curBit >= 10) {
            curBit = curBit % 10;
            isCarry = true;
        }
        res.unshift(curBit);
        idxA--;
        idxK--;
    }
    return res;
};


let A = [1, 2, 9, 9];
let K = 34;

// A = [1, 2, 6, 3, 0, 7, 1, 7, 1, 9, 7, 5, 6, 6, 4, 4, 0, 0, 6, 3]
// K = 516

// A = [1]
// K = 516

A = [2, 1, 5]
K = 806

let res = addToArrayForm(A, K);
console.log(res);