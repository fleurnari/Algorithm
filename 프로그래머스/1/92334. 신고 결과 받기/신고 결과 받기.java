import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Map<String, HashSet<String>> reportedMap = new HashMap<>();
        Map<String, Integer> resultMap = new HashMap<>();
        
        for (int i = 0; i < id_list.length; i++) {
            HashSet<String> reportSet = new HashSet<>();
            reportedMap.put(id_list[i], reportSet);
            resultMap.put(id_list[i], 0);
        }
        
        for (String s : report) {
            String reporter = s.split(" ")[0];
            String reported = s.split(" ")[1];
            reportedMap.get(reported).add(reporter);
        }
        
        for (String reported : reportedMap.keySet()) {
            HashSet<String> chk = reportedMap.get(reported);
            
            if (chk.size() >= k) {
                for (String s : chk) {
                    resultMap.put(s, resultMap.get(s) + 1);
                }
            }
            
        }
        
        for (int i = 0; i < id_list.length; i++) {
            answer[i] = resultMap.get(id_list[i]);
        }
        
        
        return answer;
    }
}