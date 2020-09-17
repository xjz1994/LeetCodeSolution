/**
 * @param {string} s
 * @return {number}
 */
var calculate = function (s) {
    let x = 1;
    let y = 0;

    let A = () => {
        x = 2 * x + y;
    }
    let B = () => {
        y = 2 * y + x;
    }

    for (let i in s) {
        if (s[i] === "A") {
            A();
        }
        if (s[i] === "B") {
            B();
        }
    }

    return x + y;
};

let s = "ABAB";
let res = calculate(s);
console.log(res);