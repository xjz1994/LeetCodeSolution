/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    let map = {};
    for (let i in nums) {
        let curNum = nums[i];
        if (map[curNum]) {
            map[curNum]++;
        } else {
            map[curNum] = 1;
        }
    }
    console.log(map);
};

let nums = [1, 1, 1, 2, 2, 3];
let k = 2;
let res = topKFrequent(nums, k);
