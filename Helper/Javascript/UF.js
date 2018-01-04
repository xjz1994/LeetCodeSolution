/**
 * 并查集
 */

// class UF {
//     constructor(n) {
//         this.count = n;
//         this.parent = [];
//         this.parent.length = n;
//         for (let i = 0; i < n; i++) {
//             this.parent[i] = i;
//         }
//     }

//     find(p) {
//         while (p != this.parent[p]) {
//             p = this.parent[p];
//         }
//         return p;
//     }

//     union(p, q) {
//         let rootP = this.find(p);
//         let rootQ = this.find(q);
//         if (rootP == rootQ) return;
//         this.parent[rootP] = rootQ;
//         this.count--;
//     }

//     connented(p, q) {
//         this.find(p) == this.find(q);
//     }
// }

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