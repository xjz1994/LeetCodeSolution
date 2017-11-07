/**
 * @param {string[]} words
 * @return {string}
 */
var longestWord = function (words) {
    let res = "";
    words = words.sort();
    for (let i in words) {
        let s = words[i];
        if (s.length >= res.length && s.indexOf(res) == 0) {
            res = s;
        }
    }
    return res;
};

//let words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
let words = ["m", "mo", "moc", "moch", "mocha", "l", "la", "lat", "latt", "latte", "c", "ca", "cat"];
let res = longestWord(words);
console.log(res);