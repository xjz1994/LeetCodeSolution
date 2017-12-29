/**
 * @param {number} n
 * @return {boolean}
 */
var hasAlternatingBits = function (n) {
    let str = n.toString(2);
    let bit = -1;
    let index = 0;
    while (index < str.length) {
        if (bit == -1) {
            bit = str[index++];
        } else {
            if (str[index++] == bit) {
                return false;
            } else {
                bit = !bit;
            }
        }
        return true;
    }
}
