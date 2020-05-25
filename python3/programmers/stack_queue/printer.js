function solution(priorities, location) {
    var answer = 0, idx = 0, pos = 0;

    while (answer < priorities.length) {
        answer++;
        idx = pos;
        for (var i = 0; i < priorities.length; i++) {
          if (priorities[idx%priorities.length] > priorities[pos] ){
            pos = idx%priorities.length;
          }
          idx++;
        }

        priorities[pos] = 0;

        if (pos === location){
          return answer;
        }
    }
    return answer;
}

var a1 = [2, 1, 3, 2], a2 = 2;
var b1 = [1, 1, 9, 1, 1, 1], b2 = 0;

console.log(solution(a1,a2));
console.log(solution(b1,b2));
// console.log(a1.slice(1).indexOf(3));
// for (var i = 0; i < 10; i++) {
//   b2++;
//   console.log(b2);
// }
