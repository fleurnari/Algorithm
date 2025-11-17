import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < players.length; i++) {
            map.put(players[i], i);
        }
        
        for (String player : callings) {
            int idx = map.get(player);
            String front = players[idx - 1];
            
            players[idx - 1] = player;
            players[idx] = front;
            
            map.put(player, idx - 1);
            map.put(front, idx);
            
        }
        
        return players;
    }
}