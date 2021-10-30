package main

import (
	"fmt"
	"math/rand"
	"os"
)

func main() {
	for true {
		var w, h, playerID, tick int
		fmt.Scan(&w, &h, &playerID, &tick)
		// read map
		for i := 0; i < h; i++ {
			for j := 0; j < w; j++ {
				var c rune
				fmt.Scan(&c)
			}
		}

		// number of entities
		var n int
		fmt.Scan(&n)

		// read entities
		for i := 0; i < n; i++ {
			var entType string
			var pID, x, y, param1, param2 int

			fmt.Scan(&entType, &pID, &x, &y, &param1, &param2)
		}

		// use `os.Stderr` to print for debugging
		fmt.Fprintf(os.Stderr, "debug code\n")

		// this will choose one of random actions
		actions := []string{"left", "right", "up", "down", "bomb"}
		randomIndex := rand.Intn(5)

		// bot action
		fmt.Println(actions[randomIndex])
	}
}
