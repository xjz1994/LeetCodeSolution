/**
 * @param {number} L
 * @param {number} R
 * @return {number}
 */
var countPrimeSetBits = function (L, R) {
    let primes = new Set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]);
    let res = 0;
    while (L <= R) {
        let str = L.toString(2);
        let match = str.match(/1/g);
        if (match && primes.has(match.length)) {
            res++;
        }
        L++;
    }
    return res;
};
let res = countPrimeSetBits(10, 15);
console.log(res);