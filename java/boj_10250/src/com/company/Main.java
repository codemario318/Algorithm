package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = stoi(br.readLine());
        String[] s;

        for (int i = 0; i < n; i++) {
            s = br.readLine().split("\\s");
            System.out.println(ACMHotel(stoi(s[0]),stoi(s[2])));
        }

        br.close();
    }

    public static String ACMHotel(int height, int num) {
        int floor = num%(height);
        int line = (int) Math.ceil((double) num/ (double) height);

        if (floor == 0) floor = height;

        if (line < 10) {
            return floor + "0" + line;
        } else {
            return floor + "" + line;
        }
    }

    public static int stoi(String s) {
        return Integer.parseInt(s);
    }
}

//3
//6 12 10
//30 50 72
//1 99 98
