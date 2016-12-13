package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	//"bufio"
)

type pair struct {
	x, y int
}

func main() {
	keypad := [][]int{}
	row1 := []int{-1, -1, 1, -1, -1}
	row2 := []int{-1, 2, 3, 4, -1}
	row3 := []int{5, 6, 7, 8, 9}
	row4 := []int{-1, 0xA, 0xB, 0xC, -1}
	row5 := []int{-1, -1, 0xD, -1, -1}
	keypad = append(keypad, row1)
	keypad = append(keypad, row2)
	keypad = append(keypad, row3)
	keypad = append(keypad, row4)
	keypad = append(keypad, row5)
	results := []string{}

	pos := pair{0, 2}

	content, _ := ioutil.ReadFile("p2.input")
	lines := strings.Split(string(content), "\n")
	//fmt.Println("Pos Before:", pos)
	fmt.Println(keypad)
	for _, line := range lines {
		fmt.Println(line)
		key, end := findKey(keypad, pos, line)
		fmt.Println(end)
		fmt.Println("Key To Press", key)
		pos = end
		results = append(results, strconv.FormatInt(int64(key), 16))
	}
	fmt.Println("Bathroom Keycode: ", results)

}

func findKey(kp [][]int, start pair, directions string) (key int, end pair) {

	for _, dir := range strings.Split(directions, "") {
		switch dir {
		case "U":
			fmt.Println("Up")
			start = movePos(kp, start, 0, -1)
		case "D":
			//fmt.Println("Down")
			start = movePos(kp, start, 0, 1)
		case "L":
			fmt.Println("Left")
			start = movePos(kp, start, -1, 0)
		case "R":
			//fmt.Println("Right")
			start = movePos(kp, start, 1, 0)
		default:
			fmt.Println(dir)
		}
		fmt.Println("findKey:", start)
	}
	return kp[start.y][start.x], start
}

// assume keypad is square
func movePos(kp [][]int, pos pair, x, y int) (newPos pair) {
	// ensure the index is in range
	if pos.x+x < len(kp[pos.y]) && pos.x+x > -1 {
		// ensure the move is valid
		if kp[pos.y][pos.x+x] > 0 {
			pos.x += x
		}

	}
	if pos.y+y < len(kp) && pos.y+y > -1 {
		// ensure the move is valid
		if kp[pos.y+y][pos.x] > 0 {
			pos.y += y
		}
	}
	//fmt.Println("Pos", pos)
	return pos
}
