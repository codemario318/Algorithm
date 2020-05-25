// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A, K) {
    // write your code in JavaScript (Node.js 8.9.4)
    var n = K % A.length;
    console.log(n);
    if (n > 0) {
        for (var i = 0; i < n; i++) {
            A.unshift(A.pop());
        }
    } else {
        for (var i = n; i < 0; i++) {
            A.push(A.shift());
        }
    }
    return A;
}

console.log(solution([3, 8, 9, 7, 6],3));
console.log(solution([1,2,3,4],4));
console.log(solution([0,0,0],4));
console.log(solution([3, 8, 9, 7, 6],-3));
