/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function (arr1, arr2) {
    let idxMap = {};
    let notInArr2Idx = {};

    for (let i = 0; i < arr2.length; i++) {
        idxMap[arr2[i]] = i;
    }

    arr1.sort((a, b) => { return a - b });
    for (let i = 0; i < arr1.length; i++) {
        if (idxMap[arr1[i]] === undefined) {
            notInArr2Idx[arr1[i]] = arr1.length + i;
        }
    }

    arr1.sort((a, b) => {
        let aIdx = idxMap[a] === undefined ? notInArr2Idx[a] : idxMap[a];
        let bIdx = idxMap[b] === undefined ? notInArr2Idx[b] : idxMap[b];
        return aIdx - bIdx;
    });

    return arr1;
};

// let arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19];
// let arr2 = [2, 1, 4, 3, 9, 6];
let arr1 = [28, 6, 22, 8, 44, 17]
let arr2 = [22, 28, 8, 6]
let res = relativeSortArray(arr1, arr2);
console.log(res);