class Solution {
    public long solution(int price, int money, int count) {
        long answer = (long)money;
        int cnt = 1;
        
        while (cnt <= count) {
            answer -= (price * cnt);
            cnt++;
        }
        
        if (answer > 0) {
            answer = 0;
        } else {
            answer = Math.abs(answer);
        }
        
        return answer;
    }
}