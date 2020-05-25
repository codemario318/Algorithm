// function solution(numbers) {
//   var answer = numbers.sort(sortFunc).join('');
//   return answer == Array(answer.length+1).join(0) ? 0:answer;
// }
//
// function sortFunc(a,b){
//   a = String(a).repeat(4).slice(0,4);
//   b = String(b).repeat(4).slice(0,4);
//
//   return a > b ? -1: (a < b)? 1:0
// };

function solution(numbers) {
    var answer = numbers.map(v=>v+'')
                        .sort((a,b) => (b+a)*1 - (a+b)*1)
                        .join('');

    return answer[0]==='0'?'0':answer;
}

var a =[6, 10, 2];
var b =[3, 30, 34, 5, 9];
var c = [20, 200, 20];
var d = [0,0,0]
console.log(solution(a));
console.log(solution(b));
console.log(solution(c));
console.log(solution(d));

// console.log(Array(2).join(4));
// console.log(Array(3).join(0));
