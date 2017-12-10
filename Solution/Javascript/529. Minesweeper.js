/**
 * @param {character[][]} board
 * @param {number[]} click
 * @return {character[][]}
 */
var updateBoard = function (board, click) {
    if (board[click[0], click[1]] == "M") {
        board[click[0], click[1]] = "X";
    }
    let queue = [{ row: click[0], col: click[1] }];
    while (queue.length > 0) {
        let p = queue.shift();
        let mineNum = getMineNum(board, p.row, p.col);
    }
    return board;
};

var getMineNum = function (board, row, col) {
    let num = 0;
    let pos = []
}

let board =
    [['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'M', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E']];

let click = [3, 0];

let res = updateBoard(board, click);
