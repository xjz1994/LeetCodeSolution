/**
 * @param {number} N
 * @return {number}
 */
var fib = function (N) {
    let a = 0, b = 1;
    let tmp = 0;
    for (let i = 0; i <= N; i += 1) {
        b = a + b;
        tmp = b;
        b = a;
        a = tmp;
    }
    return b;
};