/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var anagramMappings = function (A, B) {
    let res = [];
    res.length = A.length;
    let m = {};
    for (let i = 0; i < B.length; i++) {
        m[B[i]] = i;
    }
    for (let i in A) {
        res[i] = m[A[i]];
    }
    return res;
};

let A = [12, 28, 46, 32, 50];
let B = [50, 12, 32, 46, 28];
let res = anagramMappings(A, B);
console.log(res);