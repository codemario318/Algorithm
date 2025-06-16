package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        // A + (n*B) < (n*C) but, (C > B)
        // A < n(C-B) == A/(C-B) = n
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split("\\s");

        int fc = stoi(s[0]), vc = stoi(s[1]), rev = stoi(s[2]);
        br.close();

        System.out.println( (vc >= rev) ? -1 : (fc/(rev-vc))+1 );
    }

    public static int stoi(String s) {
        return Integer.parseInt(s);
    }
}
