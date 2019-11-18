/**
 * // This is the CustomFunction's API interface.
 * // You should not implement it, or speculate about its implementation
 * function CustomFunction() {
 *
 *     @param {integer, integer} x, y
 *     @return {integer}
 *     this.f = function(x, y) {
 *         ...
 *     };
 *
 * };
 */
/**
 * @param {CustomFunction} customfunction
 * @param {integer} z
 * @return {integer[][]}
 */
var findSolution = function (customfunction, z) {
    var r = new Array();
    var my = 1000;
    for (let x = 1; x <= 1000; x++) {
        for (let y = my; y >= 1; y--) {
            let fz = customfunction.f(x, y);
            if (fz > z) {
                my = y - 1;
                continue;
            } else if (fz == z) {
                r.push([x, y]);
                my = y - 1;
                break;
            } else if (fz < z) {
                my = y;
                break;
            }
        }
    }
    return r;
};

