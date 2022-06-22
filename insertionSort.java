import java.io.*;

public class insertion_sort {
    static void insertion_sort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && key < arr[j]) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    static void insertion_sort_reverse(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && key > arr[j]) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        int[] arr = {4, 2, 0, 6, 9};

        insertion_sort(arr);
        for (int j : arr) {
            System.out.print(j + " ");
        }

        System.out.println();

        insertion_sort_reverse(arr);
        for (int j : arr) {
            System.out.print(j + " ");
        }
    }
}