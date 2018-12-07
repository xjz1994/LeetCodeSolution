/**
 * @param {number[][]} times
 * @param {number} N
 * @param {number} K
 * @return {number}
 */

var createMatrix = (times, N) => {
    let matrix = new Array();
    for (let i = 0; i < N; i++) {
        matrix[i] = new Array();
        for (let j = 0; j < N; j++) {
            matrix[i][j] = 0;
        }
    }
    for (let i in times) {

    }
    return matrix;
}

var networkDelayTime = function (times, N, K) {
    let matrix = createMatrix(times, N);

};

let times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]];
let N = 4;
let K = 2;
let res = networkDelayTime(times, N, K);