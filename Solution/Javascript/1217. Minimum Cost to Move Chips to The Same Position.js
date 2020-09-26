/**
 * @param {number[]} position
 * @return {number}
 */
var minCostToMoveChips = function (chips) {
    let oddNums = 0, evenNums = 0;
    for (let i = 0; i < chips.length; i++) {
        if (chips[i] % 2 === 0) {
            oddNums++;
        } else {
            evenNums++;
        }
    }
    return Math.min(oddNums, evenNums)
};