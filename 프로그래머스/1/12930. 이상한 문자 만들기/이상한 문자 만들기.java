class Solution {
    public String solution(String s) {
        String answer = "";
        String[] strArr = s.split("");
        int idx = 0;
        
        for (int i = 0; i < strArr.length; i++) {
            if (strArr[i].equals(" ")) {
                idx = 0;
            } else {
                if (idx % 2 == 0) {
                    idx++;
                    strArr[i] = strArr[i].toUpperCase();
                } else {
                    idx++;
                    strArr[i] = strArr[i].toLowerCase();
                }
            }
            answer += strArr[i];
        }
        
        return answer;
    }
}