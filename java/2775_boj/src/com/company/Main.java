package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = stoi(br.readLine());

        for (int i = 0; i < T; i++) {
            int k = stoi(br.readLine()), n = stoi(br.readLine());

        }

        br.close();
    }

    public static int stoi(String s){
        return Integer.parseInt(s);
    }
}

// k층, i호 단, 아파트는 0층부터 있고 각 층네는 1호부터 있다. -> 0층 i호에는 i명이 산다.
// k-1 층의 1 ~ i호 까지 사람들의 수의 합 만큼 사람들을 데려와 살아야한다.
// 1, 3 일경우 (0,1),(0,2),(0,3),(1,1),(1,2) 호에서 사는 사람들
//     1호 2호 3호
// 0층: 1, 2, 3, n
// 1층: 1, 3 , 6, n*(n+1)/2
// 2층: 1, 4, 10, n*(n+1)/2 + n*(n-1)/2
// 3층: 1, 5, 15
//     1, 6, 31