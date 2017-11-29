package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"sort"
	"strings"
)

func loadInput(filename string) (lines []string) {
	content, _ := ioutil.ReadFile(filename)
	lines = strings.Split(string(content), "\n")
	return lines
}

func sortKeyMap(m map[string]int) (keys []string) {

	// make the reverse map
	rev_m := make(map[int]string)
	var rev_keys []int
	for k, v := range m {
		rev_m[v] = k
	}
	fmt.Println("!!!!!", rev_m)

	// grabs its keys
	for k := range rev_m {
		rev_keys = append(rev_keys, k)
	}

	// sort the keys
	sort.Ints(rev_keys)

	// return the sorted keys from m
	for i := range rev_keys {
		keys = append(keys, rev_m[i])
	}

	return keys
}

func main() {

	lines := loadInput("p4_test.input")

	regex_str := `([a-z\-]*)-([\d]*)\[([a-z]*)\]`

	r, _ := regexp.Compile(regex_str)

	for _, line := range lines {
		a := r.FindAllStringSubmatch(line, -1)
		if len(a[0]) != 4 {
			fmt.Println("Whoops: ", line, " splits into ", len(a[0]), " parts which are: ", a[0])
			break
		}
		name := a[0][1]
		sector := a[0][2]
		checksum := a[0][3]

		name = strings.Replace(name, "-", "", -1)
		checksum_list := strings.Split(checksum, "")

		// make map of room name
		name_cnt := make(map[string]int)
		for _, char := range name {
			name_cnt[string(char)] += 1
		}

		// sort the keys based on the index

		fmt.Println(name, sector, checksum, checksum_list)
		fmt.Println(name_cnt)

		fmt.Println(sortKeyMap(name_cnt))
		break

	}

}
