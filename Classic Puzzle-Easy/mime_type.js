/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var N = parseInt(readline()); // Number of elements which make up the association table.
var Q = parseInt(readline()); // Number Q of file names to be analyzed.

var mimeTypes = {};

for (var i = 0; i < N; i++) {
    var inputs = readline().split(' ');
    var EXT = inputs[0]; // file extension
    var MT = inputs[1]; // MIME type.
    mimeTypes[EXT.toLowerCase()] = MT;
}

for (var i = 0; i < Q; i++) {
    var FNAME = readline(); // One file name per line.
    var lastDot = FNAME.lastIndexOf('.')
    if (lastDot < 0) {
      print('UNKNOWN')
    } else {
      var extension = FNAME.slice(lastDot + 1).toLowerCase();
      print(mimeTypes[extension]||'UNKNOWN');
    }
}
