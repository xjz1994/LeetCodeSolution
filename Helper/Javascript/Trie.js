/**
 * 前缀树
 */

module.exports.Trie = class Trie {
    constructor() {
        this.nodes = {};
    }

    insert(word) {
        let node = this.nodes;
        for (let i = 0; i < word.length; i++) {
            let cur = word[i];
            if (!node[cur]) {
                node[cur] = {};
            }
            node = node[cur];
        }
        node.isWord = true;
    }

    search(word) {
        let node = this.nodes;
        for (let i = 0; i < word.length; i++) {
            let cur = word[i];
            if (!node[cur]) {
                return false;
            }
            node = node[cur];
        }
        return node.isWord == true;
    }

    startsWith(prefix) {
        let node = this.nodes;
        for (let i = 0; i < prefix.length; i++) {
            let cur = prefix[i];
            if (!node[cur]) {
                return false;
            }
            node = node[cur];
        }
        return true;
    }
}

//let trie = new Trie();

// trie.insert("app");
// trie.insert("apple");
// trie.insert("add");
// console.log(trie.search("app"));
// console.log(trie.search("apps"));
// let func = ["Trie", "insert", "insert", "insert", "insert", "insert", "insert", "search", "search", "search", "search", "search", "search", "search", "search", "search", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith"]
// let arg = [[], ["app"], ["apple"], ["beer"], ["add"], ["jam"], ["rental"], ["apps"], ["app"], ["ad"], ["applepie"], ["rest"], ["jan"], ["rent"], ["beer"], ["jam"], ["apps"], ["app"], ["ad"], ["applepie"], ["rest"], ["jan"], ["rent"], ["beer"], ["jam"]]

// let trie = new Trie();
// for (let i = 1; i < func.length; i++) {
//     console.log(trie[func[i]](arg[i][0]));
// }
