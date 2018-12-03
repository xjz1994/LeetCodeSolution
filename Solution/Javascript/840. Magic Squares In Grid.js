/**
 * @param {number[][]} grid
 * @return {number}
 */
var numMagicSquaresInside = function (grid) {
    let totalMagicGrid = 0;
    let mainGridLength = grid.length;
    for (x = 0; x < mainGridLength - 2; x++) {
        let A = grid[x]; let aLength = A.length;
        let B = grid[x + 1]; let bLength = B.length;
        let C = grid[x + 2]; let cLength = C.length;

        for (i = 0; i < aLength - 2; i++) {
            if (
                15 == A[i] + A[i + 1] + A[i + 2] && //row1
                15 == B[i] + B[i + 1] + B[i + 2] && //row2
                15 == C[i] + C[i + 1] + C[i + 2] && //row3
                15 == A[i] + B[i + 1] + C[i + 2] && //dia1
                15 == C[i] + B[i + 1] + A[i + 2] && //dia2
                15 == A[i] + B[i] + C[i] && //col1
                15 == A[i + 1] + B[i + 1] + C[i + 1] && //col2
                15 == A[i + 2] + B[i + 2] + C[i + 2] //col3
            ) {
                let arr = [A[i], A[i + 1], A[i + 2], B[i], B[i + 1], B[i + 2], C[i], C[i + 1], C[i + 2]], aMap = {}, flag = false;
                for (let a of arr) {
                    if (aMap[a] || a < 1 || a > 10) { // check duplicate numbers, and invalid numbers
                        flag = true; continue;
                    }
                    aMap[a] = true;
                }
                if (flag) continue;
                totalMagicGrid++;
            }
        }

    }
    return totalMagicGrid;
};