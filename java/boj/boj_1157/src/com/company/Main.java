package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().toUpperCase();
        br.close();

        Map<Character, Integer> alphabets = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (alphabets.containsKey(c)) {
                alphabets.put(c,alphabets.get(c)+1);
            } else {
                alphabets.put(c,1);
            }
        }

        List keyList = new ArrayList<>(alphabets.keySet());
        Collections.sort(keyList, (o1, o2) -> (alphabets.get(o2).compareTo(alphabets.get(o1))));

        if (keyList.size() < 2) {
            System.out.println(keyList.get(0));
        } else {
            int a = alphabets.get(keyList.get(0));
            int b = alphabets.get(keyList.get(1));

            System.out.println((a == b) ? "?": keyList.get(0));
        }
    }
}

//class Alphabet implements Comparable<Alphabet> {
//    char apbt;
//    int count;
//
//    public Alphabet(char c){
//        this.apbt = c;
//        this.count = 0;
//
//    }
//
//    public int getCode() {
//        return this.apbt;
//    }
//
//    @Override
//    public int compareTo(Alphabet o) {
//        return this.count - o.count;
//    }
//}
