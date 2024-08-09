n, m, t = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

beads = []
for _ in range(m):
    beads.append(tuple(map(int, input().split())))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for time in range(t):
    new_beads = []
    # Move beads
    for r, c in beads:
        r, c = r - 1, c - 1
        max_nx, max_ny = r, c
        max_num = 0

        for dx, dy in directions:
            nx, ny = r + dx, c + dy

            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] > max_num:
                    max_nx, max_ny = nx, ny
                    max_num = grid[nx][ny]
        
        new_beads.append((max_nx, max_ny))


    # Eliminate overlapping beads
    remain_beads = []
    for b1 in beads:
        duplicates = []
        for b2 in beads:
            if b1 == b2:
                duplicates.append(b2)
        
        if len(duplicates) == 1:
            remain_beads.append(b1)

    beads = remain_beads

# Count the number of remaining beads
print(len(beads))