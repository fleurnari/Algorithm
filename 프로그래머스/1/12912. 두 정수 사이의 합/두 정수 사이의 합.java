class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int minNum = a;
        int maxNum = b;
        
        if (a == b) {
            return a;
        }
        
        if (a > b) {
            minNum = b;
            maxNum = a;
        }
        
        for (int i = minNum; i <= maxNum; i++) {
            answer += (long)i;
        }
        
        
        return answer;
    }
}