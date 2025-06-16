package com.company;

import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        int cnt = 0;

        for(String runner: participant) {
            map.put(runner, map.getOrDefault(runner, 0) + 1);
        }

        for(String goaler: completion) {
            cnt = map.get(goaler) - 1;
            if (cnt == 0) {
                map.remove(goaler);
            } else {
                map.replace(goaler, cnt);
            }
        }

        return (String) map.keySet().toArray()[0];
    }
}