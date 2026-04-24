import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class SWEA_5644_무선충전 {
	
	// 문제를 잘 읽고 이 문제는 같은 배터리를 공유를 한다는 점이 핵심이다
	
	
	
	static class BC implements Comparable<BC> {
		int id; // 배터리를 고유하게 구분하기 위한 ID 추가
		int y, x, c, p;

		public BC(int id, int y, int x, int c, int p) {
			this.id = id;
			this.y = y;
			this.x = x;
			this.c = c;
			this.p = p;
		}

		@Override
		public int compareTo(BC o) {
			// 성능(p) 기준 내림차순 정렬
			return o.p - this.p; 
		}
	}
	
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	static int[] dyP = {0, -1, 0, 1, 0};
	static int[] dxP = {0, 0, 1, 0, -1};
	
	static PriorityQueue<BC>[][] bcMap;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=t; tc++) {
			st = new StringTokenizer(br.readLine());
			int M = Integer.parseInt(st.nextToken());
			int A = Integer.parseInt(st.nextToken());
			
			bcMap = new PriorityQueue[11][11];
			for(int i=1; i<11; i++) {
				for(int j=1; j<11; j++) {
					bcMap[i][j] = new PriorityQueue<>();
				}
			}
			
			int ay = 1, ax = 1;
			int by = 10, bx = 10;
			
			int[] pA = new int[M];
			int[] pB = new int[M];
			
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<M; i++) pA[i] = Integer.parseInt(st.nextToken());
			
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<M; i++) pB[i] = Integer.parseInt(st.nextToken());
			
			// 배터리 매설
			for(int i=0; i<A; i++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				int p = Integer.parseInt(st.nextToken());
				
				// 배터리의 고유 번호(i)를 함께 부여
				BC bc = new BC(i, y, x, c, p);
				bfs(y, x, c, bc);
			}
			
			int sum = 0;
			
			// 이동 전 0초(초기 위치)에서의 충전 처리
			sum += getCharge(ay, ax, by, bx);
			
			// 시작
			for(int i=0; i<M; i++) {
				ay += dyP[pA[i]];
				ax += dxP[pA[i]];
				by += dyP[pB[i]];
				bx += dxP[pB[i]];
				
				// 이동 후 위치에서의 충전 처리
				sum += getCharge(ay, ax, by, bx);
			}
			
			sb.append("#").append(tc).append(" ").append(sum).append("\n");
		}
		System.out.print(sb.toString());
	}
	
	// 두 사람의 위치에 있는 PQ에서 최적의 배터리 조합을 찾는 메서드 분리
	static int getCharge(int ay, int ax, int by, int bx) {
	    List<BC> listA = new ArrayList<>();
	    List<BC> listB = new ArrayList<>();
	    
	    // A와 B가 완전히 같은 칸에 있을 때의 예외 처리
	    if (ay == by && ax == bx) {
	        // 한쪽 큐에서만 최대 2개를 뽑고
	        while(!bcMap[ay][ax].isEmpty() && listA.size() < 2) {
	            listA.add(bcMap[ay][ax].poll());
	        }
	        // B는 A가 뽑은 배터리를 그대로 똑같이 참조(공유)합니다.
	        listB.addAll(listA); 
	    } else {
	        // 다른 칸이라면 각자의 큐에서 독립적으로 뽑습니다.
	        while(!bcMap[ay][ax].isEmpty() && listA.size() < 2) listA.add(bcMap[ay][ax].poll());
	        while(!bcMap[by][bx].isEmpty() && listB.size() < 2) listB.add(bcMap[by][bx].poll());
	    }
	    
	    int max = 0;
	    
	    if(listA.isEmpty() && listB.isEmpty()) max = 0;
	    else if(listB.isEmpty()) max = listA.get(0).p;
	    else if(listA.isEmpty()) max = listB.get(0).p;
	    else {
	        for(BC bcA : listA) {
	            for(BC bcB : listB) {
	                if(bcA.id == bcB.id) {
	                    max = Math.max(max, bcA.p);
	                } else {
	                    max = Math.max(max, bcA.p + bcB.p);
	                }
	            }
	        }
	    }
	    
	    // [수정된 부분] 다시 큐에 원상복구 할 때도 같은 칸인지 체크
	    if (ay == by && ax == bx) {
	        // 같은 칸이면 A의 리스트에 있는 것만 큐에 다시 넣어주면 됩니다.
	        for(BC bc : listA) bcMap[ay][ax].add(bc);
	    } else {
	        for(BC bc : listA) bcMap[ay][ax].add(bc);
	        for(BC bc : listB) bcMap[by][bx].add(bc);
	    }
	    
	    return max;
	}
	
	static void bfs(int y, int x, int w, BC bc) {
		Queue<int[]> q = new ArrayDeque<>();
		// 중복 추가 방지를 위한 visited 배열 사용
		boolean[][] visited = new boolean[11][11];
		
		q.add(new int[]{y, x});
		visited[y][x] = true;
		bcMap[y][x].add(bc);
		
		int dist = 0;
		while(!q.isEmpty() && dist < w) {
			int size = q.size();
			for(int i=0; i<size; i++) {
				int[] curr = q.poll();
				int r = curr[0];
				int c = curr[1];
				
				for(int d=0; d<4; d++) {
					int nr = r + dy[d];
					int nc = c + dx[d];
					
					// 맵을 벗어나거나 이미 이번 배터리가 방문한 곳이면 패스
					if(nr < 1 || nr >= 11 || nc < 1 || nc >= 11 || visited[nr][nc]) continue;
					
					visited[nr][nc] = true;
					bcMap[nr][nc].add(bc);
					q.add(new int[]{nr, nc});
				}
			}
			dist++;
		}
	}
}