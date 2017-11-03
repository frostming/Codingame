package main

import "fmt"
//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
type Tree map[byte]Tree


func main() {
    var N int
    fmt.Scan(&N)
    storage := make(Tree)
    number := 0
    for i := 0; i < N; i++ {
        current := &storage
        var telephone string
        fmt.Scan(&telephone)
        for _, c := range([]byte(telephone)) {
            _, ok := (*current)[c]
            if !ok {
                (*current)[c] = make(Tree)
                number++
            }
            next := (*current)[c]
            current = &next
        }
    }

    // fmt.Fprintln(os.Stderr, "Debug messages...")

    // The number of elements (referencing a number) stored in the structure.
    fmt.Println(number)
}
