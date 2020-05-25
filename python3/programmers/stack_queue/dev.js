function solution(progresses, speeds) {
    var answer = [], day = Math.ceil((100-progresses[0])/speeds[0]);
    var cnt = 1, p = 0;

    for (var i = 1; i < progresses.length; i++) {
        p = progresses[i] + speeds[i]*day;
        if ( p >= 100) {
          cnt++;
        } else {
          answer.push(cnt);
          cnt = 1;
          day += Math.ceil((100-p)/speeds[i]);
        }
    }
    return cnt == 0 ? answer : answer.concat(cnt);
}
// console.log(answer)
var a1 =[93,30,55], a2=[1,30,5];
console.log(solution(a1,a2));
// console.log(Math.floor(7/3));
// console.log(Boolean(0));
