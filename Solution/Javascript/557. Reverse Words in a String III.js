/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
    let arr = s.split(" ");
    for (let i = 0; i < arr.length; i++) {
        arr[i] = arr[i].split("").reverse().join("");
    }
    let res = arr.join(" ");
    return res;
};

let input = "Let's take LeetCode contest";
let res = reverseWords(input);
console.log(res);