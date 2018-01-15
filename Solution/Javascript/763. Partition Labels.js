/**
 * @param {string} S
 * @return {number[]}
 */
var partitionLabels = function (S) {
    let posDict = {};
    for (let i = 0; i < S.length; i++) {
        let char = S[i];
        if (posDict[char]) {
            posDict[char].end = i;
        } else {
            posDict[char] = { start: i, end: i };
        }
    }
    let res = [];
    let min = max = 0;
    for (let i in posDict) {
        let start = posDict[i].start;
        let end = posDict[i].end;
        if (start > max) {
            res.push(max - min + 1);
            [min, max] = [start, end];
        } else {
            max = Math.max(max, end);
        }
    }
    res.push(max - min + 1);
    return res;
};


let S = "ababcbacadefegdehijhklij";
let res = partitionLabels(S);
console.log(res);