package main

import (
	"fmt"
)

func game(guess []int, answer []int) int {
	count := 0
	for k, v := range guess {
		if v == answer[k] {
			count++
		}
	}
	return count
}

func main() {
	guess := []int{1, 2, 3}
	answer := []int{1, 2, 3}
	res := game(guess, answer)
	fmt.Print(res)
}
