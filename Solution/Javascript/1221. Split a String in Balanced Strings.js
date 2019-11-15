/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function (s) {
    let res = 0
    let cur = 0
    for (let i = 0; i < s.length; i++) {
        let curChar = s[i];
        if (curChar == "R") {
            cur++;
        } else if (curChar == "L") {
            cur--;
        }

        if (cur == 0) {
            res++;
        }
    }
    return res;
};