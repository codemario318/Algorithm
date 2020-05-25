function solution(participant, completion) {
    var runner = {};

    participant.map((name) => {
        if (runner.hasOwnProperty(name)) {
            runner[name]++;
        } else {
            runner[name] = 1;
        }
    });

    completion.map((name) => {
        runner[name]--;
    });

    for (var name in runner) {
        if (runner[name] > 0) {
            return name
        }
    };
}

console.log(solution(['leo', 'kiki', 'eden'],['eden', 'kiki']));
