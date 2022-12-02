package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func day2_2_score(left, right string) int {
	total := 0
	switch left {
	case "A": // Rock
		switch right {
		case "X": // Lose
			total += 3 + 0
		case "Y": // Draw
			total += 1 + 3
		case "Z": // Win
			total += 2 + 6
		}
	case "B": // Paper
		switch right {
		case "X": // Lose
			total += 1 + 0
		case "Y": // Draw
			total += 2 + 3
		case "Z": // Win
			total += 3 + 6
		}
	case "C": // Scissors
		switch right {
		case "X": // Lose
			total += 2 + 0
		case "Y": // Draw
			total += 3 + 3
		case "Z": // Win
			total += 1 + 6
		}
	}

	return total
}

func day2_2() {
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

		total += day2_2_score(left, right)
	}

	fmt.Println(total)
}
