package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] words = new String[N];
        int count = 0;

        for (int i = 0; i < N; i++) words[i] = br.readLine();

        br.close();

        for (String word: words) if (checker(word)) count++;

        System.out.println(count);
    }

    public static boolean checker(String word){
        Map<Character, Boolean> wTemp = new HashMap<>();

        char cur, prev;
        prev = '!';

        for (int i = 0; i < word.length(); i++) {
            cur = word.charAt(i);

            if ( wTemp.containsKey(cur) && cur != prev) return false;

            wTemp.put(cur,true);
            prev = cur;
        }
        return true;
    }
}
