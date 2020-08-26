/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function (grid) {
    let res = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] < 0) {
                res++;
            }
        }
    }
    return res;
};

let grid = [[5, 1, 0], [-5, -5, -5]]
let res = countNegatives(grid)
console.log(res);