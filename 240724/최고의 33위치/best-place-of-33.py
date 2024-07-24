n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

max_sum = 0
for i in range(n - 2):
    for j in range(n - 2):
        s = sum(mat[i][j:j + 3] + mat[i + 1][j:j + 3] + mat[i + 2][j:j + 3])
        max_sum = max(max_sum, s)

print(max_sum)