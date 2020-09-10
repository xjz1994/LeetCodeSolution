/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {
    let res = [];
    let gen = (arr, index) => {
        if (arr.length === k) {
            res.push(arr);
            return;
        }
        for (let i = index; i <= n; i++) {
            let newArr = arr.concat([i]);
            gen(newArr, i + 1);
        }
    };
    gen([], 1);
    return res;
};

/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {
    const ans = [];
    const dfs = (cur, temp) => {
        if (temp.length + (n - cur + 1) < k) {
            return;
        }
        if (temp.length == k) {
            ans.push(temp.concat());
            return;
        }
        temp.push(cur)
        dfs(cur + 1, temp);
        temp.pop()
        dfs(cur + 1, temp);
    }
    dfs(1, []);
    return ans;
};

let res = combine(4, 2);
console.log(res);