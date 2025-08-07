const WORDS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

function solution(msg) {
    const answer = [];
    const wordCodes = new Map([...WORDS].map((w, i) => [w, i + 1]));

    const msgArray = [...msg];

    let prevWord = '';

    while (msgArray.length > 0) {
        const char = msgArray.shift();
        const word = `${prevWord}${char}`;

        if (wordCodes.has(word)) {
            prevWord = word;
        } else {
            wordCodes.set(word, wordCodes.size + 1);
            answer.push(wordCodes.get(prevWord));
            prevWord = char;
        }
    }

    answer.push(wordCodes.get(prevWord));

    return answer;
}