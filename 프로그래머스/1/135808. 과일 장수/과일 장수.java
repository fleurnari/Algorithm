import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        
        Integer[] scoreDesc = Arrays.stream(score).boxed().toArray(Integer[]::new);
        Arrays.sort(scoreDesc, Collections.reverseOrder());
        
        for (int i = m - 1; i < scoreDesc.length; i += m) {
            answer += scoreDesc[i] * m;
        }
        
        return answer;
    }
}