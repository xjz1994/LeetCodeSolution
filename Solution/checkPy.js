const fs = require('fs');

let read = (dir) => {
    return new Promise((resolve, reject) => {
        fs.readdir(dir, (err, files) => {
            if (err) reject(err);
            resolve(files);
        })
    })
}

//46. Permutations
//统计没有用python解的题目
let main = async () => {
    let cpp = await read('./Solution/Cpp');
    let cs = await read('./Solution/CSharp');
    let js = await read('./Solution/Javascript');
    let py = await read('./Solution/Python');

    let solved = cpp.concat(cs).concat(js);
    let solvedSet = new Set();
    for (let i in solved) {
        let curTitle = solved[i];
        let id = curTitle.match(/\d+/)[0];
        solvedSet.add(id);
    }

    let pySet = new Set();
    for (let i in py) {
        let curTitle = py[i];
        let id = curTitle.match(/\d+/)[0];
        pySet.add(id);
    }

    let res = []
    for (let i of solvedSet.keys()) {
        if (!pySet.has(i)) {
            res.push(parseInt(i));
        }
    }

    res = res.sort((a, b) => { return a - b });

    let str = "";
    for (let i in res) {
        str && (str += ",");
        str += res[i];
    }

    console.log(str);
    console.log("\ntotal:" + res.length);
}

main();