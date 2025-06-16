package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split("\\s");
        br.close();

        double A = stod(s[0]), B = stod(s[1]), V = stod(s[2]);
        int res = (int) (Math.ceil((V-A)/(A-B)) + 1);

        System.out.println(res);
    }

    public static double stod(String s) {
        return Double.parseDouble(s);
    }
}
