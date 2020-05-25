function solution(N, number) {
    const LMT = 8,
          mem = {
              0: new Set(),
          };
    let ns = '';

    for (let i = 1; i <= LMT; i++) {
        const temp = new Set();
        ns += N;
        temp.add(ns);

        for (let j = 0; j < i; j++) {

        }
    }
}

function getNums( arr1 ) {

}

// console.log(solution(5,12));
// console.log( parseStr(5) * 10 );

// var mem = {};
//
// function solution(N, number) {
//     let ns = '',
//         res = 0;
//
//     for (let i = 1; i < 10; i++) {
//         ns += N;
//         mem[ns] = i;
//     }
//
//     if ( mem[1] !== 1 ) {
//         mem[1] = 2;
//     }
//
//     res = dp(N,number);
//
//     if ( res < 8 ) {
//         return res
//     } else {
//         return -1
//     }
// }
//
// function dp(N, number) {
//     console.log(mem)
//     if ( mem.hasOwnProperty(number) ) {
//         return mem[number]
//     } else {
//         const minCount = Math.min(
//             dp( N, number - N ),
//             dp( N, number + N ),
//             dp( N, number * N ),
//             dp( N, parseInt(number / N) )
//         );
//         if ( minCount > 7)  {
//             mem[number] = Infinity;
//         } else {
//             mem[number] = maxVal + 1;
//         }
//         return mem[number]
//     }
// }
