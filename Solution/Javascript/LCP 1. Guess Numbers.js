/**
 * @param {number[]} guess
 * @param {number[]} answer
 * @return {number}
 */
var game = function (guess, answer) {
    let res = 0;
    for (i = 0; i < guess.length; i++) {
        if (guess[i] == answer[i]) {
            res++
        }
    }
    return res;
};