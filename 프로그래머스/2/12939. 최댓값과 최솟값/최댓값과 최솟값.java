import java.util.*;

class Solution {
    public String solution(String s) {
        String[] strArr = s.split(" ");
        int minNum = Integer.parseInt(strArr[0]);
        int maxNum = Integer.parseInt(strArr[0]);
        
        for (int i = 1; i < strArr.length; i++) {
            int arrNum = Integer.parseInt(strArr[i]);
            if (arrNum < minNum) {
                minNum = arrNum;
            } else if (arrNum > maxNum) {
                maxNum = arrNum;
            }
        }
        
        return minNum + " " + maxNum;
    }
}