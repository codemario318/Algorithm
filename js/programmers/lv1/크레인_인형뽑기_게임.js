function solution(board, moves) {
    const N = board.length - 1;
    let stack = [],
        res = 0;

    for ( const n of moves ) {
        const p = n-1,
              last = stack[stack.length-1];
        let next = grap( board, p );
        // console.log(last,next);
        if ( next === 0 ) {
            continue;
        } else if ( last === next ) {
            stack.pop();
            res += 2;

        } else {
            stack.push(next);
        }
    }
    return res;
}

function grap(board,x) {
    const N = board.length;
    let res = 0;

    for ( let i = 0; i < N; i++ ) {
        if ( board[i][x] !== 0 ) {
            res = board[i][x];
            board[i][x] = 0;
            break;
        }
    }
    return res;
}

const board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
        moves = [1,5,3,5,1,2,1,4];

console.log(solution(board,moves));
