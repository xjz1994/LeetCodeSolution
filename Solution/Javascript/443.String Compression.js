/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    if(!chars){
        return 0
    }
    if(chars.length <= 1){
        return chars.length;
    }
    let res = "";
    let count = chars.length - 1;
    let lastChar = chars[0];
    let repeat = 0;
    for(let i = 1; i <= count; i++){
        let curChar = chars[i];
        if(curChar == lastChar){
            repeat++;
        }
        if(curChar != lastChar || i == count){
            repeat <= 0 ? (res += lastChar) : (res += lastChar + String(repeat+1));
            repeat = 0;
            lastChar = curChar;
        }
    }
    if(chars[chars.length-1] != chars[chars.length-2]){
        res+=chars[chars.length-1];
    }
    res = res.split("");
    for(let i in res){
        chars[i] = res[i];
    }
    chars.length = res.length;
    return res.length;
};

//let arr = ["a","a","b","b","c","c","c"];
//let arr = ["a","b","b","b","b","b","b","b","b","b","b","b","b"];
// let arr = ["a","b","c","d","e"];
// let res = compress(arr);
// console.log(res);
// console.log(arr);