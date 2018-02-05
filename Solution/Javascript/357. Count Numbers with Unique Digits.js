/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function (n) {
    let res = 0;
    let gen = (s, n) => {
        if (n == 0) {
            res += 1;
        } else {
            for (let i in "0123456789") {
                if (i == '0' || !s.includes(i)) {
                    gen(s + i, n - 1)
                }
            }
        }
    }
    gen("", n)
    return res;
};

let res = countNumbersWithUniqueDigits(2)
console.log(res)