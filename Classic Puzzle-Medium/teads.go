package main

import "fmt"
import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

type List []int

func main() {
    // n: the number of adjacency relations
    var n int
    fmt.Scan(&n)
    edges := make(map[int]List)
    counter := make(map[int]int)
    maxLen := 0
    for i := 0; i < n; i++ {
        // xi: the ID of a person which is adjacent to yi
        // yi: the ID of a person which is adjacent to xi
        var xi, yi int
        fmt.Scan(&xi, &yi)
        fmt.Fprintln(os.Stderr, xi, yi)
        edges[xi] = append(edges[xi], yi)
        edges[yi] = append(edges[yi], xi)
        counter[xi]++
        counter[yi]++
    }

    // fmt.Fprintln(os.Stderr, "Debug messages...")

    for len(edges) > 2 {
        var delA, delB List

        for n, val := range(edges) {
            if counter[n] == 1 {
                delA = append(delA, n)
                for _, j := range(val) {
                    if counter[j] > 1 {
                        delB = append(delB, j)
                    }
                }
            }
        }

        for _, n := range(delA) {
            delete(edges, n)
            delete(counter, n)
        }
        for _, n := range(delB) {
            counter[n]--
        }

        maxLen++
    }
    if len(edges) == 2 {
        maxLen++
    }
    fmt.Println(maxLen)
}
