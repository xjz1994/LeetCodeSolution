/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
    let res = [];

    let gen = (arr, remain) => {
        if (remain === 0) {
            res.push(arr);
            return
        }
        for (let i = 0; i < candidates.length; i++) {
            let cur = candidates[i];
            if (cur > remain) {
                break;
            }
            if (arr.length > 0 && cur < arr[arr.length - 1]) {
                continue;
            }
            gen(arr.concat([cur]), remain - cur);
        }
    };

    candidates.sort((a, b) => a - b);
    gen([], target);
    return res;
};

candidates = [2, 3, 6, 7];
target = 7;
combinationSum(candidates, target);