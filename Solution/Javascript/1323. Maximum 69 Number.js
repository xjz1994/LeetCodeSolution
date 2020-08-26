/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number = function (num) {
    // let numStrArr = num.toString().split("");
    // for(let i = 0; i<numStrArr.length; i++){
    //     let char = numStrArr[i];
    //     if(char == "6"){
    //         numStrArr[i] = "9";
    //         break;
    //     }
    // }
    // let res = Number(numStrArr.join(""));
    // return res;
    return Number(num.toString().replace('6', '9'));
};