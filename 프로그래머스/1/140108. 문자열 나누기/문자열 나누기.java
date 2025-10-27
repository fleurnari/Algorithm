class Solution {
    public int solution(String s) {
        int answer = 0;
        int cnt = 1;
        char beforeChr = s.charAt(0);
        
        for (int i = 1; i < s.length(); i++) {
            char nowChr = s.charAt(i);
            
            if (cnt == 0) {
                beforeChr = nowChr;
                cnt++;
                continue;
            }
            
            if (beforeChr == nowChr) {
                cnt++;
            } else {
                cnt--;
            }
            
            if (cnt == 0) {
                answer++;
            }
        }
        
        if (cnt != 0) {
            answer++;
        }
        
        return answer;
    }
}