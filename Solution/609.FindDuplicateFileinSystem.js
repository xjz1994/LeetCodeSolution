









/**
 * @param {string[]} paths
 * @return {string[][]}
 */
var findDuplicate = function(paths) {
    let m = {};
    for (let i in paths) {         
        let data = paths[i].split(" ");
        let path = data[0];
        for (let index = 1; index < data.length; index++) { 
            let file = data[index];
            let contentIndex = file.indexOf("(");
            let content = file.slice(contentIndex + 1, file.length - 1);
            let fileName = file.slice(0, contentIndex);
            if (m[content]) {
                m[content].push(path + "/" + fileName);
            } else { 
                m[content] = [path + "/" + fileName];
            }
        }     
    }
    let res = [];
    for (let i in m) {
        if (m[i].length > 1)
            res.push(m[i])
    }
    return res;
};
