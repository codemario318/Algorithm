package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        int[] numCost = {3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10};
        int time = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int c:br.readLine().toCharArray()) time += numCost[c - 65];

        br.close();

        System.out.println(time);
    }
}
