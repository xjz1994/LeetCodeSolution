/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves2 = function(nums) {
    let newNums = nums.sort((a,b)=>{return a-b});
    let mid = nums[parseInt(newNums.length / 2)];
    let sum = 0;
    for(let i in newNums){
        sum += Math.abs(newNums[i] - mid);
    }
    return sum;
};
