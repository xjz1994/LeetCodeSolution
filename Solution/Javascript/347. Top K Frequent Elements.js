/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    let MIN_HEAP = (a, b) => m[a] < m[b];
    let MAX_HEAP = (a, b) => m[a] > m[b];
    let left = (i) => 2 * i + 1;
    let right = (i) => 2 * (i + 1);

    let buildHeap = (x, less_p = MAX_HEAP) => {
        let n = x.length;
        for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
            heapify(x, i, less_p)
        }
    }

    let heapify = (x, i, less_p = MAX_HEAP) => {
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

    let heapPop = (x, less_p = MAX_HEAP) => {
        top = x[0]
        x.pop()
        if (x.length > 0) {
            heapify(x, 0, less_p)
        }
        return top
    }

    let topK = (x, k, less_p = MAX_HEAP) => {
        let res = [];
        buildHeap(x);
        for (let i = 0; i <= Math.min(k, x.length - 1); i++) {
            res.push(heapPop(x, less_p));
        }
        return res;
    }

    let m = {};
    let heap = [];
    for (let i in nums) {
        let c = nums[i];
        !m[c] && heap.push(c);
        m[c] = m[c] ? ++m[c] : 1;
    }
    return topK(heap, k);
};

let nums = [1, 2, 3, 2, 2, 3];
//let nums = [4, 1, 1, 2, 1, 2, 3];
let k = 2;
let res = topKFrequent(nums, k);
console.log(res);