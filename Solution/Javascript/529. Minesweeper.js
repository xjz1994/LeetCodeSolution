/**
 * @param {character[][]} board
 * @param {number[]} click
 * @return {character[][]}
 */
var updateBoard = function (board, click) {
    if (board[click[0]][click[1]] == "M") {         //click mine
        board[click[0]][click[1]] = "X";
        return board;
    }

    let pos = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]];

    let queue = [{ row: click[0], col: click[1] }];
    while (queue.length > 0) {
        let p = queue.shift();
        let mineNum = 0;
        for (var i in pos) {
            let r = p.row + pos[i][0], c = p.col + pos[i][1];
            if (r >= 0 && r < board.length && c >= 0 && c < board[0].length) {
                if (board[r][c] == "M") mineNum++;
            }
        }
        if (mineNum > 0) {
            board[p.row][p.col] = mineNum.toString();
            continue;
        }
        for (var i in pos) {
            let r = p.row + pos[i][0], c = p.col + pos[i][1];
            if (r >= 0 && r < board.length && c >= 0 && c < board[0].length) {
                if (board[r][c] == "E") {
                    board[r][c] = "B";
                    queue.push({ row: r, col: c });
                }
            }
        }
    }
    return board;
};

let board = [
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'M', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E']
];

let click = [3, 0];
let res = updateBoard(board, click);