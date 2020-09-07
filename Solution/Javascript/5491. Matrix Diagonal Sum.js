/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function (mat) {
    let res = 0;
    let left = 0;
    let right = mat[0].length - 1;
    for (let i = 0; i < mat.length; i++) {
        if (left != right) {
            res += mat[i][left];
            res += mat[i][right];
        } else {
            res += mat[i][left];
        }
        left++;
        right--;
    }
    return res;
};