package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

class Empty {
    int x;
    int y;

    public Empty(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int SIZE = 9;
    static int[][] board = new int[SIZE][SIZE];
    static ArrayList<Empty> emptys;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nums;
        int num;

        for (int i = 0; i <= SIZE; i++) {
            nums = br.readLine().split("\\s");
            for (int j = 0; j <= SIZE; j++) {
                Empty emt = new Empty(i,j);
                emptys.add(emt);
                board[i][j] = Integer.parseInt(nums[j]);
            }
        }
    }

    public static void sudoku() {
        for (Empty e: emptys) {

        }
    }

    public boolean checkCol(int n, int x) {
        for (int i = 0; i < SIZE; i++) {
            if (board[x][i] == n) return false;
        }
        return true;
    }

    public boolean checkRow(int n, int y) {
        for (int i = 0; i < SIZE; i++) {
            if (board[i][y] == n) return false;
        }
        return true;
    }

    public boolean checkSqr(int n, int x, int y) {
        int sx = (int)x/3 * 3;
        int sy = y/3;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[sx+i][sy+j] == n) return false;
            }
        }
        return true;
    }
}
