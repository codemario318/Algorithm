package com.company;

import java.util.Scanner;

public class Main {

     public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int th = 1, n = 1;
        sc.close();

        while(th < N) {
            ++n;
            th += 6*(n-1);
        }
         System.out.println(n);
     }
}
