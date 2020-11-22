/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function (nums) {
    var left, right;
    var tmp = "->";
    var arr = [];
    left = nums[0];
    right = nums[0];
    if (nums.length === 1) {
        arr.push(nums[0] + "")
        return arr
    }
    for (let i = 1; i <= nums.length; i++) {
        if (nums[i] - nums[i - 1] === 1) {
            right = nums[i]
        }
        else if (left === right) {
            arr.push(left + "")
            left = nums[i]
            right = nums[i]
        }
        else {
            arr.push(left + tmp + right)
            left = nums[i]
            right = nums[i]
        }
    }
    return arr
};