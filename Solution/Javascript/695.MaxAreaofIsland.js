var maxAreaOfIsland = function (grid) {
    let max = 0;
    let posSet = new Set();
    for (let r = 0; r < grid.length; r++) {
        let row = grid[r];
        for (let c = 0; c < row.length; c++) {
            if (row[c] === 0 || posSet.has(getPosStr(r, c))) continue;
            let block = 0;
            let queue = [{ r, c }];
            posSet.add(getPosStr(r, c));
            while (queue.length > 0) {
                block++;
                let pos = queue.shift();
                let posRow = pos.r;
                let posCol = pos.c;
                if (posRow >= 1 && grid[posRow - 1][posCol] == 1 && !posSet.has(getPosStr(posRow - 1, posCol))) {
                    queue.push({ r: posRow - 1, c: posCol });
                    posSet.add(getPosStr(posRow - 1, posCol));
                }
                if (posRow < grid.length - 1 && grid[posRow + 1][posCol] == 1 && !posSet.has(getPosStr(posRow + 1, posCol))) {
                    queue.push({ r: posRow + 1, c: posCol });
                    posSet.add(getPosStr(posRow + 1, posCol));
                }
                if (posCol >= 1 && grid[posRow][posCol - 1] == 1 && !posSet.has(getPosStr(posRow, posCol - 1))) {
                    queue.push({ r: posRow, c: posCol - 1 });
                    posSet.add(getPosStr(posRow, posCol - 1));
                }
                if (posCol < row.length - 1 && grid[posRow][posCol + 1] == 1 && !posSet.has(getPosStr(posRow, posCol + 1))) {
                    queue.push({ r: posRow, c: posCol + 1 });
                    posSet.add(getPosStr(posRow, posCol + 1));
                }
            }
            max = Math.max(max, block);
        }
    }
    return max;
};

let getPosStr = (x, y) => {
    return x + "," + y;
}
