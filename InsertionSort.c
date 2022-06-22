#include <stdio.h>

void insertionSort(int *arr, int size) {
    for (int i = 1; i < size; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && key < arr[j]) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void insertionSortReverse(int *arr, int size) {
    for (int i = 1; i < size; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && key > arr[j]) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int arr[]={4, 2, 0, 6, 9};

    insertionSort(arr,sizeof(arr) / sizeof(arr[0]) );
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        printf("%d ",arr[i]);
    }

    printf("\n");

    insertionSortReverse(arr,sizeof(arr) / sizeof(arr[0]) );
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        printf("%d ",arr[i]);
    }
}