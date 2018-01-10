let InsertSort = (arr) => {
    for (let i = 1; i < arr.length; i++) {
        let temp = arr[i];
        for (let j = i - 1; j >= 0; j--) {
            if (arr[j] > temp) {
                arr[j + 1] = arr[j];
                arr[j] = temp;
            } else {
                break;
            }
        }
    }
}

let ShellSort = (array) => {
    var length = array.length,
        gap = Math.floor(length / 2);
    while (gap > 0) {
        for (var i = gap; i < length; i++) {
            for (var j = i; 0 < j; j -= gap) {
                if (array[j - gap] > array[j]) {
                    swap(array, j - gap, j);
                } else {
                    break;
                }
            }
        }
        gap = Math.floor(gap / 2);
    }
}

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

let swap = (arr, i, j) => {
    let num = arr[i];
    arr[i] = arr[j];
    arr[j] = num;
}

let arr = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8];
//QuickSort(arr);
//InsertSort(arr);
ShellSort(arr);
console.log(arr);