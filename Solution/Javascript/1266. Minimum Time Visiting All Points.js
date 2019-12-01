/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function (points) {
    let d = 0;
    for (let i = 0; i < points.length - 1; i++) {
        let dx = Math.abs(points[i + 1][0] - points[i][0]);
        let dy = Math.abs(points[i + 1][1] - points[i][1]);
        d += dx > dy ? dx : dy;
    }
    return d;
};

points = [[1, 1], [3, 4], [-1, 0]]
res = minTimeToVisitAllPoints(points)
console.log(res)