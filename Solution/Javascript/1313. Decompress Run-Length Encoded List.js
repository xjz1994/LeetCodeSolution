/**
 * @param {number[]} nums
 * @return {number[]}
 */
var decompressRLElist = function (nums) {
    let res = [];
    for (let i = 0; i < nums.length; i += 2) {
        let count = nums[i];
        let number = nums[i + 1];
        while (count > 0) {
            res.push(number);
            count--;
        }
    }
    return res;
};