/**
 * @param {string} text
 * @param {string} first
 * @param {string} second
 * @return {string[]}
 */
var findOcurrences = function (text, first, second) {
    let res = [];
    let textArr = text.split(" ");
    for (let i = 0; i < textArr.length - 2; i++) {
        if (textArr[i] == first && textArr[i + 1] == second) {
            res.push(textArr[i + 2]);
        }
    }
    return res;
};

let text = "alice is a good girl she is a good student"
let first = "a"
let second = "good"
let res = findOcurrences(text, first, second)
console.log(res)