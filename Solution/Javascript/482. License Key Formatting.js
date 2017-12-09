/**
 * @param {string} S
 * @param {number} K
 * @return {string}
 */
var licenseKeyFormatting = function (S, K) {
    let res = "";
    let str = S.replace(/-/g, "");
    let groupLength = 0;
    for (let i = str.length - 1; i >= 0; i--) {
        res = str[i].toUpperCase() + res;
        if (++groupLength == K && i != 0) {
            res = "-" + res;
            groupLength = 0;
        }
    }
    return res;
};


let s = "2-5g-3-J";
let k = 2;
let res = licenseKeyFormatting(s, k);
console.log(res);