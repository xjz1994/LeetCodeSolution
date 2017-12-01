

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    let m = {}
    for (var i in nums) { 
        let num = nums[i];
        if (m[num]) {
            m[num]++;
        } else { 
            m[num] = 1;
        }
    }
    let res = [];
    for (var i in m) { 
        if (res.length == 2) { 
            break;
        }
        let num = m[i]
        if (num == 1) { 
            res.push(parseInt(i));
        }
    }
    return res
};
