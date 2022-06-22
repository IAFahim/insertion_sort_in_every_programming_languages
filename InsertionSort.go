package main

import "fmt"

func insertion_sort(arr []int) []int {
	for i := 1; i < len(arr); i++ {
		key := arr[i]
		j := i - 1
		for j >= 0 && key < arr[j] {
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = key
	}
	return arr
}

func insertion_sort_reverse(arr []int) []int {
	for i := 1; i < len(arr); i++ {
		key := arr[i]
		j := i - 1
		for j >= 0 && key > arr[j] {
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = key
	}
	return arr
}

func main() {
	arr := []int{4, 2, 0, 6, 9}

	ascending := insertion_sort(arr)
	fmt.Printf("%v", ascending)

    fmt.Println();

	descending := insertion_sort_reverse(arr)
	fmt.Printf("%v", descending)
}
