import java.util.Arrays;
import java.util.Scanner;
import java.util.Set;

public class SWEA_1210_Ladder1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int tc=0; tc<10; tc++) {
			int t = sc.nextInt();
			int[][] map = new int[100][100];
			
			//map
			for(int i=0; i<100; i++) {
				for(int j=0; j<100; j++) {
					map[i][j] = sc.nextInt();
				}//j
			}//i
			
			//p

			
			//game start
			//시작 지점
			int[] start_x = map[0];
			
			
//			for(int n=0; n<start_x.length; n++) {
//				if(start_x[n] == 1) {
//					System.out.println(n);
//				}
//			}
			
			for(int i=0; i<start_x.length; i++) {
				// 시작 지점 찾음
				if(start_x[i] == 1) {
					int[] p = {0,0};
					
					// 게임시작
					p[1] = i;
//					System.out.println("게임시작"+i);
					while(p[0] < 99) {
						
						
						if(p[0] == 0) {
							p[0] += 1;
//							System.out.println("일단 내려가");
						}
						//맵 좌측 끝부분
						if(p[1]==0) {
							// 우측 공간 존재
							if(map[p[0]][p[1]+1] == 1) {
								while(map[p[0]][p[1]+1] != 0 && p[1]+1 <99) {
									p[1] += 1;
	//								System.out.println("좌측끝 우측공간");
								}
								p[0] +=1;
							// 없는 경우 다운
							}else {
								p[0] += 1;
	//							System.out.println("좌측끝 다운");
							}
							
						// 맵 우측 끝부분	
						}else if(p[1] == 99) {
							//좌측 공간 존재
							if(map[p[0]][p[1]-1] == 1) {
								while(map[p[0]][p[1]-1] != 0 && p[1]-1 >=0) {
									p[1] -= 1;
	//								System.out.println("우측끝 좌측공간");
								}
								p[0] +=1;
								
							//없는 경우 다운	
							}else {
								p[1] -= 1;
//								System.out.println("우측끝 다운");
							}
						}
						
						
						// 맵중간
						if(p[1]-1 >= 0 && p[1]+1 <100) {
							
							//왼쪽에 공간
							if(map[p[0]][p[1]-1] == 1 && map[p[0]][p[1]] == 1) {
								while(map[p[0]][p[1]-1] == 1 && (p[1]-1) > 0) {
									p[1] --;
//									System.out.println("맵중간 좌측");
								}
								if(p[1] == 1) p[1] = 0;
								p[0] +=1;
//								System.out.println("맵좌"+p[0]+" "+p[1]);
							
							//오른쪽에 공간
							}else if(map[p[0]][p[1]+1] == 1) {
								while(map[p[0]][p[1]+1] != 0 && p[1]+1 <99) {
									p[1] += 1;
	//								System.out.println("맵중간 우측");
								}
								if(p[1] == 98) p[1] = 99;
								p[0] +=1;
							//어느곳에도 공간 없음 다운
							}else {
								p[0] += 1;
	//							System.out.println("맵중간 공간없어");
							}
						}
												
						
						
						
					}//while
					
				if(map[p[0]][p[1]] == 2) {
					System.out.println("#"+t+" "+i);
					break;
				}
					
				}
			}
			
			
			
		}//tc
	}
}
