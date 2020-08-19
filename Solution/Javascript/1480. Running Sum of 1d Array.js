/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function (nums) {
    let res = [0];
    for (let i = 0; i < nums.length; i++) {
        res[i + 1] = nums[i] + res[i];
    }
    res.shift();
    return res;
};