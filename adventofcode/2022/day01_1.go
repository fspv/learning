package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("day01_1.input")

	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	soFar := 0
	max := 0

	for scanner.Scan() {
		text := scanner.Text()

		if text == "" {
			soFar = 0
		} else {
			value, err := strconv.Atoi(text)

			if err != nil {
				log.Fatal(err)
			}

			soFar += value
		}

		if soFar > max {
			max = soFar
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(max)
}
