"""
단어 변환
제출 내역
문제 설명
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

제한사항
각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.
입출력 예
begin	target	words	return
"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0
입출력 예 설명
예제 #1
문제에 나온 예와 같습니다.

예제 #2
target인 "cog"는 words 안에 없기 때문에 변환할 수 없습니다.
"""

import java.util.*;

class State {
    final String word;
    final int step;

    State(String word, int step) {
        this.word = word;
        this.step = step;
    }
}

class Solution {
    public int solution(String begin, String target, String[] words) {
        List<String> wordList = Arrays.asList(words);

        if (!wordList.contains(target)) {
            return 0;
        }

        Queue<State> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.add(new State(begin, 0));
        visited.add(begin);

        while (!queue.isEmpty()) {
            State state = queue.poll();

            if (state.word.equals(target)) {
                return state.step;
            }

            wordList.stream()
                    .filter((word) -> !visited.contains(word))
                    .filter((word) -> calcDistance(state.word, word) == 1)
                    .forEach((word) -> {
                        visited.add(word);
                        queue.add(new State(word, state.step + 1));
                    });
        }

        return 0;
    }

    static int calcDistance(String begin, String target) {
        int count = 0;

        for (int i = 0; i < begin.length(); i++) {
            if (begin.charAt(i) != target.charAt(i)) {
                count++;
            }
        }

        return count;
    }
}