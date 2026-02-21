/*
BFS(Breadth-First-Search: 너비 우선 탐색)
횡의 방향으로 하는 완전 탐색을 의미함
큐를 사용하는 완전 탐색 방법

1. 시작 노드를 큐에 저장
2. 맨 앞의 값을 꺼냄
3. 문제에서 요구하는 연산을 수행
4. 인접 노드를 큐에 저장
5. 탐색이 끝난 노드를 버림
6. 다음 노드를 꺼내서 큐가 빌 때 까지 2~6번까지의 과정을 반복

### 반드시 visited를 사용해서 방문한 노드를 표시해준다.


 */
import java.util.LinkedList;
import java.util.Queue;

public class BFS연습 {
	public static void main(String[] args) {
		
	    String[][] map = { 
                { "S", "0", "0", "0", "W", "0", "W" }, 
                { "W", "0", "W", "0", "0", "0", "0" },
                { "0", "0", "0", "W", "0", "W", "0" }, 
                { "0", "W", "W", "0", "0", "0", "0" },
                { "0", "0", "W", "W", "0", "W", "W" }, 
                { "W", "0", "W", "0", "0", "0", "0" },
                { "0", "0", "0", "W", "0", "0", "G" } };
	    
	    //미로탈출
	    Queue<Integer> p = new LinkedList<>();
	    p.add(0); //시작점 x좌표
	    p.add(0); //시작점 y좌표
	    int[][] visited = new int[map.length][map[0].length];
	    
	    int row = map.length;
	    int col = map[0].length;
	    
	    visited[0][0] = 1;
	    int cnt = 0;
	    
	    while(!p.isEmpty()) {
	    	int x = p.poll();
	    	int y = p.poll();
	    	
	    	if(x-1 >= 0) {
	    		if(!"W".equals(map[x-1][y]) && visited[x-1][y] == 0) {
	    			p.add(x-1);
	    			p.add(y);
	    			visited[x-1][y] = visited[x][y] + 1;
	    		}
	    	}
	    	
	    	if(x+1 < col) {
	    		if(!"W".equals(map[x+1][y]) && visited[x+1][y] == 0) {
	    			p.add(x+1);
	    			p.add(y);
	    			visited[x+1][y] = visited[x][y] + 1;
	    		}
	    	}
	    	
	    	if(y-1 >= 0) {
	    		if(!"W".equals(map[x][y-1]) && visited[x][y-1] == 0) {
	    			p.add(x);
	    			p.add(y-1);
	    			visited[x][y-1] = visited[x][y] + 1;
	    		}
	    	}
	    	
	    	if(y+1 < row) {
	    		if(!"W".equals(map[x][y+1]) && visited[x][y+1] == 0) {
	    			p.add(x);
	    			p.add(y+1);
	    			visited[x][y+1] = visited[x][y] + 1;
	    		}
	    	}
	    	
	    	
	    	
	    	
	    }
	    
	    cnt = visited[row-1][col-1];
	    
	    System.out.println(cnt);
	    
		
	}
}
