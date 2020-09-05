/**
 * @param {number[]} nums
 * @return {number[]}
 */
let minSubsequence = (nums) => {
    nums.sort((a, b) => b - a)
    let sum = nums.reduce((a, b) => a + b)
    let temp = 0
    let res = []
    for (let i = 0; i < nums.length; i++) {
        res.push(nums[i])
        temp += nums[i]
        if (temp > sum >> 1) return res
    }
};