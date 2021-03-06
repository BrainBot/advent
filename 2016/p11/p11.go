package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"sort"
	"strings"
)

const TARGET_FLOOR = 4

type Comp struct {
	mic int
	rtg int
}

type Comps []Comp

type State struct {
	ele int
	comps Comps
}

func (slice Comps) Len() int {
	return len(slice)
}

func (slice Comps) Less(i, j int) bool {
	return slice[i].mic < slice[j].mic || slice[i].mic == slice[j].mic && slice[i].rtg <= slice[j].rtg
}

func (slice Comps) Swap(i, j int) {
	slice[i], slice[j] = slice[j], slice[i]
}

func loadInput(filename string) (lines []string) {
	content, _ := ioutil.ReadFile(filename)
	lines = strings.Split(string(content), "\n")
	return lines
}

func main() {
	lines := loadInput("p11_test2.input")
	regex_str := `a (\w+)[-\w]* (microchip|generator)[ .]`
	var comps Comps

	r, _ := regexp.Compile(regex_str)

	// INIT
	start := make(map[string]Comp)
	for i, line := range lines {
		a := r.FindAllStringSubmatch(line, -1)
		fmt.Println(line)
		for _, tmp := range a {
			name := tmp[1]
			comp := tmp[2]
			c, ok := start[name]
			if !ok {
				c = Comp{}
			}
			if comp[0] == 'm' {
				c.mic = i + 1
				//fmt.Println("This is a microchip")
			} else {
				c.rtg = i + 1
				//fmt.Println("This is a generator")
			}
			start[name] = c
			//fmt.Println(tmp[1], tmp[2])
		}
	}
	for k := range start {
		comps = append(comps, start[k])
	}
	sort.Sort(comps)
	fmt.Println(comps)

	// While True // We control the breakout
	var front []State
	front = append(front, State{1, comps})
	fmt.Println(start)
	index := 1
	win := false

	for {
		var new_front []State
		// For each move in our front:
		for _, s := range front {
			fmt.Println(s)

		

			// *SPEED* sort the list so our hash is consistant
			// If a move finishes, break out
			win := true
			for _, c := range s.comps {
				win = win && c.mic == TARGET_FLOOR && c.rtg == TARGET_FLOOR
			}
			if win {
				break
			}
			// Discard moves that lose
			// *SPEED* Combine the above 3 moves?

			// Discard moves that we've already seen
			// Generate all moves from the current state
			// Add moves to the new front

			// increment step num
			// set current front to the new front
		}
		break
		index++
	}
	print index
}
