/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function (heights) {
    let copy = heights.concat()
    let sort = heights.sort((a, b) => a - b)
    let count = 0
    for (let i = 0; i < sort.length; i++) {
        if (sort[i] != copy[i]) {
            count++;
        }
    }
    return count;
};
let heights = [1, 1, 4, 2, 1, 3]
let res = heightChecker(heights)
console.log(res);