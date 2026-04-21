import java.net.*;
import java.io.*;
import java.util.*;

public class Main {
    /////////////////////////////////
    // 메인 프로그램 통신 변수 정의
    /////////////////////////////////
    private static final String HOST = "70.12.60.55"; // 사용자 IP
    private static final int PORT = 8747;
    private static String ARGS = "";
    private static Socket socket = null;

    ///////////////////////////////
    // 입력 데이터 변수 정의
    ///////////////////////////////
    private static String[][] mapData; 
    private static Map<String, String[]> myAllies = new HashMap<>(); 
    private static Map<String, String[]> enemies = new HashMap<>(); 
    private static String[] codes; 
    
    // 델타 배열 (상하좌우)
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};
    
    // 명령어 모음
    static String[] MOVE_CMDS = {"U A", "D A", "L A", "R A"};
    static String[] FIRE_CMDS = {"U F", "D F", "L F", "R F"};
    static String[] MEGA_FIRE_CMDS = {"U F M", "D F M", "L F M", "R F M"};
    
    static String START_SYMBOL = "M";
    static String TARGET_SYMBOL = "X";
    static String WALL_SYMBOL = "R";
    static String WATER_SYMBOL = "W";
    static String TREE_SYMBOL = "T";
    static String ITEM_SYMBOL = "F";
    
    public static void main(String[] args) {
        ARGS = args.length > 0 ? args[0] : "";
        
        String NICKNAME = "서울15_박화랑"; // 닉네임
        String gameData = init(NICKNAME);
        
        Queue<String> actions = new ArrayDeque<>();

        parseData(gameData);
        
        boolean isFarming = false; 
        
        // 반복문: 메인 프로그램 <-> 클라이언트 간 순차로 데이터 송수신
        while (gameData != null && gameData.length() > 0) {
            printData(gameData);
            String output = "S"; // 기본값 제자리 대기(Stay)

            int megaCount = myAllies.containsKey("M") ? Integer.parseInt(myAllies.get("M")[3]) : 0;

            // 내 탱크의 현재 위치 파악 (위협 감지 레이더용)
            int[] me = null;
            for (int r = 0; r < mapData.length; r++) {
                for (int c = 0; c < mapData[0].length; c++) {
                    if (mapData[r][c].equals("M")) {
                        me = new int[]{r, c};
                        break;
                    }
                }
            }

            // 내 탱크의 현재 체력 및 일반포탄 개수 파악
            int myHp = myAllies.containsKey("M") ? Integer.parseInt(myAllies.get("M")[0]) : 0;
            int normalCount = myAllies.containsKey("M") ? Integer.parseInt(myAllies.get("M")[2]) : 0;

            // 💡 [스마트 방어 로직 적용]
            if (megaCount == 0) {
                isFarming = true;
            } else if (megaCount >= 4) {
                isFarming = false;
            } else if (isFarming && isEnemyInSight(mapData, me)) {
                // 적이 시야에 들어왔을 때의 판단!
                if (myHp <= 70 && (megaCount > 0 || normalCount > 0)) {
                    isFarming = false; 
                } else if (megaCount >= 2) {
                    isFarming = false;
                }
            }

            // 행동 결정
            if (isFarming && codes != null && codes.length > 0 && !codes[0].trim().equals("0") && codes[0].trim().length() > 1) {
                String decoded = decodeCaesar(codes[0].trim(), 9); 
                output = "G " + decoded;
            } else {
                int[][] positions = findPositions(mapData, isFarming);
                int[] start = positions[0];
                int[] target = positions[1];
                
                actions = (start != null && target != null) ? dijkstra(mapData, start, target) : new ArrayDeque<>();
                output = actions.isEmpty() ? "S" : actions.poll();
            }

            gameData = submit(output);
            if (gameData != null && gameData.length() > 0) {
                parseData(gameData);
            }
        }
        
        close();
    }

    // ====================================================================
    // 아군 판별 메서드 (M1~M3, H)
    // ====================================================================
    private static boolean isAlly(String symbol) {
        return symbol.equals("H") || symbol.equals("M1") || symbol.equals("M2") || symbol.equals("M3");
    }

    // ====================================================================
    // 💡 [수정됨] 아군 포탑(H) 및 적군 포탑(X)의 3x3 접근 금지 구역 판별
    // ====================================================================
    private static boolean isInTurretZone(String[][] grid, int r, int c) {
        int rows = grid.length;
        int cols = grid[0].length;
        
        // 현재 칸(r, c)을 기준으로 주변 3x3(자신 포함 9칸)을 스캔
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                int nr = r + i;
                int nc = c + j;
                // 맵 범위를 벗어나지 않는다면
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                    // 아군 포탑(H)과 적군 포탑(X) 모두 진입 금지 구역으로 설정!
                    if (grid[nr][nc].equals("H") || grid[nr][nc].equals(TARGET_SYMBOL)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    // ====================================================================
    // 사거리 내 적 감지 레이더 메서드
    // ====================================================================
    private static boolean isEnemyInSight(String[][] grid, int[] start) {
        if (start == null) return false;
        int r = start[0];
        int c = start[1];
        
        for (int d = 0; d < 4; d++) {
            for (int p = 1; p <= 3; p++) {
                int nr = r + dy[d] * p;
                int nc = c + dx[d] * p;
                
                if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length) break;
                
                String cell = grid[nr][nc];
                if (cell.equals(WALL_SYMBOL) || cell.equals(ITEM_SYMBOL) || cell.equals(TREE_SYMBOL) || isAlly(cell)) break;
                if (cell.equals(TARGET_SYMBOL) || cell.startsWith("E")) return true;
            }
        }
        return false;
    }

    // 특정 기호의 위치 찾기 (파밍 모드에 따라 타겟 변경)
    private static int[][] findPositions(String[][] map, boolean isFarming) {
        int rows = map.length;
        int cols = map[0].length;
        
        int[] start = null;
        List<int[]> supplyList = new ArrayList<>(); 
        List<int[]> enemyList = new ArrayList<>(); 

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (map[row][col].equals(START_SYMBOL)) {
                    start = new int[]{row, col};
                } else if (map[row][col].equals(ITEM_SYMBOL)) {
                    supplyList.add(new int[]{row, col});
                } else if (map[row][col].equals(TARGET_SYMBOL) || map[row][col].startsWith("E")) {
                    enemyList.add(new int[]{row, col});
                }
            }
        }

        // 파밍 모드일 때 가장 가까운 보급시설 찾기
        if (isFarming && !supplyList.isEmpty() && start != null && myAllies.containsKey("M")) {
            int[] targetSupply = null;
            int minDistance = Integer.MAX_VALUE;
            for (int[] supplyPos : supplyList) {
                int dist = Math.abs(start[0] - supplyPos[0]) + Math.abs(start[1] - supplyPos[1]);
                if (dist < minDistance) {
                    minDistance = dist;
                    targetSupply = supplyPos;
                }
            }
            return new int[][]{start, targetSupply};
        }

        // 전투 모드(!isFarming)이거나 보급시설이 없으면 가장 가까운 적에게 이동!
        int[] target = null;
        if (start != null && !enemyList.isEmpty()) {
            int minDistance = Integer.MAX_VALUE;
            for (int[] enemyPos : enemyList) {
                int dist = Math.abs(start[0] - enemyPos[0]) + Math.abs(start[1] - enemyPos[1]);
                if (dist < minDistance) {
                    minDistance = dist;
                    target = enemyPos;
                }
            }
        }

        return new int[][]{start, target};
    }

    // 다익스트라 알고리즘
    private static Queue<String> dijkstra(String[][] grid, int[] start, int[] target) {
        int rows = grid.length;
        int cols = grid[0].length;
        
        PriorityQueue<DijkstraNode> pq = new PriorityQueue<>();
        int[][] minCost = new int[rows][cols];
        for (int[] row : minCost) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        
        pq.offer(new DijkstraNode(start[0], start[1], 0, new ArrayDeque<>()));
        minCost[start[0]][start[1]] = 0;

        while (!pq.isEmpty()) {
            DijkstraNode current = pq.poll();
            int r = current.row;
            int c = current.col;
            int currentCost = current.cost;
            Queue<String> actions = current.actions;
            
            if (currentCost > minCost[r][c]) continue;
            
            if (grid[target[0]][target[1]].equals(ITEM_SYMBOL)) {
                if (Math.abs(r - target[0]) + Math.abs(c - target[1]) == 1) {
                    return actions; 
                }
            } else {
                for (int d = 0; d < 4; d++) {
                    for (int p = 1; p <= 3; p++) {
                        int nr = r + dy[d] * p;
                        int nc = c + dx[d] * p;
                        
                        // 사격 조준 시 아군이 중간에 있으면 쏘지 않고 중단
                        if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || 
                                grid[nr][nc].equals(WALL_SYMBOL) || 
                                grid[nr][nc].equals(ITEM_SYMBOL) || 
                                grid[nr][nc].equals(TREE_SYMBOL) ||
                                isAlly(grid[nr][nc])) break;
                        
                        if (nr == target[0] && nc == target[1]) {
                            Queue<String> result = new ArrayDeque<>(actions);
                            if (!myAllies.get("M")[3].equals("0")) {
                                result.offer(MEGA_FIRE_CMDS[d]);
                            } else {
                                result.offer(FIRE_CMDS[d]);
                            }
                            return result; 
                        }
                    }
                }
            }

            for (int d = 0; d < 4; d++) {
                int nr = r + dy[d];
                int nc = c + dx[d];
                
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                    String cell = grid[nr][nc];
                    
                    // 💡 [수정됨] 길 찾기 이동 시, 해당 위치가 아군 또는 적군 포탑의 3x3 구역이면 진입 금지(continue)
                    if (cell.equals(WALL_SYMBOL) || cell.equals(WATER_SYMBOL) || cell.equals(ITEM_SYMBOL) || isAlly(cell) || isInTurretZone(grid, nr, nc)) continue;

                    int nextCost = currentCost;
                    Queue<String> nextActions = new ArrayDeque<>(actions);

                    if (cell.equals(TREE_SYMBOL)) {
                        nextCost += 2;
                        if (!myAllies.get("M")[2].equals("0")) {
                            nextActions.offer(FIRE_CMDS[d]);
                        } else {
                            nextActions.offer(MEGA_FIRE_CMDS[d]);
                        }
                        nextActions.offer(MOVE_CMDS[d]);
                    } else if (cell.equals("S")) {
                        nextCost += 10; 
                        nextActions.offer(MOVE_CMDS[d]);
                    } else {
                        nextCost += 1;
                        nextActions.offer(MOVE_CMDS[d]);
                    }

                    if (nextCost < minCost[nr][nc]) {
                        minCost[nr][nc] = nextCost;
                        pq.offer(new DijkstraNode(nr, nc, nextCost, nextActions));
                    }
                }
            }
        }
        return new ArrayDeque<>(); 
    }

    private static class DijkstraNode implements Comparable<DijkstraNode> {
        int row, col, cost;
        Queue<String> actions;
        
        DijkstraNode(int row, int col, int cost, Queue<String> actions) {
            this.row = row;
            this.col = col;
            this.cost = cost;
            this.actions = actions;
        }

        @Override
        public int compareTo(DijkstraNode other) {
            return Integer.compare(this.cost, other.cost);
        }
    }
    
    private static String decodeCaesar(String cipherText, int shift) {
        StringBuilder plainText = new StringBuilder();
        for (char c : cipherText.toCharArray()) {
            if (c >= 'A' && c <= 'Z') {
                int originalPos = c - 'A';
                int newPos = (originalPos + shift) % 26;
                if (newPos < 0) newPos += 26;
                plainText.append((char) ('A' + newPos));
            } else {
                plainText.append(c);
            }
        }
        return plainText.toString();
    }
    
    // --- 통신 및 파싱 로직 ---
    private static String init(String nickname) {
        try {
            System.out.println("[STATUS] Trying to connect to " + HOST + ":" + PORT + "...");
            socket = new Socket();
            socket.connect(new InetSocketAddress(HOST, PORT));
            System.out.println("[STATUS] Connected");
            String initCommand = "INIT " + nickname;
            return submit(initCommand);
        } catch (Exception e) {
            System.out.println("[ERROR] Failed to connect.");
            e.printStackTrace();
            return null;
        }
    }

    private static String submit(String stringToSend) {
        try {
            OutputStream os = socket.getOutputStream();
            String sendData = ARGS + stringToSend + " ";
            os.write(sendData.getBytes("UTF-8"));
            os.flush();
            return receive();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    private static String receive() {
        try {
            InputStream is = socket.getInputStream();
            byte[] bytes = new byte[1024];
            int length = is.read(bytes);
            if (length <= 0) {
                close();
                return null;
            }
            String gameData = new String(bytes, 0, length, "UTF-8");
            if (gameData.length() > 0 && gameData.charAt(0) >= '1' && gameData.charAt(0) <= '9') {
                return gameData;
            }
            close();
            return null;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    private static void close() {
        try {
            if (socket != null && !socket.isClosed()) {
                socket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void parseData(String gameData) {
        String[] gameDataRows = gameData.split("\n");
        int rowIndex = 0;
        String[] header = gameDataRows[rowIndex].split(" ");
        int mapHeight = header.length >= 1 ? Integer.parseInt(header[0]) : 0;
        int mapWidth = header.length >= 2 ? Integer.parseInt(header[1]) : 0; 
        int numOfAllies = header.length >= 3 ? Integer.parseInt(header[2]) : 0; 
        int numOfEnemies = header.length >= 4 ? Integer.parseInt(header[3]) : 0; 
        int numOfCodes = header.length >= 5 ? Integer.parseInt(header[4]) : 0; 
        rowIndex++;

        mapData = new String[mapHeight][mapWidth];
        for (int i = 0; i < mapHeight; i++) {
            String[] col = gameDataRows[rowIndex + i].split(" ");
            for (int j = 0; j < col.length; j++) {
                mapData[i][j] = col[j];
            }
        }
        rowIndex += mapHeight;

        myAllies.clear();
        for (int i = rowIndex; i < rowIndex + numOfAllies; i++) {
            String[] ally = gameDataRows[i].split(" ");
            String allyName = ally.length >= 1 ? ally[0] : "-";
            String[] allyData = new String[ally.length - 1];
            System.arraycopy(ally, 1, allyData, 0, ally.length - 1);
            myAllies.put(allyName, allyData);
        }
        rowIndex += numOfAllies;

        enemies.clear();
        for (int i = rowIndex; i < rowIndex + numOfEnemies; i++) {
            String[] enemy = gameDataRows[i].split(" ");
            String enemyName = enemy.length >= 1 ? enemy[0] : "-";
            String[] enemyData = new String[enemy.length - 1];
            System.arraycopy(enemy, 1, enemyData, 0, enemy.length - 1);
            enemies.put(enemyName, enemyData);
        }
        rowIndex += numOfEnemies;

        codes = new String[numOfCodes];
        for (int i = 0; i < numOfCodes; i++) {
            codes[i] = gameDataRows[rowIndex + i];
        }
    }

    private static void printData(String gameData) {
        System.out.printf("\n----------입력 데이터----------\n%s\n", gameData);
    }
}