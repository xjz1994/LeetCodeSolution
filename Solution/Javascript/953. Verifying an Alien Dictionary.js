/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function (words, order) {
    let alphabet = {};
    for (let i = 0; i < order.length; i++) {
        alphabet[order[i]] = i;
    }

    let invalid = function (a, b) {
        let minLength = Math.min(a.length, b.length);
        for (var i = 0; i < minLength; i++) {
            if (alphabet[a[i]] !== alphabet[b[i]]) {
                return alphabet[a[i]] > alphabet[b[i]];
            }
        }
        return a.length > b.length;
    };

    for (var i = 1; i < words.length; i++) {
        if (invalid(words[i - 1], words[i])) {
            return false;
        }
    }

    return true;
};

let words = ["hello", "leetcode"];
let order = "hlabcdefgijkmnopqrstuvwxyz";

words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"

words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"

// words = ["kuvp", "q"]
// order = "ngxlkthsjuoqcpavbfdermiywz"

words = ["iekm", "tpnhnbe"]
order = "loxbzapnmstkhijfcuqdewyvrg"

let res = isAlienSorted(words, order);
console.log(res);