package main

func open(room int, unlocked []bool, rooms [][]int) {
	unlocked[room] = true

	for _, key := range rooms[room] {
		if !unlocked[key] {
			open(key, unlocked, rooms)
		}
	}
}

func canVisitAllRooms(rooms [][]int) bool {
	unlocked := make([]bool, len(rooms))

	for pos, _ := range unlocked {
		unlocked[pos] = false
	}

	open(0, unlocked, rooms)

	for pos, _ := range unlocked {
		if !unlocked[pos] {
			return false
		}
	}

	return true
}
