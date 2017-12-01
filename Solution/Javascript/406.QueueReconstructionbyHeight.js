/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function (people) {
    var sorter = function (a, b) {
        if (a[0] != b[0]) {
            return b[0] - a[0]
        } else {
            return a[1] - b[1]
        }
    }
    people.sort(sorter);
    var res = [];
    for (let i = 0; i < people.length; i++) {
        res.splice(people[i][1], 0, people[i]);
    }
    return res;
};

