import java.util.*;

class Solution {
    public int[] solution(String[] park, String[] routes) {
        char[][] arr = new char[park.length][park[0].length()];
        int x = 0;
        int y = 0;
        
        for (int i = 0; i < park.length; i++) {
            arr[i] = park[i].toCharArray();
            
            if (park[i].contains("S")) {
                x = park[i].indexOf('S');
                y = i;
            }
        }
        
        for (String route : routes) {
            String direct = route.split(" ")[0];
            int dist = Integer.parseInt(route.split(" ")[1]);
            int nx = x;
            int ny = y;
            
            for (int i = 0; i < dist; i++) {
                switch (direct) {
                    case "E":
                        nx++;
                        break;
                    case "W":
                        nx--;
                        break;
                    case "S":
                        ny++;
                        break;
                    default:
                        ny--;
                        break;
                }
                
                if (nx >= 0 && nx < arr[0].length && ny >= 0 && ny < arr.length) {
                    if (arr[ny][nx] == 'X') {
                        break;
                    }
                    
                    if (i == dist - 1) {
                        x = nx;
                        y = ny;
                    }
                }
            }
        }
        
        
        return new int[]{y, x};
    }
}