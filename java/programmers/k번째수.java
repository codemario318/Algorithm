import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for (int i = 0; i < commands.length; i++) {
            int[] command = commands[i];
            int start = command[0] - 1;
            int end = command[1];
            int index = command[2] - 1;
            int[] slice = Arrays.copyOfRange(array, start, end);
            Arrays.sort(slice);
            answer[i] = slice[index];
        }

        return answer;
    }
}