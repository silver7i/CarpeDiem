t = int(input())

for tc in range(1, t+1):
    n = int(input())
    n //= 10


    def paper(n):
        f = [0] * (n + 2)

        f[1] = 1
        f[2] = 3

        for i in range(3, n+2):
            f[i] = f[i-1] + f[i-2] * 2
        
        return f[n]
    
    print(f"#{tc} {paper(n)}")