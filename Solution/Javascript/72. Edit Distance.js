/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = (word1, word2) => {
    let lenA = word1.length;
    let lenB = word2.length;
    let d = createMatrix(lenB + 1, lenA + 1);

    for (let i = 0; i <= lenA; i++) {
        d[i][0] = i;
    }

    for (let i = 0; i <= lenB; i++) {
        d[0][i] = i;
    }

    for (let i = 1; i <= lenA; i++) {
        for (let j = 1; j <= lenB; j++) {
            if (word1[i - 1] == word2[j - 1]) {
                d[i][j] = d[i - 1][j - 1];
            } else {
                d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + 1);
            }
        }
    }

    return d[lenA][lenB];
}

let createMatrix = (rowNum, colNum) => {
    let matrix = [];
    matrix.length = colNum;
    for (let i = 0; i < matrix.length; i++) {
        matrix[i] = [];
        matrix[i].length = rowNum;
        matrix[i].fill(0);
    }
    return matrix
}

let a = "abcde";
let b = "abcd";
console.log(editDistance(a, b));