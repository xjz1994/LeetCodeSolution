/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function (nums) {
    let res = 0;
    for (let i = 0; i < nums.length; i++) {
        let curNum = nums[i];
        let num = Math.log10(curNum);
        if (Math.floor(num) % 2 != 0) {
            res++;
        }
    }
    return res;
};

let nums = [12, 345, 2, 6, 7896]
let res = findNumbers(nums)
console.log(res)