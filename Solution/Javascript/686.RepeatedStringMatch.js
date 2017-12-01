/**
 * @param {string} A
 * @param {string} B
 * @return {number}
 */
var repeatedStringMatch = function (A, B) {
    if (A.includes(B)) {
    }
    while (true) {
        let res = A.repeat(++time);
        if (res.includes(B)) {
            return time;
        }else if (res.length > B.length) {
            return -1;
        }
    }
};
