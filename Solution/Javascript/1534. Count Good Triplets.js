/**
 * @param {number[]} arr
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var countGoodTriplets = function (arr, a, b, c) {
    const n = arr.length, sum = new Array(1001).fill(0);
    let ans = 0;
    for (let j = 0; j < n; ++j) {
        for (let k = j + 1; k < n; ++k) {
            if (Math.abs(arr[j] - arr[k]) <= b) {
                const lj = arr[j] - a, rj = arr[j] + a;
                const lk = arr[k] - c, rk = arr[k] + c;
                const l = Math.max(0, Math.max(lj, lk)), r = Math.min(1000, Math.min(rj, rk));
                if (l <= r) {
                    if (l === 0) {
                        ans += sum[r];
                    }
                    else {
                        ans += sum[r] - sum[l - 1];
                    }
                }
            }
        }
        for (let k = arr[j]; k <= 1000; ++k) {
            sum[k] += 1;
        }
    }
    return ans;
};