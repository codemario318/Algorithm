function solution(citations) {
    var answer = 0;

    citations.sort().reverse();

    for (var i = 0; i < citations.length; i++) {
      answer = i;
      if (i >= citations[i]) {
        return i;
      };
    };

    return answer+1;
}

var a=[3, 0, 6, 1, 5];
var b = [10,10,10,10]
console.log(solution(a));
console.log(solution(b));
