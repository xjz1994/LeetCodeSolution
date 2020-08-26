/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
    nums.sort((a, b) => { return b - a });
    return (nums[0] - 1) * (nums[1] - 1);
};

let nums = [3, 4, 5, 2];
let res = maxProduct(nums);