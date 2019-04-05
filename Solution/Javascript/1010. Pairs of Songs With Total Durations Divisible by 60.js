/**
 * @param {number[]} time
 * @return {number}
 */
var numPairsDivisibleBy60 = function (time) {
    let dp = new Array(60);
    dp.fill(0);

    let ans = 0;
    for (let i in time) {
        let t = time[i];
        t %= 60;
        ans += dp[t != 0 ? 60 - t : 0];
        dp[t]++;
    }

    return ans;
};


let time = [30, 20, 150, 100, 40];
let res = numPairsDivisibleBy60(time);
console.log(res);