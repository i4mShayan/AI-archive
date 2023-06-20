import sys

def indicesOf(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j

def distanceOf(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Heuristic function (Manhattan distance)
def heuristic(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if goal_state[i][j] != 0:
                distance += distanceOf(indicesOf(state, goal_state[i][j]), (i, j))
    return distance

# Successor function
def successors(state):
    successors = []
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_i, empty_j = i, j

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        new_i, new_j = empty_i + move[0], empty_j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[empty_i][empty_j] = new_state[new_i][new_j]
            new_state[new_i][new_j] = 0
            successors.append(new_state)

    return successors

# Goal test function
def is_goal(state, goal_state):
    return state == goal_state

# Print puzzle 
def print_puzzle(state):
    for row in state:
        print(row)

def rbfs(state, goal_state, f_limit, g):
    if is_goal(state, goal_state):
        return state

    successors_list = successors(state)
    successors_with_f = []

    if len(successors_list) == 0:
        return None

    for s in successors_list:
        f = max(g + heuristic(s, goal_state), f_limit)
        successors_with_f.append((s, f))

    while True:
        successors_with_f.sort(key=lambda x: x[1])
        best = successors_with_f[0]

        if best[1] > f_limit:
            return None

        alternative = successors_with_f[1][1] if len(successors_with_f) > 1 else sys.maxsize
        result = rbfs(best[0], goal_state, min(f_limit, alternative), g + 1)

        if result is not None:
            return result

        successors_with_f[0] = (best[0], sys.maxsize)


# Example input
initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
f_limit = heuristic(initial_state, goal_state)
result = rbfs(initial_state, goal_state, f_limit, 0)


print("Initial state:")
print_puzzle(initial_state)

if result is not None:
    print("Goal state reached:")
    print_puzzle(result)
else:
    print("Goal state could not be reached.")
