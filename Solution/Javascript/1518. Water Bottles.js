/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function (numBottles, numExchange) {
    let bottle = numBottles;
    let res = numBottles;
    while (bottle >= numExchange) {
        bottle -= numExchange;
        res++;
        bottle++;
    }
    return res;
};