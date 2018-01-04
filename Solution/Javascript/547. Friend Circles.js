class UF {
    constructor(n) {
        this.count = n;
        this.parent = [];
        this.parent.length = n;
        for (let i = 0; i < n; i++) {
            this.parent[i] = i;
        }
    }

    find(p) {
        while (p != this.parent[p]) {
            p = this.parent[p];
        }
        return p;
    }

    union(p, q) {
        let rootP = this.find(p);
        let rootQ = this.find(q);
        if (rootP == rootQ) return;
        this.parent[rootP] = rootQ;
        this.count--;
    }
}

/**
 * @param {number[][]} M
 * @return {number}
 */
var findCircleNum = function (M) {
    let uf = new UF(M.length)
    for (let i = 0; i < M.length; i++) {
        for (let j = 0; j < M[i].length; j++) {
            if (M[i][j] == 1) {
                uf.union(i, j);
            }
        }
    }
    return uf.count;
};


let m = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1]
];

let res = findCircleNum(m);
console.log(res); 