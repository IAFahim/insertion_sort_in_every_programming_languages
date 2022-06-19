function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let key = arr[i];
        let j = i - 1;
        while (j >= 0 && key < arr[j]) {
            arr[j + 1] = arr[j]
            j--
        }
        arr[j + 1] = key;
    }
    return arr;
}

function insertionSortReverse(arr) {
    for (let i = 1; i < arr.length; i++) {
        let key = arr[i]
        let j = i - 1;
        while (j >= 0 && key > arr[j]) {
            arr[j + 1] = arr[j]
            j--
        }
        arr[j + 1] = key;
    }
    return arr;
}

let arr = [4, 2, 0, 6, 9]

let ascending = insertionSort(arr)
console.log(ascending)

let descending = insertionSortReverse(arr)
console.log(descending)