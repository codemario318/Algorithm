function solution(heights) {
    return heights.map((v,i) => {
      while(i) {
        i--;
        if (heights[i] > v){
          return i+1;
        }
      }
      return 0;
    })
}


var a = [6,9,5,7,4]
var b = [3,9,9,3,5,7,2]
var c = [1,5,3,6,7,6,5]
console.log(solution(a));
console.log(solution(b));
console.log(solution(c));
