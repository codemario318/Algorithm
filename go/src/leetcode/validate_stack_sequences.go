package leetcode

import "fmt"

func validateStackSequences(pushed []int, popped []int) bool {
	defer func() bool {
		if r := recover(); r != nil {
			return true
		}
		return false
	}()

	pushedIdx := 0
	poppedIdx := 0

	var stack []int
	top := 0

	for pushedIdx < len(pushed) || poppedIdx < len(popped) {
		fmt.Println(stack)
		if len(stack) == 0 {
			stack = append(stack, pushed[pushedIdx])
			pushedIdx++
			fmt.Println("push ", stack[len(stack)-1])
			continue
		} else {
			top = stack[len(stack)-1]
		}

		if top == popped[poppedIdx] {
			fmt.Println("pop ", stack[len(stack)-1])
			stack = stack[:len(stack)-1]
			poppedIdx++
		} else {
			stack = append(stack, pushed[pushedIdx])
			pushedIdx++
			fmt.Println("push ", stack[len(stack)-1])
		}
	}

	return len(stack) == 0
}
