class Solution {
    public String solution(int n) {
        String answer = "";
        int cnt = 1;
        
        while (cnt <= n) {
            if (cnt % 2 == 1) {
                answer += "수";
            } else {
                answer += "박";
            }
            cnt++;
        }
        
        return answer;
    }
}