package main

import "fmt"
import "strings"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
    // W: width of the building.
    // H: height of the building.
    var W, H int
    fmt.Scan(&W, &H)

    // N: maximum number of turns before game over.
    var N int
    fmt.Scan(&N)

    var X0, Y0 int
    fmt.Scan(&X0, &Y0)

    left, right, top, bottom := 0, W-1, 0, H-1
    for {
        // bombDir: the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        var bombDir string
        fmt.Scan(&bombDir)
        if strings.IndexByte(bombDir, 'U') >= 0 {
            bottom = Y0 - 1
        } else if strings.IndexByte(bombDir, 'D') >= 0 {
            top = Y0 + 1
        }
        if strings.IndexByte(bombDir, 'L') >= 0 {
            right = X0 - 1
        } else if strings.IndexByte(bombDir, 'R') >= 0 {
            left = X0 + 1
        }
        X0, Y0 = left + (right - left)/2, top + (bottom - top)/2
        // fmt.Fprintln(os.Stderr, "Debug messages...")

        // the location of the next window Batman should jump to.
        fmt.Println(X0, Y0)
    }
}
