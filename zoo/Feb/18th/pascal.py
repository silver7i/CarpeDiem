t = int(input())

for tc in range(1, t+1):
    n = int(input())

    tri = []

    print(f"#{tc}")
    for i in range(n):
        tri_row = []
        for j in range(i+1):
            if j == 0 or j == i:
                tri_row.append(1)
            else:
                tri_row.append(tri[i-1][j-1] + tri[i-1][j])

        tri.append(tri_row)
        print(*tri_row)