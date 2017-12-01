let max = 0;
var longestUnivaluePath = function(root) { 
  max = 0;
  helper(root, null);
  return max;
};

var helper = (node,parentVal) => { 
  if (!node) return 0;
  let left = helper(node.left, node.val);
  let right = helper(node.right, node.val);
  max = Math.max(left + right, max);
  if (node.val == parentVal) {
    return Math.max(left, right) + 1;
  } else { 
    return 0;
  }
}
