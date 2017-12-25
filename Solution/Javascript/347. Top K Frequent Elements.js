/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

let left = (i) => 2 * i + 1;
let right = (i) => 2 * (i + 1);

let buildHeap = (x, less_p) => {
    let n = x.length;
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        heapify(x, i, less_p)
    }
}

let heapify = (x, i, less_p) => {
    let n = x.length;
    while (true) {
        let l = left(i);
        let r = right(i);
        let smallest = i;
        if (l < n && less_p(x[l], x[i])) {
            smallest = l;
        }
        if (r < n && less_p(x[r], x[smallest])) {
            smallest = r;
        }
        if (smallest != i) {
            [x[i], x[smallest]] = [x[smallest], x[i]];
            i = smallest;
        } else {
            break;
        }
    }
}

let heapPop = (x, less_p) => {
    top = x[0]
    x[0] = x[x.length - 1];
    x.pop()
    if (x.length > 0) {
        heapify(x, 0, less_p)
    }
    return top
}

let topK = (x, k, less_p) => {
    let res = [];
    buildHeap(x, less_p);
    let count = x.length;
    for (let i = 0; i < Math.min(k, count); i++) {
        res.push(heapPop(x, less_p));
    }
    return res;
}

var topKFrequent = function (nums, k) {
    let MAX_HEAP = (a, b) => m[a] > m[b];

    let m = {};
    let heap = [];
    for (let i in nums) {
        let c = nums[i];
        !m[c] && heap.push(c);
        m[c] = m[c] ? ++m[c] : 1;
    }
    return topK(heap, k, MAX_HEAP);
};

let nums = [1, 2];
let k = 2;
let res = topKFrequent(nums, k);
console.log(res);