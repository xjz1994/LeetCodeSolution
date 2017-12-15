/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayNesting = function (nums) {
    let res = 0, set = new Set();           //因为集合S会成环，因此可以用set存储遍历过的index
    for (let i = 0; i < nums.length; i++) {
        let curIndex = i, count = 0;
        while (!set.has(curIndex)) {
            set.add(curIndex);
            curIndex = nums[curIndex];
            count++;
        }
        res = Math.max(res, count);
    }
    return res;
};

//let arr = [5, 4, 0, 3, 1, 6, 2];
let arr = [1, 2, 3, 4, 5, 0]
console.log(arrayNesting(arr));