/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var luckyNumbers = function (matrix) {
    let minInRow = [];
    let maxInCol = [];
    for (let i = 0; i < matrix.length; i++) {
        let min = Math.min(...matrix[i]);
        minInRow[i] = min;
    }

    for (let i = 0; i < matrix[0].length; i++) {
        let max = 0;
        for (let j = 0; j < matrix.length; j++) {
            max = Math.max(max, matrix[j][i]);
        }
        maxInCol[i] = max;
    }
    let res = minInRow.filter(e => maxInCol.includes(e))
    return res;
};


let matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
let res = luckyNumbers(matrix)