package main

import (
	"fmt"
	"math/rand"
	"os"
)

func main() {
	for true {
		var n, m, playerID, tick int
		fmt.Scan(&n, &playerID, &tick)
		// read cities
		for i := 0; i < n; i++ {
			line := ""
			fmt.Scan(&line)
			fmt.Fprint(os.Stderr, line, "\n")
		}

		// number of movements
		fmt.Scan(&m)

		// read movements
		for i := 0; i < m; i++ {
			fmt.Scan(&line)
		}

		// use `os.Stderr` to print for debugging
		fmt.Fprintf(os.Stderr, "debug code\n")
		fmt.Println("100 100 200 200")
	}
}
