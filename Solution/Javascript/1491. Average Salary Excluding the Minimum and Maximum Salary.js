/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function (salary) {
    salary.sort((a, b) => a - b);
    salary.shift();
    salary.pop();
    return salary.reduce((accumulator, val) => accumulator + val) / salary.length;
};