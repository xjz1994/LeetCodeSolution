/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParityII = function (A) {
    let res = new Array(A.length);
    let evenIdx = 0;
    let oddIdx = 1;
    for (let i = 0; i < A.length; i++) {
        let cur = A[i];
        if (cur % 2 == 0) {
            res[evenIdx] = cur;
            evenIdx += 2;
        } else {
            res[oddIdx] = cur;
            oddIdx += 2;
        }
    }
    return res;
};


let array = [5, 2, 4, 7]
let res = sortArrayByParityII(array);
console.log(res);