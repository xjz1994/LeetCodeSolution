/**
 * @param {string} s
 * @return {string}
 */
var sortString = function (s) {
    var list = new Array(26).fill(0);
    var end = false;
    var res = '';

    for (var i = 0; i < s.length; i++) {
        let index = s.charCodeAt(i) - 97;
        list[index]++;
    }

    while (!end) {
        end = true;

        for (var i = 0; i < list.length; i++) {
            if (list[i]) {
                res += String.fromCharCode(i + 97);
                list[i]--;
            }
        }

        for (var i = list.length - 1; i > -1; i--) {
            if (list[i]) {
                res += String.fromCharCode(i + 97);
                list[i]--;
            }

            if (list[i] > 0) {
                end = false;
            }
        }
    }
    return res;
};

let s = "aaaabbbbcccc";
let res = sortString(s);
console.log(res);