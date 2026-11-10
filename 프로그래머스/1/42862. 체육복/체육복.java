import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        
        int[] cnt = new int[n+2];
        Arrays.fill(cnt, 1);
        
        for(int i: lost) cnt[i] -= 1;
        for(int i: reserve) cnt[i] += 1;
        
        System.out.println(Arrays.toString(cnt));
        
        // 0부터 n까지 순회
        
        for (int i = 1; i <= n; i++) {
            if (cnt[i] == 0) {
                if (cnt[i - 1] == 2) {
                    cnt[i - 1]--; 
                    answer += 1;
                } else if (cnt[i + 1] == 2) {
                    cnt[i + 1]--;
                    answer += 1;
                }
            } else {
                answer += 1;
            }
        }

        
        
        // lost면? -> reverse에서 순회해서 있으면 거기서 빼기 answer += 1
        
        // lost에 없으면? -> answer += 1
        
        return answer;
    }
}