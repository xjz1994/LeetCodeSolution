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
        x.shift()
        if (x.length > 0) {
            heapify(x, 0, less_p)
        }
        return top
    }

    let topK = (x, k, less_p = MAX_HEAP) => {
        let res = [];
        buildHeap(x, less_p);
        let count = x.length;
        for (let i = 0; i < Math.min(k, count); i++) {
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

let nums = [5, 1, -1, -8, -7, 8, -5, 0, 1, 10, 8, 0, -4, 3, -1, -1, 4, -5, 4, -3, 0, 2, 2, 2, 4, -2, -4, 8, -7, -7, 2, -8, 0, -8, 10, 8, -8, -2, -9, 4, -7, 6, 6, -1, 4, 2, 8, -3, 5, -9, -3, 6, -8, -5, 5, 10, 2, -5, -1, -5, 1, -3, 7, 0, 8, -2, -3, -1, -5, 4, 7, -9, 0, 2, 10, 4, 4, -4, -1, -1, 6, -8, -9, -1, 9, -9, 3, 5, 1, 6, -1, -2, 4, 2, 4, -6, 4, 4, 5, -5];
let k = 7;
let res = topKFrequent(nums, k);
console.log(res);