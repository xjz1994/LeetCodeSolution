/**
 * @param {string} S
 * @param {string} T
 * @return {boolean}
 */
var backspaceCompare = function (S, T) {
    let getResultString = (str) => {
        let stack = [];
        for (let i = 0; i < str.length; i++) {
            let char = str[i]
            if (char == "#") {
                stack.pop();
            } else {
                stack.push(char);
            }
        }
        return stack.join("");
    }
    let newS = getResultString(S);
    let newT = getResultString(T);
    return newS === newT;
};

S = "ab#c";
T = "ad#c"
let res = backspaceCompare(S, T);
console.log(res);