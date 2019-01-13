/**
 * @param {number[][]} points
 * @param {number} K
 * @return {number[][]}
 */
var kClosest = function (points, K) {
    points.sort((a, b) => {
        return (a[0] * a[0] + a[1] * a[1]) - (b[0] * b[0] + b[1] * b[1]);
    });
    return points.slice(0, K);
};

// let points = [[3, 3], [5, -1], [-2, 4]];
// let K = 2;

let points = [[-95, 76], [17, 7], [-55, -58], [53, 20], [-69, -8], [-57, 87], [-2, -42], [-10, -87], [-36, -57], [97, -39], [97, 49]]
let K = 5

let res = kClosest(points, K);
console.log(res);