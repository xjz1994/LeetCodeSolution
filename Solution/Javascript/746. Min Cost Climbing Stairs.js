/**
 * @param {number[]} cost
 * @return {number}
 */
// var minCostClimbingStairs = function (cost) {
//     var a = 0, b = 0, min = 0;
//     for (let c in cost) {
//         b = a;
//         a = cost[c] + min;
//         min = Math.min(a, b);
//     }
//     return min;
// };

var minCostClimbingStairs = function (cost) {
    let dp = [];
    dp.length = cost.length;
    dp.fill(0);
    dp[0] = cost[0];
    dp[1] = cost[1];
    for (let i = 2; i < cost.length; i++) {
        dp[i] = cost[i] + Math.min(dp[i - 1], dp[i - 2]);
    }
    return Math.min(dp[cost.length - 1], dp[cost.length - 2]);
};

//let cost = [10, 15, 20];
let cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1];
console.log(minCostClimbingStairs(cost));