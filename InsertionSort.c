#include <stdio.h>

void insertion_sort(int *arr, int size) {
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

void insertion_sort_reverse(int *arr, int size) {
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

    insertion_sort(arr,sizeof(arr) / sizeof(arr[0]) );
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        printf("%d ",arr[i]);
    }

    printf("\n");

    insertion_sort_reverse(arr,sizeof(arr) / sizeof(arr[0]) );
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        printf("%d ",arr[i]);
    }
}