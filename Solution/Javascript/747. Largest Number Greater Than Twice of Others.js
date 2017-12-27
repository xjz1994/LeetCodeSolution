/**
 * @param {number[]} nums
 * @return {number}
 */
var dominantIndex = function (nums) {
    let max = -1;
    let largestIndex = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > max) {
            max = nums[i];
            largestIndex = i;
        }
    }

    for (let i = 0; i < nums.length; i++) {
        if (i != largestIndex && nums[i] * 2 > max) {
            return -1;
        }
    }
    return largestIndex;
};

let nums = [3, 6, 1, 0];
let res = dominantIndex(nums);
console.log(res);