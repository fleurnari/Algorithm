import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] sArr = s.split("");
        Arrays.sort(sArr, Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();
        
        for (String str : sArr) {
            sb.append(str);
        }
        
        answer = sb.toString();
        
        return answer;
    }
}