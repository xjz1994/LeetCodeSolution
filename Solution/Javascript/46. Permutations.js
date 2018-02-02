/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
    let res = [];
    let m = {};
    for (let i in nums) {
        m[i] = nums[i];
    }
    let gen = (list, added) => {
        if (list.length == nums.length) {
            res.push(list.concat());
        } else {
            for (let i in m) {
                let cur = m[i];
                if (!added.has(m[i])) {
                    list.push(m[i]);
                    added.add(m[i]);
                    gen(list, added);
                    list.pop();
                    added.delete(m[i]);
                }
            }
        }
    }
    gen([], new Set())
    return res
};

let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];
let start = new Date().getTime()
let res = permute(nums)
console.log(new Date().getTime() - start)