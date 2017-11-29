package main

import (
	"fmt"
	"crypto/md5"
	"strconv"
	"strings"
	hex "encoding/hex"
	"sync"
	//"io"
)

type pair struct {
	pass string
	count int

}


func lookForHash(s string, init_c int, size int, c chan<- pair, wg *sync.WaitGroup) {
	defer wg.Done()

	for i := init_c; i < init_c + size; i++  {
		candidate := []byte(s + strconv.Itoa(i))
		h := md5.Sum(candidate)
		h_str := hex.EncodeToString(h[:])
		//fmt.Println(i, h_str)
		if strings.HasPrefix(h_str, "00000") {
			c <- pair{string(h_str[5]), i}
		}
	}
} 

func main() {
	workers := 1000
	max := 214748364700
	step := max / workers
	input := "abc"
	var wg sync.WaitGroup

	c := make(chan pair, 8)

	for i := 0; i < workers; i++ {
		wg.Add(1)
		start := i * step
		go lookForHash(input, start, step , c, &wg)
	}
	wg.Wait()
	close(c)
	for elem := range c {
		fmt.Println(elem)
	}

}