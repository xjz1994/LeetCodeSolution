/**
 * @param {number} n
 * @param {number} m
 * @param {number[][]} indices
 * @return {number}
 */
var oddCells = function (n, m, indices) {
    let row = new Array(n).fill(0);
    let col = new Array(m).fill(0);
    for (let i = 0; i < indices.length; i++) {
        let x = indices[i][0];
        let y = indices[i][1];
        row[x]++;
        col[y]++;
    }

    let sum = 0;
    for (let x = 0; x <= n; x++) {
        for (let y = 0; y <= m; y++) {
            if ((row[x] + col[y]) % 2 == 1) {
                sum++;
            }
        }
    }

    return sum;
};

n = 2, m = 3, indices = [[0, 1], [1, 1]]
res = oddCells(n, m, indices);
console.log(res)