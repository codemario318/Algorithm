package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] nums = new int[2];
        String  temp = "";
        String[] s = br.readLine().split("\\s");
        br.close();

        for (int i = 0; i < 2; i++) {
            for (int j = 2; j >= 0; j--) {
                temp += s[i].charAt(j);
            }
            nums[i] = Integer.parseInt(temp);
            temp = "";
        }
        System.out.println((nums[0] > nums[1]) ? nums[0] : nums[1]);
    }
}
