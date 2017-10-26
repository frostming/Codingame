/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

function getDistance(lonA, latA, lonB, latB) {
  var newArray = Array.map([lonA, latA, lonB, latB], function(e){
    if (typeof e === 'string') {
      e = parseFloat(e.replace(',', '.'));
    }
    return e * Math.PI / 180;
  });
  var x = (newArray[2] - newArray[0]) * Math.cos((newArray[1] + newArray[3]) / 2),
    y = newArray[3] - newArray[1];
  return Math.sqrt(x*x + y*y) * 6371;
}


var LON = readline();
var LAT = readline();
var N = parseInt(readline());

var minDis = 99999999, answer = undefined;

for (var i = 0; i < N; i++) {
    var DEFIB = readline();
    var splitted = DEFIB.split(';');
    var distance = getDistance(splitted[4], splitted[5], LON, LAT);
    if (distance < minDis) {
      answer = splitted[1];
      minDis = distance;
    }
}

// Write an action using print()
// To debug: printErr('Debug messages...');

print(answer);
