/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var minimumDeleteSum = function (s1, s2) {
    let lenA = s1.length;
    let lenB = s2.length;
    let dp = createMatrix(lenB + 1, lenA + 1);

    for (let i = 1; i <= lenA; i++) {
        dp[i][0] = dp[i - 1][0] + s1[i - 1].charCodeAt();
    }

    for (let i = 1; i <= lenB; i++) {
        dp[0][i] = dp[0][i - 1] + s2[i - 1].charCodeAt();
    }

    for (let i = 1; i <= lenA; i++) {
        for (let j = 1; j <= lenB; j++) {
            let last = dp[i - 1][j - 1];
            let s1LastCode = s1[i - 1].charCodeAt();
            let s2LastCode = s2[j - 1].charCodeAt();
            if (s1[i - 1] != s2[j - 1]) {
                last += s1LastCode + s2LastCode;
            }
            dp[i][j] = Math.min(last, dp[i - 1][j] + s1LastCode, dp[i][j - 1] + s2LastCode);
        }
    }
    printMatrix(dp);
    return dp[lenA][lenB];
};

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

let printMatrix = (matrix) => {
    let str = "";
    for (let i in matrix) {
        for (let j in matrix[i]) {
            str += matrix[i][j] + ","
        }
        str += "\n";
    }
    console.log(str);
}

let a = "abcde";
let b = "abcd";
console.log(minimumDeleteSum(a, b));