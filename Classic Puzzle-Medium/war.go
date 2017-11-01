package main

import (
    "fmt"
    // "os"
    "strconv"
    // "container/list"
)

//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
type Queue struct {
    Data []string
}

func (self *Queue) Len() int {
    return len(self.Data)
}


func (self *Queue) Push(v string) {
    self.Data = append(self.Data, v)
}

func (self *Queue) PopHead() string {
    rv := self.Data[0]
    self.Data = self.Data[1:]
    return rv
}

func convert(card string) int {
    switch card[0] {
        case 'A':
            return 14
        case 'J':
            return 11
        case 'Q':
            return 12
        case 'K':
            return 13
        default:
            value, _ := strconv.Atoi(card[0:len(card)-1])
            return value
    }
}


func battle(deck1 *Queue, deck2 *Queue, war1 *Queue, war2 *Queue) {
    card1 := deck1.PopHead()
    card2 := deck2.PopHead()
    war1.Push(card1)
    war2.Push(card2)
    if diff := convert(card1) - convert(card2); diff > 0 {
        for war1.Len() > 0 {
            deck1.Push(war1.PopHead())
        }
        for war2.Len() > 0 {
            deck1.Push(war2.PopHead())
        }
    } else if diff < 0 {
        for war1.Len() > 0 {
            deck2.Push(war1.PopHead())
        }
        for war2.Len() > 0 {
            deck2.Push(war2.PopHead())
        }
    } else {
        for i:=0; i<3; i++ {
            if deck1.Len() == 0 || deck2.Len() == 0 {
                return
            } else {
                war1.Push(deck1.PopHead())
                war2.Push(deck2.PopHead())
            }
        }
        if deck1.Len() > 0 && deck2.Len() > 0{
            battle(deck1, deck2, war1, war2)
        }
    }
}

func main() {
    // n: the number of cards for player 1
    var n int
    fmt.Scan(&n)

    var deck1, deck2, war1, war2 Queue

    for i := 0; i < n; i++ {
        // cardp1: the n cards of player 1
        var cardp1 string
        fmt.Scan(&cardp1)
        deck1.Push(cardp1)
    }
    // m: the number of cards for player 2
    var m int
    fmt.Scan(&m)

    for i := 0; i < m; i++ {
        // cardp2: the m cards of player 2
        var cardp2 string
        fmt.Scan(&cardp2)
        deck2.Push(cardp2)
    }

    round := 0
    for ; deck1.Len() > 0 && deck2.Len() > 0; round++ {
        battle(&deck1, &deck2, &war1, &war2)
    }

    if war1.Len() > 0|| war2.Len() > 0 {
        fmt.Println("PAT")
    } else if deck1.Len() > 0 {
        fmt.Println(1, round)
    } else {
        fmt.Println(2, round)
    }
}
