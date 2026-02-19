import java.util.Scanner;



public class SWEA_1216_회문2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		StringBuilder sb2 = new StringBuilder();
		
		for(int tc=0; tc<10; tc++) {
			int t = Integer.parseInt(sc.nextLine());
			String[] list = new String[100];
			String[] list2 = new String[100];
			
			String[] list3 = new String[100];
			String[] list4 = new String[100];

			
			int max=0;
			
			//가로 map
			for(int i =0; i<100; i++) {
				list[i] = sc.nextLine();
				list2[i] = sb.append(list[i]).reverse().toString();
			}
			
			for(int i=0; i<100; i++) {
				String T = list[i];
				String P = list2[i];
				int N = T.length();
				
				boolean find=false;
				
				for(int r=0; r<100; r++) {
					for(int c=0; c<r+1; c++) {
						String p = P.substring(c, 100-r+c);
						int M = p.length();
						
						
						for(int k=0; k<N-M+1; k++) {
							int cnt = 0;
							for(int j=0; j<M; j++) {
								if(p.charAt(j) == T.charAt(j+k)) {
									cnt++;
								}else break;
							}
							if(cnt == M) {
								find = true;
								if(max < cnt) max=cnt;
								break;
							}
						}// t시작지점을 결정한 for문
						if(find)break;
					}//c for
				}//r for
			}
			
			
			//세로 map
			for(int j =0; j<100; j++) {
				//null값제외
				list3[j] = "";
				for(int i=0; i<100; i++) {
					//정방향 배열
					list3[j] += list[i].charAt(j);
				}
				list4[j] = sb2.append(list3[j]).reverse().toString();
			}
			
			for(int i=0; i<100; i++) {
				String T = list3[i];
				String P = list4[i];
				int N = T.length();
				
				boolean find=false;
				
				for(int r=0; r<100; r++) {
					for(int c=0; c<r+1; c++) {
						String p = P.substring(c, 100-r+c);
						int M = p.length();
						
						
						for(int k=0; k<N-M+1; k++) {
							int cnt = 0;
							for(int j=0; j<M; j++) {
								if(p.charAt(j) == T.charAt(j+k)) {
									cnt++;
								}else break;
							}
							if(cnt == M) {
								find = true;
								if(max < cnt) max=cnt;
								break;
							}
						}// t시작지점을 결정한 for문
						if(find)break;
					}//c for
					if(find)break;
				}//r for
			}
			
			System.out.println("#"+t+" "+max);
		}
	}

}
