n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

n_happy = 0

for i in range(n):
    l, r = 0, 0
    while r < n:
        if mat[i][l] == mat[i][r]:
            # check
            if r - l + 1 >= m:
                n_happy += 1
                break
        else:
            l = r
        r += 1
for j in range(n):
    l, r = 0, 0
    while r < n:
        if mat[l][j] == mat[r][j]:
            # check
            if r - l + 1 >= m:
                n_happy += 1
                break
        else:
            l = r
        r += 1

print(n_happy)