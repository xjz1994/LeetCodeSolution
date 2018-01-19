let less = (i, j) => {
    return i < j
}

let swap = (arr, i, j) => {
    [arr[i], arr[j]] = [arr[j], arr[i]];
}

let printArr = (arr) => {
    let str = "";
    for (let i in arr) {
        str += arr[i] + ",";
    }
    console.log(str);
}

//插入排序
let InsertSort = (a) => {
    let N = a.length;
    for (let i = 1; i < N; i++) {
        for (let j = i; j > 0 && less(a[j], a[j - 1]); j--) {
            swap(a, j, j - 1);
            printArr(a);
        }
    }
}

//希尔排序
let ShellSort = (a) => {
    let N = a.length;
    let h = 1;
    while (h < N / 3) { h = 3 * h + 1 };
    while (h >= 1) {
        for (let i = h; i < N; i++) {
            for (let j = i; j >= h && less(a[j], a[j - h]); j -= h) {
                swap(a, j, j - h);
                printArr(a);
            }
        }
        h = parseInt(h / 3);
    }
}

//快速排序
let QuickSort = (arr) => {
    let sort = (arr, left, right) => {
        if (left < right) {
            let temp = arr[left];
            let i = left - 1;
            let j = right + 1;
            while (true) {
                while (arr[++i] < temp);
                while (arr[--j] > temp);
                if (i >= j) break;
                swap(arr, i, j);
            }
            sort(arr, left, i - 1);
            sort(arr, j + 1, right);
        }
    }
    sort(arr, 0, arr.length - 1);
}

let arr = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8];
//QuickSort(arr);
//InsertSort(arr);
ShellSort(arr);
console.log(arr);