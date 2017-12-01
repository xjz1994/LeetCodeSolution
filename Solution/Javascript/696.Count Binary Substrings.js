/**
 * @param {string} s
 * @return {number}
 */
var countBinarySubstrings = function (s) {
    let prevRunLength = 0;
    let curRunLength = 1;
    let res = 0;
    for (let i = 1; i < s.length; i++) {
        if (s[i] == s[i - 1]) {
            curRunLength++;
        } else {
            prevRunLength = curRunLength;
            curRunLength = 1;
        }
        if (prevRunLength >= curRunLength) res++;
    }
    return res;
};

//console.log(countBinarySubstrings("00110011"));