/**
 * @param {string} S
 * @return {string}
 */
var removeDuplicates = function (S) {
    let stack = [];
    for (let i = 0; i < S.length; i++) {
        let char = S[i];
        stack.push(char);
        if (stack.length >= 2 && stack[stack.length - 2] == stack[stack.length - 1]) {
            stack.pop();
            stack.pop();
        }
    }
    return stack.join("");
};

let S = "abbaca";
let res = removeDuplicates(S);
console.log(res);