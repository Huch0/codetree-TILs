n = int(input())
jenga = []
for _ in range(n):
    jenga.append(int(input()))

removes = []
for _ in range(2):
    removes.append(list(map(int, input().split())))


n_blocks = n
for s, e in removes:
    jenga[s-1:e] = [0] * (e - s + 1)

    down = -1
    for up in range(-1, -n_blocks-1, -1):
        if jenga[down] > 0:
            down -= 1
            continue
        
        # if up != down:
        if jenga[up] > 0:
            jenga[down], jenga[up] = jenga[up], 0
            down = up

    n_blocks -= e - s + 1
    jenga[:] = jenga[-n_blocks:]

print(n_blocks)
for block in jenga:
    if block > 0:
        print(block)