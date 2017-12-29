/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function (nums) {
    let res = [];
    res.length = nums.length;
    res.fill(-1);

    let stack = [];
    let index = 0;
    while (index < nums.length * 2) {
        let cur = nums[index % nums.length];
        while (stack.length > 0 && nums[stack[stack.length - 1]] < cur) {
            res[stack.pop()] = cur;
        }
        if (index < nums.length) stack.push(index);
        index++
    }
    return res;
};

//let nums = [2, 1, 1, 3];
let nums = [1, 2, 1];
let res = nextGreaterElements(nums);
console.log(res);