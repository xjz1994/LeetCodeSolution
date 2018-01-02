/**
 * @param {number[][]} M
 * @return {number}
 */

var findCircleNum = function (M) {
    let res = 0;
    let copy = [];
    for (let i in M) {
        copy[i] = M[i].slice();
    }
    for (let i = 0; i < copy.length; i++) {
        for (let j = 0; j < copy[i].length; j++) {
            if (copy[i][j] == 1) {
                res++;
                DFS(i, j, copy);
            }
        }
    }
    return res;
};

var DFS = (row, col, arr) => {
    // let pos = [[-1, 0], [0, -1], [0, 0], [0, 1], [1, 0]];
    // for (let i in pos) {
    //     let r = row + pos[i][0], c = row + pos[i][1];
    //     if (r >= 0 && r < arr.length && c >= 0 && c < arr[0].length) {
    //         if (arr[r][c] == 1) {
    //             arr[r][c] = 0;
    //             DFS(r, c, arr);
    //         }
    //     }
    // }
}

let m = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1]
];

let res = findCircleNum(m);
console.log(res); 