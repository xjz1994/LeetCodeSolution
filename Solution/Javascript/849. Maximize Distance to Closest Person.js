/**
* @param {number[]} seats
* @return {number}
*/
var maxDistToClosest = function (seats) {
    let continueArr = [];
    let continueCount = 0;
    for (let i = 0; i < seats.length; i++) {
        if (seats[i] == 0) {
            continueCount++;
        }
        if ((seats[i] == 1 && continueCount > 0) || i == seats.length - 1) {
            continueArr.push(continueCount);
            continueCount = 0;
        }
    }

    let arr = continueArr.map((val) => Math.ceil(val / 2))

    let leftContinue = 0
    if (seats[0] == 0) {
        leftContinue = continueArr[0];
    }
    let rightContinue = 0
    if (seats[seats.length - 1] == 0) {
        rightContinue = continueArr[continueArr.length - 1];
    }

    return Math.max(leftContinue, rightContinue, Math.max.apply(null, arr));
}

// let seats = [1, 0, 0, 0, 1, 0, 1];
// let seats = [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0];
// let seats = [0, 1]
let seats = [0, 0, 1]
// let seats = [1, 0, 0, 0]
// let seats = [0, 1, 0, 1, 0]
let res = maxDistToClosest(seats);
console.log(res);
