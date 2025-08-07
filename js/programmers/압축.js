const WORDS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

function solution(msg) {
    const answer = [];
    const wordCodes = new Map([...WORDS].map((w, i) => [w, i + 1]));

    const msgArray = [...msg];

    let prevWord = '';
    let index = 0;

    while (index < msgArray.length) {
        const char = msgArray[index];
        const word = `${prevWord}${char}`;

        index++;

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