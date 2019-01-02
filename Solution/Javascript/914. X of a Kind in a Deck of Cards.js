/**
 * @param {number[]} deck
 * @return {boolean}
 */
var hasGroupsSizeX = function (deck) {
    if (deck.length <= 1) {
        return false;
    }

    let m = new Map();
    let maxCount = 0;
    for (let i = 0; i < deck.length; i++) {
        let cur = deck[i];
        let count = m.has(cur) ? m.get(cur) + 1 : 1;
        m.set(cur, count);
        maxCount = Math.max(maxCount, count);
    }

    let arr = Array.from(m.values());
    let result = arr.reduce((a, b) => {
        if (a < b) {
            [a, b] = [b, a];
        }
        while (b) {
            a = a % b;
            [a, b] = [b, a];
        }
        return a;
    });

    return result >= 2 ? true : false;
};

// let deck = [1, 2, 3, 4, 4, 3, 2, 1];
// let deck = [1, 1, 1, 2, 2, 2, 3, 3];
// let deck = [1];
// let deck = [1, 1];
// let deck = [1, 1, 2, 2, 2, 2];
let deck = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2];
let res = hasGroupsSizeX(deck)
console.log(res)