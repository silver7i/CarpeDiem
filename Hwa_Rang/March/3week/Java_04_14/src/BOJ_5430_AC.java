import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class BOJ_5430_AC {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        
        for(int tc=0; tc<t; tc++) {
            String cmd = br.readLine();
            int len = Integer.parseInt(br.readLine());
            
            String[] text = br.readLine().replace('[', ' ').replace(']', ' ').trim().split(",");
            
            ArrayDeque<String> dq = new ArrayDeque<>();
            
            for(int i=0; i<text.length; i++) { 	
            	dq.add(text[i]);
            }
            
            int rCnt = 0;
            int dCnt = 0;
            for(int i=0; i<cmd.length(); i++) {
            	if(cmd.charAt(i) == 'R') rCnt++;
            	else {
            		dCnt++;
            		if(rCnt%2 != 0)dq.pollLast();
            		else dq.pollFirst();
            	}
            }
            
            if(len < dCnt) {
            	System.out.println("error");
            }
            else {
            	if(dq.isEmpty()) {
            		System.out.println("[]");
            	}
            	
            	else if(rCnt % 2 != 0) {
            		System.out.print('[');
            		int size = dq.size();
            		for(int i=0; i<size; i++) {
            			if(i == size-1)System.out.println(dq.pollLast()+"]");
            			else System.out.print(dq.pollLast()+',');
            		}
            	}
            	
            	else {
            		System.out.print('[');
            		int size = dq.size();
            		for(int i=0; i<size; i++) {
            			if(i == size-1)System.out.println(dq.pollFirst()+"]");
            			else System.out.print(dq.pollFirst()+',');
            		}
            	}
            }
            
            
        }
    }
}
