package main

import "fmt"
import "os"
import "bufio"
import "strings"
import "strconv"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/


func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Buffer(make([]byte, 1000000), 1000000)

    var n int
    scanner.Scan()
    fmt.Sscan(scanner.Text(),&n)

    scanner.Scan()
    inputs := strings.Split(scanner.Text()," ")
    var maxPeak, maxLoss int64
    maxPeak, maxLoss = 0, 0
    for i := 0; i < n; i++ {
        v,_ := strconv.ParseInt(inputs[i],10,32)
        if v > maxPeak {
            maxPeak = v
        } else if v - maxPeak < maxLoss {
            maxLoss = v - maxPeak
        }
    }

    // fmt.Fprintln(os.Stderr, "Debug messages...")
    fmt.Println(maxLoss)// Write answer to stdout
}
