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

const (
    NULL = iota
    LEFT
    DOWN
    RIGHT
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Buffer(make([]byte, 1000000), 1000000)
    topDirection := []int{NULL, DOWN, NULL, DOWN, LEFT, RIGHT, NULL, DOWN, NULL, DOWN, LEFT, RIGHT, NULL, NULL}
    leftDirection := []int{NULL, DOWN, RIGHT, NULL, NULL, DOWN, RIGHT, NULL, DOWN, DOWN, NULL, NULL, NULL, DOWN}
    rightDirection := []int{NULL, DOWN, LEFT, NULL, DOWN, NULL, LEFT, DOWN, DOWN, NULL, NULL, NULL, DOWN, NULL}
    // W: number of columns.
    // H: number of rows.
    var W, H int
    scanner.Scan()
    fmt.Sscan(scanner.Text(),&W, &H)
    rooms := make([][]int64, H)
    for i := 0; i < H; i++ {
        scanner.Scan()
        line := strings.Split(scanner.Text(), " ")
        rooms[i] = make([]int64, W)
        for j, v := range(line) {
            rooms[i][j], _ = strconv.ParseInt(v, 10, 32)
        }
        //LINE := scanner.Text() // represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    }
    // EX: the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
    var EX int
    scanner.Scan()
    fmt.Sscan(scanner.Text(),&EX)

    for {
        var XI, YI int
        var POS string
        scanner.Scan()
        fmt.Sscan(scanner.Text(),&XI, &YI, &POS)

        room := rooms[YI][XI]
        var next int
        switch POS {
            case "TOP":
                next = topDirection[room]
            case "LEFT":
                next = leftDirection[room]
            case "RIGHT":
                next = rightDirection[room]
        }

        switch next {
            case DOWN:
                fmt.Println(XI, YI+1)
            case LEFT:
                fmt.Println(XI-1, YI)
            case RIGHT:
                fmt.Println(XI+1, YI)
        }
    }
}
