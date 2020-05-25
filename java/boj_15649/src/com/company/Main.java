package com.company;

import static java.lang.System.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N, M;
    static int[] perm;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        String[] st = br.readLine().split(" ");

        N = stoi(st[0]);
        M = stoi(st[1]);

        perm = new int[M];
        visited = new boolean[N + 1];

        dfs(0);

        out.println(sb);
    }

    public static void dfs(int d) {
        if (d == M) {
            for (int p: perm ) sb.append(p).append(' ');
            sb.append('\n');
        } else {
            for (int i = 1; i <= N; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    perm[d] = i;
                    dfs(d+1);
                    visited[i] = false;
                }
            }
        }
    }

    public static int stoi (String s) {
        return Integer.parseInt(s);
    }
}
