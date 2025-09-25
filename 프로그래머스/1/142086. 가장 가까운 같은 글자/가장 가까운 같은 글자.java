import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        Map<Character, Integer> map = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char chr = s.charAt(i);
            if (!map.containsKey(chr)) {
                answer[i] = -1;
                map.put(chr, i);
            } else {
                answer[i] = i - map.get(chr);
                map.put(chr, i);
            }
        }
        
        return answer;
    }
}