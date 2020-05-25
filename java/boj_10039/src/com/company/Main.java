package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int total = 0, num = 0;

        for (int i = 0; i < 5; i++) {
            num = Integer.parseInt(bf.readLine());
            total += (num >= 40) ? num : 40;
        }

        System.out.println(total/5);
    }
}
