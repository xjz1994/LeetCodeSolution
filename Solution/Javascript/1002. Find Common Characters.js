/**
 * @param {string[]} A
 * @return {string[]}
 */
var commonChars = function (A) {
    let res = A[0].split("");
    for (let i = 1; i < A.length; i++) {
        let charArr = A[i].split("");
        res = res.filter((char) => {
            let idx = charArr.indexOf(char);
            if (idx !== -1) {
                charArr.splice(idx, 1);
                return true;
            }
            return false;
        });
    }
    return res;
};


let arr = ["bella", "label", "roller"];
// arr = ["cool", "lock", "cook"]
let res = commonChars(arr);
console.log(res);