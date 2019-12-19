function solution(bridge_length, weight, truck_weights) {
    var answer = 0, total = 0, truck = 0;
    var bridge = Array(bridge_length).fill(0);

    while (truck_weights.length) {
        ++answer;
        total -= bridge.shift();
        if (total + truck_weights[0] <= weight ) {
          truck = truck_weights.shift();
          bridge.push(truck);
          total += truck;
        } else {
          bridge.push(0);
        }
    };
    return answer+bridge.length;
}

var a1 = 2, a2 = 10, a3= [7,4,5,6];
var b1 = 100, b2 = 100, b3= [10];
var c1 = 100, c2 = 100, c3= [10,10,10,10,10,10,10,10,10,10];

console.log(solution(a1,a2,a3));
console.log(solution(b1,b2,b3));
console.log(solution(c1,c2,c3));
