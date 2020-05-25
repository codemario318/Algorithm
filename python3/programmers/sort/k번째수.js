// function solution(array, commands) {
//     var answer = [];
//
//     for (var i = 0; i < commands.length; i++) {
//         var temp = array.slice(commands[i][0]-1,commands[i][1]);
//         temp.sort(function(a,b) {
//           return a-b
//         });
//         answer.push(temp[commands[i][2]-1]);
//     }
//     return answer;
// }

function solution(array, commands) {
    return commands.map(
      ([s,e,k]) => array.slice(s-1,e)
                        .sort((x,y) => x-y)[k-1]);
}
var a = [1, 5, 2, 6, 3, 7, 4];
var c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
console.log(solution(a,c))
