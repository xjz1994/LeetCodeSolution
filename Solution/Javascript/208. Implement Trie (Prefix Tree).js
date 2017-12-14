var Trie = function () {
    this.nodes = {};
};

Trie.prototype.insert = function (word) {
    let node = this.nodes, cur;
    for (let i = 0; i < word.length; i++) {
        cur = word[i];
        if (!node[cur]) {
            node[cur] = {};
        }
        node = node[cur];
    }
    node.isWord = true;
};

Trie.prototype.search = function (word) {
    let node = this.nodes, cur;
    for (let i = 0; i < word.length; i++) {
        cur = word[i];
        if (!node[cur]) {
            return false;
        }
        node = node[cur];
    }
    return node.isWord == true;
};

Trie.prototype.startsWith = function (prefix) {
    let node = this.nodes, cur;
    for (let i = 0; i < prefix.length; i++) {
        cur = prefix[i];
        if (!node[cur]) {
            return false;
        }
        node = node[cur];
    }
    return true;
};


// let func = ["Trie", "insert", "insert", "insert", "insert", "insert", "insert", "search", "search", "search", "search", "search", "search", "search", "search", "search", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith"]
// let arg = [[], ["app"], ["apple"], ["beer"], ["add"], ["jam"], ["rental"], ["apps"], ["app"], ["ad"], ["applepie"], ["rest"], ["jan"], ["rent"], ["beer"], ["jam"], ["apps"], ["app"], ["ad"], ["applepie"], ["rest"], ["jan"], ["rent"], ["beer"], ["jam"]]

// let tire = new Tire();
// for (let i = 1; i < func.length; i++) {
//     console.log(tire[func[i]](arg[i][0]));
// }