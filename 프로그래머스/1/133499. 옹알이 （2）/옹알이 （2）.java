class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] strList = {"aya", "ye", "woo", "ma"};
        String[] impossible = {"ayaaya", "yeye", "woowoo", "mama"};
        
        for (String str : babbling) {
            for (String chk : impossible) {
                str = str.replace(chk, "X"); 
            }
            
            for (String chk : strList) {
                str = str.replace(chk, "O");
            }
            
            int chk = 0;
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) != 'O') {
                    chk++;
                    break;
                }
            }
            
            if (chk == 0) {
                answer++;
            }
            
        }
        
        return answer;
    }
}