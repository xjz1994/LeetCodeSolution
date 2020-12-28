/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
    let map = {};
    for (let i = 0; i < s.length; i++) {
        let cur = s[i];
        if (map[cur]) {
            map[cur]++;
        } else {
            map[cur] = 1;
        }
    }

    for (let i = 0; i < s.length; i++) {
        let cur = s[i];
        if (map[cur] == 1) {
            return i;
        }
    }

    return -1;
};

let s = "loveleetcode"