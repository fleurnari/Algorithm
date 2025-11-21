import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Map<Integer, Integer> tanMap = new HashMap<>();
        
        for (int i : tangerine) {
            tanMap.put(i, tanMap.getOrDefault(i, 0) + 1);
        }
        
        List<Integer> keyList = new ArrayList<>(tanMap.keySet());
        keyList.sort(((a, b) -> tanMap.get(b) - tanMap.get(a)));
        
        for (Integer i : keyList) {
            if (k <= 0) {
                break;
            }
            answer++;
            k -= tanMap.get(i);
        }
        
        return answer;
    }
}