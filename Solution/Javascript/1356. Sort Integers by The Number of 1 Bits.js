/**
 * @param {number[]} arr
 * @return {number[]}
 */
// var sortByBits = function (arr) {
//     arr.sort((a, b) => {
//         let aArr = a.toString(2).match(/1/g);
//         let bArr = b.toString(2).match(/1/g);
//         let aNum = aArr ? aArr.length : 0;
//         let bNum = bArr ? bArr.length : 0;
//         if (aNum !== bNum) {
//             return aNum - bNum;
//         } else {
//             return a - b;
//         }
//     });
//     return arr
// };


var sortByBits = function (arr) {
    let hammingWeight = (n) => {
        let sum = 0;
        while (n > 0) {
            if (n & 1 == 1) {
                sum++;
            }
            n = n >>> 1;
        }
        return sum;
    }
    arr.sort((a, b) => {
        let aNum = hammingWeight(a)
        let bNum = hammingWeight(b);
        if (aNum !== bNum) {
            return aNum - bNum;
        } else {
            return a - b;
        }
    });
    return arr
};

arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
res = sortByBits(arr)
console.log(res)