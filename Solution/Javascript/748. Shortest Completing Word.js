/**
 * @param {string} licensePlate
 * @param {string[]} words
 * @return {string}
 */
var shortestCompletingWord = function (licensePlate, words) {
    let m = {};
    for (let i = 0; i < licensePlate.length; i++) {
        let c = licensePlate[i].toLowerCase();
        if (!isNaN(c)) continue;
        m[c] = m[c] ? ++m[c] : 1;
    }
    let res = "";
    for (let i in words) {
        let str = words[i];
        if (isMatch(m, str) && (str.length < res.length || res == "")) {
            res = str;
        }
    }
    return res;
};

var isMatch = (m, s) => {
    let newM = {};
    for (let i = 0; i < s.length; i++) {
        let c = s[i].toLowerCase();
        if (!isNaN(c)) continue;
        newM[c] = newM[c] ? ++newM[c] : 1;
    }
    for (let i in m) {
        if (!newM[i] || m[i] > newM[i]) {
            return false;
        }
    }
    return true;
}

let licensePlate = "GrC8950";
let words = ["measure", "other", "every", "base", "according", "level", "meeting", "none", "marriage", "rest"];
console.log(shortestCompletingWord(licensePlate, words));