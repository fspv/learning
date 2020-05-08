package main

func checkStraightLine(coordinates [][]int) bool {
	k := func(x1, y1, x2, y2 int) float64 { return float64(y2-y1) / float64(x2-x1) }
	b := func(x1, y1, x2, y2 int) float64 { return float64(y1*x2-y2*x1) / float64(x2-x1) }

	point1 := coordinates[0]
	point2 := coordinates[1]

	k_init := k(point1[0], point1[1], point2[0], point2[1])
	b_init := b(point1[0], point1[1], point2[0], point2[1])

	for _, point := range coordinates[2:] {
		k_new := k(point1[0], point1[1], point[0], point[1])
		b_new := b(point1[0], point1[1], point[0], point[1])
		if k_new != k_init || b_new != b_init {
			return false
		}
	}
	return true
}
