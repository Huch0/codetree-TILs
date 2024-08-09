n, m, t = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

beads = []
for _ in range(m):
    beads.append(tuple(map(int, input().split())))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for time in range(t):
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

    # Eliminate overlapping beads
    visited = set()
    remain_beads = []
    for bead in beads:
        if bead not in visited:
            visited.add(bead)
            remain_beads.append(bead)

# Count the number of remaining beads
print(len(beads))