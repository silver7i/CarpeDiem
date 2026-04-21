import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class BOJ_1238_파티 {
	static class Edge implements Comparable<Edge>{
		int to, cost;

		public Edge(int to, int cost) {
			this.to = to;
			this.cost = cost;
		}
		
		@Override
		public int compareTo(Edge o) {
			// TODO Auto-generated method stub
			return this.cost - o.cost;
		}
	}
	
	static final int INF = Integer.MAX_VALUE;
	
	static List<Edge>[] edge;
	static int[] dist;
			
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int x = Integer.parseInt(st.nextToken());
		
		edge = new ArrayList[n+1];
		dist = new int[n+1];
		
		for(int i=1; i<=n; i++) {
			edge[i] = new ArrayList<>();
		}
		
		for(int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			
			edge[from].add(new Edge(to, cost));
		}
		
		int[] target = new int[n+1];
		
		for(int i=1; i<=n; i++) {
			Arrays.fill(dist, INF);
			
			if(i == x) {
				dijkstra(i);
				for(int j=1; j<=n; j++) {
					target[j] += dist[j];
				}
			}
			else {
				dijkstra(i);
				target[i] += dist[x];
			}
		}
		int max = 0;
		for(int i=1; i<=n; i++) {
			if(max < target[i]) max = target[i];
		}
		
		System.out.println(max);
	}
	
	static void dijkstra (int start) {
		
		//우선순위 큐 및 시작
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		pq.add(new Edge(start, 0));
		dist[start] = 0;
		
		while(!pq.isEmpty()) {
			//가장 거리가 가장 짧은 친구 꺼내기
			
			Edge current = pq.poll();
			
			//dist배열에 저장된 거리가 지금 거리보다 짧은 경우
			if(dist[current.to] < current.cost) continue;
			
			//현재 간선과 인접한 간선확인
			for(Edge e : edge[current.to]) {
				
				int cost = dist[current.to] + e.cost;
				
				//더 짧은 경로를 발견한 경우 업데이트
				if(cost < dist[e.to]) {
					dist[e.to] = cost;
					pq.add(new Edge(e.to, cost));
				}
			}
		}
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
}
