/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function (nums) {
    if (nums.length < 3) {
        return nums.length % 2 === 0 ? -1 : 1;
    }

    let sum = 0;
    nums.map((num) => { sum += num });

    let res = -1;
    let leftSum = 0;
    for (let i = 0; i < nums.length; i++) {
        sum -= nums[i];
        if (leftSum == sum) {
            res = i;
            break;
        }
        leftSum += nums[i];
    }
    return res;
};

//let arr = [1, 7, 3, 6, 5, 6];
//let arr = [100];
//let arr = [-1, -1, -1, 0, 1, 1];
let arr = [-1, -1, 0, 1, 1, 0];
console.log(pivotIndex(arr));