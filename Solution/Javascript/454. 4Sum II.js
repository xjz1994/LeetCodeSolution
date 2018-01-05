/**
 * @param {number[]} A
 * @param {number[]} B
 * @param {number[]} C
 * @param {number[]} D
 * @return {number}
 */
var fourSumCount = function (A, B, C, D) {
    let res = 0;
    let m = {};
    for (let i in A) {
        for (let j in B) {
            let value = A[i] + B[j];
            m[value] = m[value] ? ++m[value] : 1;
        }
    }
    for (let i in C) {
        for (let j in D) {
            let negativeValue = -1 * (C[i] + D[j]);
            if (m[negativeValue]) {
                res += m[negativeValue];
            }
        }
    }
    return res;
};

let A = [1, 2];
let B = [-2, -1];
let C = [-1, 2];
let D = [0, 2];
let res = fourSumCount(A, B, C, D);
console.log(res);