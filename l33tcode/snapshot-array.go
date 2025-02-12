package main

type value struct {
	value      int
	snapshotID int
}

type SnapshotArray struct {
	values     [][]value
	snapshotID int
}

func Constructor(length int) SnapshotArray {
	values := make([][]value, length)
	for i := range values {
		values[i] = []value{{}}
	}
	return SnapshotArray{
		values: values,
	}
}

func (this *SnapshotArray) Set(index int, val int) {
	if this.values[index][len(this.values[index])-1].snapshotID != this.snapshotID {
		this.values[index] = append(this.values[index], value{})
	}
	this.values[index][len(this.values[index])-1] = value{val, this.snapshotID}
}

func (this *SnapshotArray) Snap() int {
	this.snapshotID += 1
	return this.snapshotID - 1
}

func (this *SnapshotArray) Get(index int, snap_id int) int {
	left, right := 0, len(this.values[index])

	for left < right {
		mid := left + (right-left)/2

		if this.values[index][mid].snapshotID <= snap_id {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return this.values[index][left-1].value
}
