let editDistance = (strA, strB) => {
    let lenA = strA.length;
    let lenB = strB.length;
    let d = createMixture(lenB + 1, lenA + 1);

    for (let i = 0; i <= lenA; i++) {
        d[i][0] = i;
    }

    for (let i = 0; i <= lenB; i++) {
        d[0][i] = i;
    }

    for (let i = 1; i <= lenA; i++) {
        for (let j = 1; j <= lenB; j++) {
            if (a[i - 1] == b[j - 1]) {
                d[i][j] = d[i - 1][j - 1];
            } else {
                d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + 1);
            }
        }
    }

    return d[lenA][lenB];
}

let createMixture = (rowNum, colNum) => {
    let mixture = [];
    mixture.length = colNum;
    for (let i = 0; i < mixture.length; i++) {
        mixture[i] = [];
        mixture[i].length = rowNum;
        mixture[i].fill(0);
    }
    return mixture
}


let a = "abcde";
let b = "abcd";
console.log(editDistance(a, b));