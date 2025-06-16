package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    // 1/1
    // 1/2, 2/1
    // 3/1, 2/2, 1/3
    // 1/4, 2/3, 3/2, 4/1
    // 5/1, 4/2, 3/3, 2/4, 1/5
    // 1, 3, 6, 10, 15, 21
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());
        br.close();

        int n = 1;
        int total = 1;
        while (X > total){
            ++n;
            total += n;
        }

        int seq = X - ((n*(n-1))/2);

        if (n%2 == 0) {
            System.out.println(seq+"/"+(n+1-seq));
        } else {
            System.out.println((n+1-seq)+"/"+(seq));
        }
    }
}
