module.exports.QSort = (arr) => {
    sort(arr, 0, arr.length - 1);
}

let sort = (arr, left, right) => {
    if (left < right) {
        let middle = arr[parseInt((left + right) / 2)];
        let i = left - 1;
        let j = right + 1;
        while (true) {
            while (arr[++i] < middle);
            while (arr[--j] > middle);
            if (i >= j) break;
            swap(arr, i, j);
        }
        sort(arr, left, i - 1);
        sort(arr, j + 1, right);
    }
}

let swap = (arr, i, j) => {
    let num = arr[i];
    arr[i] = arr[j];
    arr[j] = num;
}

// let arr = [3, 4, 2, 1, 8, 7, 9, 5, 5];
// QSort(arr);
// console.log(arr);