/**
 * @param {string[]} dict
 * @param {string} sentence
 * @return {string}
 */

class Trie {
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

    match(prefix) {
        let node = this.nodes, cur;
        let res = ""
        for (let i = 0; i < prefix.length; i++) {
            cur = prefix[i];
            if (!node[cur]) return null;
            res += cur;
            node = node[cur];
            if (node.isWord) {
                return res;
            }
        }
        return res;
    }
}

var replaceWords = function (dict, sentence) {
    let tire = new Trie();
    for (let i in dict) {
        tire.insert(dict[i]);
    }
    let scentenctArr = sentence.split(/\s/);
    for (let i in scentenctArr) {
        let res = tire.match(scentenctArr[i])
        if (res) {
            scentenctArr[i] = res;
        }
    }
    return scentenctArr.join(" ");
};

let dict = ["cat", "bat", "rat"];
let sentenct = "the cattle was rattled by the battery";
let res = replaceWords(dict, sentenct);
console.log(res);