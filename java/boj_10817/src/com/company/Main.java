package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> nums = new ArrayList<Integer>(3);

        for (String s: br.readLine().split("\\s")) {
            nums.add(Integer.parseInt(s));
        }
        nums.sort(null);
        System.out.println(nums.get(1));
        br.close();
    }
}
