/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function (nums) {
    let res = 0;
    let map = {};
    for (let i = 0; i < nums.length; i++) {
        let currentNum = nums[i];
        if (map[currentNum]) {
            map[currentNum].push(i);
            res += map[currentNum].length - 1;
        } else {
            map[currentNum] = [i];
        }
    }
    return res;
};

nums = [1, 2, 3, 1, 1, 3]
res = numIdenticalPairs(nums)
console.log(res)