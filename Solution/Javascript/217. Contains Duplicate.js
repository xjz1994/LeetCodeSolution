/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let m = {};
    for(let i = 0; i < nums.length; i++){
        let currentNum = nums[i];
        if(!m[currentNum]){
            m[currentNum] = true
        }else{
            return true;
        }
    }
    return false;
};