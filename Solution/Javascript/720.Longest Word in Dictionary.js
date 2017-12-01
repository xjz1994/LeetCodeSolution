/**
 * @param {string[]} words
 * @return {string}
 */
var longestWord = function (words) {
    let res = "";
    words = words.sort();
    let set = new Set();
    for (let i in words) {
        let s = words[i];
        if (s.length == 1 || set.has(s.substring(0, s.length - 1))) {
            res = s.length > res.length ? s : res;
            set.add(s);
        }
    }
    return res;
};

//let words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
let words = ["m", "mo", "moc", "moch", "mocha", "l", "la", "lat", "latt", "latte", "c", "ca", "cat"];
let res = longestWord(words);
console.log(res);