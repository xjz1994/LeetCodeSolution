/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function (arr) {
    let needCount = 3;
    let odds = [];
    for (let i = 0; i < arr.length; i++) {
        let cur = arr[i];
        if (cur % 2 !== 0) {
            odds.push(cur);
        } else {
            odds = [];
        }
        if (odds.length === needCount) {
            return true;
        }
    }
    return false;
};