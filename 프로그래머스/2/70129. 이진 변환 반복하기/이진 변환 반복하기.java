import java.util.*;

class Solution {
    public int[] solution(String s) {
        int turnCnt = 0;
        int delCnt = 0;
        
        while (s.length() > 1) {
            String tmp = "";
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0') {
                    delCnt++;
                    continue;
                }
                tmp += s.charAt(i);
            }
            s = Integer.toBinaryString(tmp.length());
            turnCnt++;
        }
        
        return new int[] {turnCnt, delCnt};
    }
}