/**
 * Initialize your data structure here.
 */
var MapSum = function() {
  this.map = new Map();
};

/** 
* @param {string} key 
* @param {number} val
* @return {void}
*/
MapSum.prototype.insert = function (key, val) {
  this.map.set(key, val);
};

/** 
* @param {string} prefix
* @return {number}
*/
MapSum.prototype.sum = function (prefix) {
  let times = 0;
  let map = this.map;
  for (let item of map) { 
    if (item[0].slice(0,prefix.length) == (prefix)) { 
      times += item[1];
    }
  }
  return times;
};

/** 
 * Your MapSum object will be instantiated and called as such:
 * var obj = Object.create(MapSum).createNew()
 * obj.insert(key,val)
 * var param_2 = obj.sum(prefix)
 */
