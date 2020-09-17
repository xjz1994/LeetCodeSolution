/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function (arr) {
    let res = -1;
    let map = {};
    for (let i = 0; i < arr.length; i++) {
        let cur = arr[i];
        if (map[cur]) {
            map[cur]++;
        } else {
            map[cur] = 1;
        }
    }

    for (let k in map) {
        if (parseInt(k) === map[k]) {
            res = Math.max(k);
        }
    }

    return res;
};

let arr = [1, 2, 2, 3, 3, 3];
let res = findLucky(arr);
console.log(res);