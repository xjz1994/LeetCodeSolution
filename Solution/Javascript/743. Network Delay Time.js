// /**
//  * @param {number[][]} times
//  * @param {number} N
//  * @param {number} K
//  * @return {number}
//  */

// var createMatrix = (times, N) => {
//     let matrix = new Array();
//     for (let i = 0; i < N; i++) {
//         matrix[i] = new Array();
//         for (let j = 0; j < N; j++) {
//             matrix[i][j] = 0;
//         }
//     }
//     for (let i in times) {
//         let info = times[i];
//         let srcIdx = info[0];
//         let tarIdx = info[1];
//         let dis = info[2];
//         matrix[srcIdx - 1][tarIdx - 1] = dis;
//         // matrix[b - 1][a - 1] = dis;
//     }
//     return matrix;
// }

// var networkDelayTime = function (times, N, K) {
//     let matrix = createMatrix(times, N);

//     let maxTime = -1;
//     let m = {};
//     m[K] = 0;
//     let queue = [K];
//     while (queue.length > 0) {
//         let srcIdx = queue.shift() - 1;
//         let srcNode = srcIdx + 1;
//         let canMovePaths = matrix[srcIdx];
//         for (let i = 0; i < canMovePaths.length; i++) {
//             let time = canMovePaths[i];
//             let targetNode = i + 1;
//             if (time > 0 && m[targetNode] === undefined) {
//                 let newTime = time + (m[srcNode] || 0);
//                 m[targetNode] = newTime;
//                 maxTime = Math.max(maxTime, newTime);
//                 queue.push(targetNode);
//             }
//         }
//     }
//     return maxTime;
// };

function Node(name) {
    this.name = name;
    this.next = [];
    this.visited = false;
    this.time = Infinity;
}

function popSmallestTime(list) {
    let min = Infinity;

    const minIndex = list.reduce((acc, e, i) => {
        if (e.time < min) {
            min = e.time;
            return i;
        }
        return acc
    }, 0);

    return list.splice(minIndex, 1)[0];
}

function createGraph(numNodes, edges) {
    const nodes = {};

    for (var i = 1; i <= numNodes; i++) {
        nodes[i] = new Node(i);
    }

    edges.forEach(([u, v, w]) => {
        nodes[u].next.push([nodes[v], w]);
    });

    return nodes;
}

var networkDelayTime = function (times, N, K) {
    const processList = []
    const visitedList = [];

    const nodes = createGraph(N, times);
    const unvisited = Object.values(nodes);

    let minTime = 0;

    nodes[K].time = 0;
    nodes[K].visited = true;

    processList.push(nodes[K]);

    while (processList.length) {
        const node = popSmallestTime(processList);
        minTime = node.time;

        node.next.forEach(([next, weight]) => {
            if ((node.time + weight) < next.time) {
                next.time = node.time + weight;
            }
            if (!next.visited) {
                processList.push(next);
                next.visited = true;
            }
        });

        visitedList.push(node);
    }

    return visitedList.length !== N ? -1 : minTime;
};

// let times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]];
// let N = 4;
// let K = 2;

// let times = [[1, 2, 1]];
// let N = 2;
// let K = 2;

let times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
let N = 3
let K = 1

let res = networkDelayTime(times, N, K);
console.log(res);