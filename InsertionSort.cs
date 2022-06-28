using System;
class InsertionSort {
    static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.Length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && key < arr[j]) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    static void insertionSortReverse(int[] arr) {
        for (int i = 1; i < arr.Length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && key > arr[j]) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    static void Main() {
        int[] arr = new int[] {4, 2, 0, 6, 9};

        insertionSort(arr);
        foreach(int j in arr) {
            Console.Write(j + " ");
        }

        Console.WriteLine();

        insertionSortReverse(arr);
        foreach(int j in arr) {
            Console.Write(j + " ");
        }
    }
}