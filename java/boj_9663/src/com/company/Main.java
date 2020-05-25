package com.company;

import java.util.Scanner;

public class Main {
    static int N;
    static boolean[][] board;
    static int count;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        board = new boolean[N][N];

        nQueen(0);

        System.out.println(count);
    }

    public static void nQueen(int n) {
        if (n == N) {
            count++;
        } else {
            for (int i = 0; i < N; i++) {
                if (checkQueen(n, i)) {
                    board[n][i] = true;
                    nQueen(n + 1);
                    board[n][i] = false;
                }
            }
        }
    }

    public static boolean checkQueen(int n, int m) {
        for (int i=1; i <= n; i++) {
            if (board[n-i][m]) return false;
            if (m >= i && board[n-i][m-i]) return false;
            if (m+i < N && board[n-i][m+i]) return false;
        }
        return true;
    }
}
