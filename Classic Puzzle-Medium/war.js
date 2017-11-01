/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
var deck1 = [];
var n = parseInt(readline()); // the number of cards for player 1
for (var i = 0; i < n; i++) {
    var cardp1 = readline(); // the n cards of player 1
    deck1.push(cardp1);
}
var deck2 = [];
var m = parseInt(readline()); // the number of cards for player 2
for (var i = 0; i < m; i++) {
    var cardp2 = readline(); // the m cards of player 2
    deck2.push(cardp2);
}

var round = 0;

function fight(card1, card2) {
    var values = Array.map([card1, card2], function(e) {
        switch(e.slice(0, -1)) {
            case 'J':
                return 11;
            case 'Q':
                return 12;
            case 'K':
                return 13;
            case 'A':
                return 100;
            default:
                return parseInt(e.slice(0, -1));
        }
    });
    return values[0] - values[1];
}

function battle(deck1, deck2, war1, war2) {
    var card1 = deck1.shift(),
        card2 = deck2.shift();
    war1.push(card1);
    war2.push(card2);
    var result = fight(card1, card2);
    if (result > 0) {
        while(war1.length > 0) {
            deck1.push(war1.shift());
        }
        while(war2.length > 0) {
            deck1.push(war2.shift());
        }
    } else if (result < 0) {
        while(war1.length > 0) {
            deck2.push(war1.shift());
        }
        while(war2.length > 0) {
            deck2.push(war2.shift());
        }
    } else {
        for (var i = 0; i < 3; i++) {
            if (deck1.length === 0 || deck2.length === 0) {
                return;
            }
            war1.push(deck1.shift());
            war2.push(deck2.shift());
        }
        if (deck1.length > 0 && deck2.length > 0) {
            battle(deck1, deck2, war1, war2);
        }
    }
}

var war1 = [], war2 = [];

while (deck1.length > 0 && deck2.length > 0) {
    printErr('Round:', round)
    printErr(deck1);
    printErr(deck2);
    printErr(war1);
    printErr(war2);
    battle(deck1, deck2, war1, war2);
    round++;
}

if(war1.length > 0 || war2.length > 0) {
    print('PAT');
} else if (deck2.length === 0) {
    print(1, round);
} else {
    print(2, round);
}
