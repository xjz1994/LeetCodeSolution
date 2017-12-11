/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function (letters, target) {
    for (let i in letters) {
        if (letters[i] > target) {
            return letters[i];
        }
    }
    return letters[0];
};

// let letters = ["c", "f", "j"];
// let target = "c";
let letters = ["a", "b"];
let target = "z";
console.log(nextGreatestLetter(letters, target));