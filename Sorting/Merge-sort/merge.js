function mergeSort(arr, s, e) {
    if (e - s + 1 <= 1) {
        return arr
    }

    let m = (s + e) / 2

    mergeSort(arr, s, m)

    mergeSort(arr, m + 1, e)

    mergeSort(arr, s, m, e)

    return arr
}

function merge(arr, s, m, e) {
    const L = arr.slice(s, m + 1);
    const R = arr.slice(m + 1, e + 1);

    let i = 0;
    let j = 0;
    let k = s;

    while (i < L.length && j < R.length) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i ++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < L.length) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < R.length) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

const arr = [38, 27, 43, 3, 9, 82, 10];
merge(arr, 0, 2, 6);
console.log(arr);