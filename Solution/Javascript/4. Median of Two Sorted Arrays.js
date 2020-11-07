/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
    let nums = nums1.concat(nums2).sort((a, b) => { return a - b });
    if (nums.length == 0) {
        return 0
    } else if (nums.length % 2 == 0) {
        return (nums[nums.length / 2 - 1] + nums[nums.length / 2]) / 2;
    } else if (nums.length % 2 != 0) {
        return nums[Math.ceil(nums.length / 2 - 1)];
    }
};

let nums1 = [1, 3]
let nums2 = [2]
let res = findMedianSortedArrays(nums1, nums2);
console.log(res);
