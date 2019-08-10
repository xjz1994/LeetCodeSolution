/**
* @param {number} candies
* @param {number} num_people
* @return {number[]}
*/
var distributeCandies = function (candies, num_people) {
    let res = [];
    res.length = num_people;
    res.fill(0);

    let i = 0;
    while (candies > i) {
        res[i % num_people] += i + 1;
        candies -= i + 1;
        i += 1;
    }
    res[i % num_people] += candies;
    return res;
};

let candies = 7;
let num_people = 4;
let res = distributeCandies(candies, num_people);
console.log(res);