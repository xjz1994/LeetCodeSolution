// /**
//  * Initialize your data structure here.
//  */
// var MagicDictionary = function () {
//     this.nodes = {};
// };

// /**
//  * Build a dictionary through a list of words 
//  * @param {string[]} dict
//  * @return {void}
//  */
// MagicDictionary.prototype.buildDict = function (dict) {
//     for (var i in dict) {
//         this.insert(dict[i]);
//     }
// };

// MagicDictionary.prototype.insert = function (word) {
//     let node = this.nodes, cur;
//     for (let i = 0; i < word.length; i++) {
//         cur = word[i];
//         if (!node[cur]) {
//             node[cur] = {};
//         }
//         node = node[cur];
//     }
//     node.isWord = true;
// };

// /**
//  * Returns if there is any word in the trie that equals to the given word after modifying exactly one character 
//  * @param {string} word
//  * @return {boolean}
//  */
// MagicDictionary.prototype.search = function (word) {
//     for (let i = 0; i < word.length; i++) {
//         for (let code = 65; code < 91; code++) {
//             let c = String.fromCharCode(code).toLowerCase();
//             if (word[i] == c) continue;
//             let str = word.slice(0, i) + c + word.slice(i + 1, word.length);
//             if (this.helper(str)) return true;
//         }
//     }
//     return false;
// };

// MagicDictionary.prototype.helper = function (word) {
//     let node = this.nodes, cur;
//     for (let i = 0; i < word.length; i++) {
//         cur = word[i];
//         if (!node[cur]) {
//             return false;
//         }
//         node = node[cur];
//     }
//     return node.isWord == true;
// }


/**
 * Initialize your data structure here.
 */
var MagicDictionary = function () {
    this.words = new Set();
};

/**
 * Build a dictionary through a list of words 
 * @param {string[]} dict
 * @return {void}
 */
MagicDictionary.prototype.buildDict = function (dict) {
    for (var i in dict) {
        this.words.add(dict[i]);
    }
};

/**
 * Returns if there is any word in the trie that equals to the given word after modifying exactly one character 
 * @param {string} word
 * @return {boolean}
 */
MagicDictionary.prototype.search = function (word) {
    for (let i = 0; i < word.length; i++) {
        for (let code = 65; code < 91; code++) {
            let c = String.fromCharCode(code).toLowerCase();
            if (word[i] == c) continue;
            let str = word.slice(0, i) + c + word.slice(i + 1, word.length);
            if (this.words.has(str)) return true;
        }
    }
    return false;
};


let func = ["MagicDictionary", "buildDict", "search", "search", "search", "search"];
let arg = [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]];
let dict = new MagicDictionary();
for (var i = 1; i < func.length; i++) {
    console.log(dict[func[i]](arg[i][0]));
}

/** 
 * Your MagicDictionary object will be instantiated and called as such:
 * var obj = Object.create(MagicDictionary).createNew()
 * obj.buildDict(dict)
 * var param_2 = obj.search(word)
 */