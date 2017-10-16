/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function (s) {
    let m = {};
    for (let i in s) {
        let c = s[i];
        if (m[c]) {
            m[c]++;
        } else {
            m[c] = 1;
        }
    }
    let arr = [];
    for (let i in m) {
        let d = {};
        d.str = i;
        d.time = m[i];
        arr.push(d);
    }
    arr.sort((a, b) => {
        return b.time - a.time;
    });

    let res = "";
    for (let i in arr) {
        let item = arr[i];
        res += item.str.repeat(item.time);
    }
    return res;
};

// let s = "Aabb";
// console.log(frequencySort(s));