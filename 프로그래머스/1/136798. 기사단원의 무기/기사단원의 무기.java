import java.util.*;

class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        int div = 0;
        
        for (int i = 1; i <= number; i++) {
            div = divCnt(i);
            if (div > limit) {
                answer += power;
            } else {
                answer += div;
            }
        }
        
        return answer;
    }
    
    private int divCnt(int num) {
        int cnt = 0;
        
        for (int i = 1; i <= (int)Math.sqrt(num); i++) {
            if (num % i == 0) {
                cnt++;
                
                if (num / i != i) {
                    cnt++;
                }
            }
        }
        
        return cnt;
    }
}