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

    connented(p, q) {
        this.find(p) == this.find(q);
    }
}

/**
 * 加权并查集
 */
class WeightedQuickUnionUF {
    constructor(n) {
        this.count = n;
        this.parent = [];
        this.parent.length = n;
        this.size = [];
        this.size.length = n;
        for (let i = 0; i < n; i++) {
            this.parent[i] = i;
            this.size[i] = 1;
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
        if (this.size[rootP] < this.size[rootQ]) {
            this.parent[rootP] = rootQ;
            this.size[rootQ] += this.size[rootP];
        } else {
            this.parent[rootQ] = rootP;
            this.size[rootP] += this.size[rootQ];
        }
        this.count--;
    }

    connented(p, q) {
        this.find(p) == this.find(q);
    }
}

/**
 * @param {number[][]} M
 * @return {number}
 */
var findCircleNum = function (M) {
    let uf = new WeightedQuickUnionUF(M.length)
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