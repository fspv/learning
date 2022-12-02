package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func day2_1_score(left, right string) int {
	total := 0
	switch right {
	case "X":
		total += 1
		switch left {
		case "A":
			total += 3
		case "B":
			total += 0
		case "C":
			total += 6
		}
	case "Y":
		total += 2
		switch left {
		case "A":
			total += 6
		case "B":
			total += 3
		case "C":
			total += 0
		}
	case "Z":
		total += 3
		switch left {
		case "A":
			total += 0
		case "B":
			total += 6
		case "C":
			total += 3
		}
	}

	return total
}

func day2_1() {
	file, err := os.Open("day02_2.input")

	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	total := 0

	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())

		left, right := fields[0], fields[1]

		total += day2_1_score(left, right)

	}

	fmt.Println(total)
}
