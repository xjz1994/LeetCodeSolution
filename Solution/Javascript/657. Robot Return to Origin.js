/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function (moves) {
    let x = y = 0;
    for (let i = 0; i < moves.length; i++) {
        let char = moves[i];
        if (char === "U") {
            y += 1;
        } else if (char === "D") {
            y -= 1;
        } else if (char === "L") {
            x -= 1;
        } else if (char === "R") {
            x += 1;
        }
    }
    let res = (x === 0 && y === 0);
    return res;
};

let moves = "UD";
let res = judgeCircle(moves);