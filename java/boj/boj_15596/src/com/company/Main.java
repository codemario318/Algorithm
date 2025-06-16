package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
	// write your code here
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s;
        s = br.readLine();
        s.charAt(0);
        System.out.println(s.length());

    }

    public class Test {
        long sum(int[] a) {
            long ans = 0;

            for (int i = 0; i < a.length; i++) {
                ans += a[i];
            }

            return ans;
        }
    }
}
