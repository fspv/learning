func findComplement(num int) int {
    x := 1
    for x < num {
        x = x << 1
        x += 1
    }
    return ^num & x
}
