from collections import deque

def water_jug_bfs(jug1_cap, jug2_cap, target):
    # Each state is (amount_in_jug1, amount_in_jug2)
    visited = set()
    queue = deque()
    
    start = (0, 0)
    queue.append(start)
    visited.add(start)
    
    parent = {start: None}   # For reconstructing the path

    while queue:
        x, y = queue.popleft()

        if x == target or y == target:
            # Reconstruct path
            path = []
            curr = (x, y)
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            return path

        # All possible next moves
        moves = []

        # 1. Fill Jug 1
        moves.append((jug1_cap, y))
        # 2. Fill Jug 2
        moves.append((x, jug2_cap))
        # 3. Empty Jug 1
        moves.append((0, y))
        # 4. Empty Jug 2
        moves.append((x, 0))
        # 5. Pour Jug 1 -> Jug 2
        pour = min(x, jug2_cap - y)
        moves.append((x - pour, y + pour))
        # 6. Pour Jug 2 -> Jug 1
        pour = min(y, jug1_cap - x)
        moves.append((x + pour, y - pour))

        for new_state in moves:
            if new_state not in visited:
                visited.add(new_state)
                parent[new_state] = (x, y)
                queue.append(new_state)

    return None  # No solution

# Example usage:
jug1 = 4
jug2 = 3
target = 2

solution = water_jug_bfs(jug1, jug2, target)

if solution:
    print("Steps to reach the goal:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")
