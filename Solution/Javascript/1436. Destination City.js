/**
 * @param {string[][]} paths
 * @return {string}
 */
var destCity = function (paths) {
    let res = "";
    let map = {};
    for (let i = 0; i < paths.length; i++) {
        map[paths[i][0]] = paths[i][1];
    }
    for (let key in map) {
        let val = map[key];
        // 去不到其他城市的地方即为终点
        if (!map[val]) {
            res = val;
            break;
        }
    }
    return res;
};