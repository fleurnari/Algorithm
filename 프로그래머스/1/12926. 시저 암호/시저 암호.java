class Solution {
    public String solution(String s, int n) {
        String answer = "";
        
        for (int i = 0; i < s.length(); i++) {
            char chr = s.charAt(i);
            
            if (chr == ' ') {
                answer += chr;
                continue;
            }
            
            if (chr >= 'a' && chr <= 'z') {
                if (chr + n > 'z') {
                    answer += (char)(chr - 26 + n);
                } else {
                    answer += (char)(chr + n);
                }
            } else {
                if (chr + n > 'Z') {
                    answer += (char)(chr - 26 + n);
                } else {
                    answer += (char)(chr + n);
                }
            }
         
        }
        
        return answer;
    }
}