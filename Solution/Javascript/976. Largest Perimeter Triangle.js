/**
 * @param {number[]} A
 * @return {number}
 */
var largestPerimeter = function (A) {
    if (A.length < 3) {
        return 0;
    }
    A = A.sort((a, b) => { return b - a });
    for (let i = 0; i < A.length - 2; i++) {
        let [a, b, c] = [A[i], A[i + 1], A[i + 2]];
        if (a + b > c && a + c > b && b + c > a) {
            return A[i] + A[i + 1] + A[i + 2];
        }
    }
    return 0;
};

// let A = [3, 2, 3, 4];
let A = [18, 2, 7, 15, 14, 1, 40, 147, 85, 16, 31];
let res = largestPerimeter(A);
console.log(res);