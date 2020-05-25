// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
    // write your code in JavaScript (Node.js 8.9.4)
    var res = 0;
    var count = 0;

    for (var n of N.toString(2)) {
        if (n == 0) {
            count++;
        } else {
            res = Math.max(res,count);
            count = 0;
        }
    }

    return res;
}

console.log(solution(1024));
console.log(solution(1));
console.log(solution(3));
console.log(solution(2));
console.log(solution(2));
console.log(solution(2));
