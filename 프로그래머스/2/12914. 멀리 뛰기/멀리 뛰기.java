class Solution {
    public long solution(int n) {
        int[] dpTable = new int[2001];
        dpTable[1] = 1;
        dpTable[2] = 2;
        
        for (int i = 3; i < dpTable.length; i++) {
            dpTable[i] = (dpTable[i - 2] + dpTable[i - 1]) % 1234567;
        }
        
        return dpTable[n];
    }
}