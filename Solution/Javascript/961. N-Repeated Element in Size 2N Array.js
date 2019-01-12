/**
 * @param {number[]} A
 * @return {number}
 */
var repeatedNTimes = function (A) {
    let m = {};
    for (let i = 0; i < A.length; i++) {
        let num = A[i];
        m[num] = m[num] ? m[num] + 1 : 1;
        if (m[num] > 1) {
            return num;
        }
    }
    return null;
};

// let A = [2, 1, 2, 5, 3, 2];
let A = [1, 2, 3, 3]
let res = repeatedNTimes(A);
console.log(res)