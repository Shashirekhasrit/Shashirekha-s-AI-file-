def water_jug_solver(jugA, jugB, target):
    a = 0  # current water in Jug A
    b = 0  # current water in Jug B

    steps = []

    while True:
        # If Jug A has the target
        if a == target or b == target:
            steps.append((a, b))
            break

        # Strategy:
        # 1. If Jug A is empty, fill it
        if a == 0:
            a = jugA
            steps.append((a, b))

        # 2. Pour from A → B
        pour = min(a, jugB - b)
        a -= pour
        b += pour
        steps.append((a, b))

        # 3. If Jug B is full, empty it
        if b == jugB:
            b = 0
            steps.append((a, b))

    return steps


# Example Usage
jugA = 4
jugB = 3
target = 2

solution = water_jug_solver(jugA, jugB, target)

print("Steps to reach the goal:")
for i, step in enumerate(solution):
    print(f"Step {i}: JugA = {step[0]} L, JugB = {step[1]} L")
