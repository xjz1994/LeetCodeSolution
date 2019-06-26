/**
 * @param {string} S
 * @return {string}
 */
var removeOuterParentheses = function (S) {
    let stack = [];
    let temp = "";
    let res = "";
    for (let i = 0; i < S.length; i++) {
        let c = S[i];
        if (c == "(") {
            stack.push(c);
        } else {
            stack.shift();
        }
        temp += c;
        if (stack.length == 0) {
            temp = temp.substr(1, temp.length - 1)
            temp = temp.substr(0, temp.length - 1)
            res += temp;
            temp = "";
        }
    }
    return res;
};

let S = "(()())(())(()(()))";
let res = removeOuterParentheses(S);
console.log(res);