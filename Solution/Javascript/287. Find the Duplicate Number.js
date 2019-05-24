/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function (nums) {
    let slow = nums[0], fast = nums[nums[0]];

    while (slow !== fast) {
        slow = nums[slow];
        fast = nums[nums[fast]];
        console.log(slow, fast)
    }
    fast = 0;

    while (slow !== fast) {
        slow = nums[slow];
        fast = nums[fast];
    }
    return slow;
};


let nums = [1, 4, 3, 5, 2, 2]
let res = findDuplicate(nums);
console.log(res);