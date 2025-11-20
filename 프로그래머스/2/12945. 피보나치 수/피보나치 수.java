class Solution {
    public int solution(int n) {
        int[] dpTable = new int[n + 1];
        dpTable[0] = 0;
        dpTable[1] = 1;
        
        for (int i = 2; i < dpTable.length; i++) {
            dpTable[i] = (dpTable[i - 1] + dpTable[i - 2]) % 1234567;
        }
        
        return dpTable[n] % 1234567;
    }
}