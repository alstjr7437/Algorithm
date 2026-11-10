import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        int[] dx = {0,0,-1,1};
        int[] dy = {1,-1,0,0};
        
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;
        
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        
        queue.offer(new int[]{0, 0, 1});
        
        while(!queue.isEmpty()){
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            
            if (x == n - 1 && y == m - 1) return current[2];
            
            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if(nx >= n || nx < 0 || ny >= m || ny < 0) continue;
                
                if(visited[nx][ny] || maps[nx][ny] == 0) continue;
                
                visited[nx][ny] = true;
                queue.offer(new int[]{nx, ny, current[2] + 1});  
            }
        }
        
        return -1;
    }
}