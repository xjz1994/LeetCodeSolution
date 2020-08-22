/**
 * @param {number[]} coins
 * @return {number}
 */
var minCount = function(coins) {
    let res = 0;
    for(let i = 0; i < coins.length; i++){
        let current = Math.ceil(coins[i] / 2);
        res += current;
    }
    return res;
};