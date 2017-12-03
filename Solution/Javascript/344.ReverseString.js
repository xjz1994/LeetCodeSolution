/**
 * @param {string} s
 * @return {string}
 */
var reverseString = function (s) {
    let left = 0, right = s.length - 1;
    let sArr = s.split("");
    while (left < right) {
        let c = sArr[left];
        sArr[left++] = sArr[right];
        sArr[right--] = c;
    }
    return sArr.join("");
};

let s = "hello";
console.log(reverseString(s));