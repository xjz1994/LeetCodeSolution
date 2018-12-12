/**
 * @param {number[]} A
 * @return {boolean}
 */
var validMountainArray = function (A) {
    let maxIdx = 0;
    for (let i = 0; i < A.length; i++) {
        if (A[i] > A[maxIdx]) {
            maxIdx = i;
        }
    }
    if (maxIdx == 0 || maxIdx == A.length - 1) {
        return false
    }
    let left = maxIdx - 1;
    while (left >= 0) {
        if (A[left] >= A[left + 1]) {
            return false;
        }
        left--;
    }
    let right = maxIdx + 1;
    while (right <= A.length - 1) {
        if (A[right] >= A[right - 1]) {
            return false;
        }
        right++;
    }
    return true;
};

// let A = [1, 2, 3, 9, 5, 4, 2];
// let A = [5, 9, 1];
// let A = [2, 1];
// let A = [3, 5, 5];
let A = [0, 3, 2, 1];
let res = validMountainArray(A);
console.log(res);