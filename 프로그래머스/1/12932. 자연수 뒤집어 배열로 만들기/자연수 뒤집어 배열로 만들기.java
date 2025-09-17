class Solution {
    public int[] solution(long n) {
        int nLength = (int)(Math.log10(n) + 1);
        int[] answer = new int[nLength];
        int num = 0;
        
        while (num < nLength) {
            answer[num] = (int)(n % 10);
            n /= 10;
            num++;
        }
        
        return answer;
    }
}