package main

import "sort"

type Player struct {
	played uint
	lost   uint
}

func findWinners(matches [][]int) [][]int {
	playerMap := map[int]*Player{}

	for _, match := range matches {
		winner := match[0]
		loser := match[1]

		if player, ok := playerMap[winner]; ok {
			player.played++
		} else {
			playerMap[winner] = &Player{1, 0}
		}

		if player, ok := playerMap[loser]; ok {
			player.played++
			player.lost++
		} else {
			playerMap[loser] = &Player{1, 1}
		}
	}

	lostNone := []int{}
	lostOne := []int{}

	for pos, player := range playerMap {
		if player.played > 0 {
			if player.lost == 0 {
				lostNone = append(lostNone, pos)
			}

			if player.lost == 1 {
				lostOne = append(lostOne, pos)
			}
		}
	}

	sort.Ints(lostNone)
	sort.Ints(lostOne)

	result := [][]int{}

	result = append(result, lostNone)
	result = append(result, lostOne)

	return result
}
