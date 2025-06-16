import java.util.*;

class Solution {
    private int[] parents;

    public int solution(int n, int[][] computers) {
        parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && computers[i][j] == 1) {
                    union(i, j);
                }
            }
        }

        Set<Integer> rootSet = new HashSet<>();
        for (int i = 0; i < n; i++) {
            rootSet.add(find(i));
        }

        return rootSet.size();
    }

    private void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA != rootB) {
            parents[rootB] = rootA;
        }
    }

    private int find(int x) {
        if (parents[x] != x) {
            parents[x] = find(parents[x]);
        }
        return parents[x];
    }
}
