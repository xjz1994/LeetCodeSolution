/**
* @param {number[]} seats
* @return {number}
*/
var maxDistToClosest = function (seats) {
    let maxCoutinuteCount = 0;
    let lastSeatIdx = -1
    for (let i = 0; i < seats.length; i++) {
        if (lastSeatIdx == -1 && seats[i] == 0) {
            lastSeatIdx = i;
        } else if (lastSeatIdx != -1 && seats[i] == 1) {
            maxCoutinuteCount = Math.max(i - lastSeatIdx, maxCoutinuteCount);
            lastSeatIdx = i;
        }
    }

    let lastContinuteCount = 0
    if (seats[seats.length - 1] == 0) {
        lastContinuteCount = (seats.length - 1) - lastSeatIdx;
    }

    return Math.max(Math.ceil(maxCoutinuteCount / 2), lastContinuteCount);
}

// let seats = [1, 0, 0, 0, 1, 0, 1];
// let seats = [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0];
// let seats = [0, 1]
let seats = [0, 0, 1]
let res = maxDistToClosest(seats);
console.log(res);
