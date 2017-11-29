package main


import (
	"crypto/md5"
	"fmt"
	"sort"
	"strconv"
	"strings"
	"sync"
	hex "encoding/hex"
)


type pair struct {
	pass string
	count int
	pos string
}


func lookForHash(s string, init_c int, size int, c chan<- pair, wg *sync.WaitGroup) {

	defer wg.Done()
	for i := init_c; i < init_c + size; i++  {
		candidate := []byte(s + strconv.Itoa(i))
		h := md5.Sum(candidate)
		h_str := hex.EncodeToString(h[:])

		if strings.HasPrefix(h_str, "00000") {
			c <- pair{string(h_str[6]), i, string(h_str[5])}
		}
	}
	
}


func main() {
	workers := 250
	max := 52785680
	start := 0
	step := max / workers
	input := "ugkcyxxp"
	var wg sync.WaitGroup

	c := make(chan pair, workers * 10)

	for i := 0; i < workers; i++ {
		wg.Add(1)
		start = i * step
		//fmt.Println(start, step)
		go lookForHash(input, start, step, c, &wg)
	}

	wg.Wait()
	close(c)
	var y []int
	y2 :=  make(map[int]pair)
	ans := make([]string, 8)

	for elem := range c {
		y = append(y, elem.count)
		y2[elem.count] = elem
	}
	sort.Ints(y)

	for _, q := range y {
		fmt.Println(q, y2[q].pos, y2[q].pass)
		pos_i, _ := strconv.ParseInt(y2[q].pos, 16, 0)
		fmt.Println(q, pos_i, y2[q].pass)
		if pos_i < 8 {
			if len(ans[pos_i]) == 0 {
				ans[pos_i] = y2[q].pass
			}
		}
	}
	fmt.Println(ans)

}


