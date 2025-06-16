import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {0, 0});

        while(!queue.isEmpty()) {
            int[] state = queue.poll();
            int index = state[0];
            int total = state[1];

            if (index >= numbers.length) {
                if (total == target) {
                    answer++;
                }
            } else {
                queue.add(new int[] {index + 1, total + numbers[index]});
                queue.add(new int[] {index + 1, total - numbers[index]});
            }
        }

        return answer;
    }
}