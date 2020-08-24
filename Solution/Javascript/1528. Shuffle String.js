/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function (s, indices) {
    let strArr = [];
    for (let i = 0; i < indices.length; i++) {
        strArr[indices[i]] = s[i];
    }
    let res = strArr.join("");
    return res;
};