/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function (nums) {
    //     let countMap = {};
    //     for (let i = 0; i < nums.length; i++) {
    //         let cur = nums[i];
    //         if (countMap[cur]) {
    //             countMap[cur]++;
    //         } else {
    //             countMap[cur] = 1;
    //         }
    //     }

    //     let sum = 0
    //     for (let i in countMap) {
    //         let cur = countMap[i];
    //         countMap[i] = sum;
    //         sum += cur;
    //     }

    //     let res = [];
    //     for (let i = 0; i < nums.length; i++) {
    //         res[i] = countMap[nums[i].toString()];
    //     }
    //     return res;

    let arr = [];
    let brr = [].concat(nums);
    nums.sort((a, b) => a - b);
    brr.map(item => {
        arr.push(nums.indexOf(item));
    })
    return arr;
};

let nums = [8, 1, 2, 2, 3];
let res = smallerNumbersThanCurrent(nums);
console.log(res);