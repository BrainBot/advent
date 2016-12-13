package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	//"bufio"
)

func loadInput(filename string) (lines []string) {
	content, _ := ioutil.ReadFile(filename)
	lines = strings.Split(string(content), "\n")
	return lines
}

func isTriangle(nums []int) (isTri int) {

	a := nums[0]
	b := nums[1]
	c := nums[2]

	isTri = 0
	if a+b > c && a+c > b && b+c > a {
		isTri = 1
	}
	return isTri

}

func main() {

	lines := loadInput("p3.input")
	valid := 0
	invalid := 0

	var first, second, third []int

	for _, line := range lines {
		
		
		if ! (len(line) > 0) {
			fmt.Println("Not 3 sides, not a triangle")
			continue
		}
		var a, b, c int

		a, _ = strconv.Atoi(strings.TrimSpace(line[2:5]))
		b, _ = strconv.Atoi(strings.TrimSpace(line[7:10]))
		c, _ = strconv.Atoi(strings.TrimSpace(line[12:15]))

		first = append(first, a)
		second = append(second, b)
		third = append(third, c)

		if len(first) == 3 {
			valid += isTriangle(first)
			valid += isTriangle(second)
			valid += isTriangle(third)
			first = nil
			second = nil
			third = nil
		}

		fmt.Println(line, "a,b,c", a, b, c)

		
	}

	fmt.Println("Valid: ", valid)
	fmt.Println("Invalid: ", invalid)

}
