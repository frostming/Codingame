/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var N = parseInt(readline());
var horses = [];
var min_d = 9999999;
for (var i = 0; i < N; i++) {
    var pi = parseInt(readline());
    horses.push(pi);
}

horses.sort(function(a, b){
    return a - b;
});

// Write an action using print()
// To debug: printErr('Debug messages...');
for (var i = 0; i < horses.length - 1; i++) {
    if (horses[i + 1] - horses[i] < min_d) {
        min_d = horses[i + 1] - horses[i];
    }
}
print(min_d);
