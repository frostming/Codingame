/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var inputs = readline().split(' ');
var W = parseInt(inputs[0]); // width of the building.
var H = parseInt(inputs[1]); // height of the building.
var N = parseInt(readline()); // maximum number of turns before game over.
var inputs = readline().split(' ');
var X0 = parseInt(inputs[0]);
var Y0 = parseInt(inputs[1]);
var left = 0, right = W-1, topY = 0, bottom = H -1;

// game loop
while (true) {
    var bombDir = readline(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if(bombDir.indexOf('U') >= 0) {
        bottom = Y0 - 1;
    } else if (bombDir.indexOf('D') >= 0) {
        topY = Y0 + 1;
    }
    if(bombDir.indexOf('L') >= 0) {
        right = X0 - 1;
    } else if (bombDir.indexOf('R') >= 0) {
        left = X0 + 1;
    }

    X0 = parseInt(left + (right - left) / 2);
    Y0 = parseInt(topY + (bottom - topY) / 2);
    // the location of the next window Batman should jump to.
    print(X0, Y0);
}
