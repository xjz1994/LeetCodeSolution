/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function (words, chars) {
    let res = 0;
    let map = {};
    for (let i in chars) {
        let c = chars[i];
        map[c] = map[c] == undefined ? 1 : ++map[c];
    }
    for (let i = 0; i < words.length; i++) {
        let word = words[i];
        let usedMap = {};
        let matchCount = 0;
        for (let i in word) {
            let c = word[i];
            usedMap[c] = usedMap[c] == undefined ? 0 : usedMap[c];
            if (map[c] != undefined && usedMap[c] < map[c]) {
                matchCount++;
                usedMap[c]++;
            }
        }
        if (matchCount == word.length) {
            res += matchCount
        }
    }
    return res;
};


let words = ["hello", "world", "leetcode"]
let chars = "welldonehoneyr"
let res = countCharacters(words, chars)
console.log(res)