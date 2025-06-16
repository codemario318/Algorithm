package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int bugger = 2000, drink = 2000;

        for (int i = 0; i < 3; i++) {
            bugger = min(bugger, Integer.parseInt(bf.readLine()));
        }

        for (int i = 0; i < 2; i++) {
            drink = min(drink, Integer.parseInt(bf.readLine()));
        }
        System.out.println(bugger + drink - 50);
    }

    public static int min(int a, int b) {
        return (a < b) ? a : b;
    }
}
