/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function (arr) {
    let map = {};
    let numberCount = 0;

    for (let i = 0; i < arr.length; i++) {
        let curNum = arr[i];
        if (map[curNum]) {
            map[curNum]++;
        } else {
            map[curNum] = 1;
            numberCount++;
        }
    }

    let set = new Set()
    for (let i in map) {
        set.add(map[i])
    }

    return numberCount == set.size
};


// let arr = [1, 2, 2, 1, 1, 3]
let arr = [3, 5, -2, -3, -6, -6]
let res = uniqueOccurrences(arr)
console.log(res);