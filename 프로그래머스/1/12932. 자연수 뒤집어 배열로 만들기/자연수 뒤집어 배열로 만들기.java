class Solution {
    public int[] solution(long n) {
        int nLength = (int)(Math.log10(n) + 1);
        int[] answer = new int[nLength];
        
        for (int i = 0; i < nLength; i++) {
            answer[i] = (int)(n % 10);
            n /= 10;
        }
        
        return answer;
    }
}