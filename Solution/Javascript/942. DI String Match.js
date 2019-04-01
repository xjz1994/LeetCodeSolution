/**
 * @param {string} S
 * @return {number[]}
 */
var diStringMatch = function (S) {
    let l = S.length;
    let s = 0;
    let result = [];
    for (let i = 0; i <= S.length; i++) {
        if (S[i] === 'I') {
            result.push(s++);
        } else {
            result.push(l--);
        }
    }
    return result;
};


let S = "IDID";
let res = diStringMatch(S);
console.log(res);