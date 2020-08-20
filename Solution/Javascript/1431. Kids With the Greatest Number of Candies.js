/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function (candies, extraCandies) {
    let res = [];
    let max = 0;
    for (let i = 0; i < candies.length; i++) {
        max = Math.max(candies[i], max);
    }
    for (let i = 0; i < candies.length; i++) {
        if (candies[i] + extraCandies >= max) {
            res[i] = true;
        } else {
            res[i] = false;
        }
    }
    return res;
};