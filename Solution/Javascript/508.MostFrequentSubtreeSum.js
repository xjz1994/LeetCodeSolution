/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var findFrequentTreeSum = function (root) {
  let max = 0;
  let res = [];
  let m = {};

  let helper = (node) => {
    if (!node) return 0;
    let left = helper(node.left);
    let right = helper(node.right);
    let sum = left + right + node.val;
    if (m[sum]) {
      m[sum]++;
    } else {
      m[sum] = 1;
    }
    max = Math.max(m[sum], max);
    return sum;
  }

  helper(root);

  for (let i in m) {
    if (m[i] == max) {
      res.push(parseInt(i));
    }
  }
  return res;
};
