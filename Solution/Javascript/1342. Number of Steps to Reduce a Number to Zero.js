/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function (num) {
    let res = 0;
    while (num != 0) {
        if (num % 2 == 0) {
            num = num >> 1;
        } else {
            num--;
        }
        res++;
    }
    return res;
};

let num = 123
let res = numberOfSteps(num)
console.log(res)