function solution(answers) {
    const pNums = 3,
    patterns = {
        1:[ 1, 2, 3, 4, 5 ],
        2:[ 2, 1, 2, 3, 2, 4, 2, 5],
        3:[ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    };

    let res = [],
        max = 0;

    for (let i = 1; i <= pNums; i++) {
        let temp = getScore(patterns[i], answers);

        if (temp > max) {
            max = temp
            res = [i];
        } else if (temp === max) {
            res.push(i);
        }
    }
    return res;
}

function getScore(pattern,answers) {
    const pLen = pattern.length,
          aLen = answers.length;
    let res = 0;

    for (let i = 0;i < aLen; i++){
        let answer = pattern[i%pLen];

        if ( answers[i] === answer ) {
            res++;
        }
    }
    return res;
}

// console.log(solution([1,2,3,4,5]));
// console.log(solution([1,3,2,4,2]));
// console.log(solution([4]));
//
// let a = solution
// console.log(a.name);
// console.log(undefined == true);
// console.log('123'[0]);
console.log('12'.substr(parseInt('12'.length/2)-1,2));
console.log('12'.length/2);
