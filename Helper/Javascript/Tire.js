/**
 * 前缀树
 */

class Tire {
    constructor() {
        this.nodes = {};
    }

    insert(word) {
        let node = this.nodes, cur;
        for (let i = 0; i < word.length; i++) {
            cur = word[i];
            if (!node[cur]) {
                node[cur] = {};
            }
            node = node[cur];
        }
        node.isWord = true;
    }

    search(word) {
        let node = this.nodes, cur;
        for (let i = 0; i < word.length; i++) {
            cur = word[i];
            if (!node[cur]) {
                return false;
            }
            node = node[cur];
        }
        return node.isWord == true;
    }

    startsWith(prefix) {
        let node = this.nodes, cur;
        for (let i = 0; i < prefix.length; i++) {
            cur = prefix[i];
            if (!node[cur]) {
                return false;
            }
            node = node[cur];
        }
        return true;
    }
}

let tire = new Tire();

// tire.insert("app");
// tire.insert("apple");
// tire.insert("add");
// console.log(tire.search("app"));
// console.log(tire.search("apps"));
// let func = ["Trie", "insert", "insert", "insert", "insert", "insert", "insert", "search", "search", "search", "search", "search", "search", "search", "search", "search", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith"]
// let arg = [[], ["app"], ["apple"], ["beer"], ["add"], ["jam"], ["rental"], ["apps"], ["app"], ["ad"], ["applepie"], ["rest"], ["jan"], ["rent"], ["beer"], ["jam"], ["apps"], ["app"], ["ad"], ["applepie"], ["rest"], ["jan"], ["rent"], ["beer"], ["jam"]]

// let tire = new Tire();
// for (let i = 1; i < func.length; i++) {
//     console.log(tire[func[i]](arg[i][0]));
// }
