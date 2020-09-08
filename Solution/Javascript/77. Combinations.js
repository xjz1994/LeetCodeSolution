/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {
    let res = [];
    let gen = (arr, index) => {
        if (arr.length === k) {
            res.push(arr);
            return;
        }
        for (let i = index; i <= n; i++) {
            if (arr.length + 1 > k) {
                break;
            }
            let newArr = arr.concat([i]);
            gen(newArr, i + 1);
        }
    };
    gen([], 1);
    return res;
};

let res = combine(4, 2);
console.log(res);