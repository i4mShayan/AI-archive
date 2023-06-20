import math


def nodeNameOf(index):
    return chr(index + 65 - 1)

def minimax(depth, index, is_max_turn, values, path=None):
    tree_depth = int(math.log(len(values), 2))

    if path is None:
        path = []
    if depth == tree_depth:
        index = index - 2**tree_depth
        return values[index], path + [values[index]]

    best_value = None
    best_path = None

    for i in range(2):
        child_value, child_path = minimax(depth + 1, index * 2 + i, not is_max_turn, values, path + [nodeNameOf(index)])
        if best_value is None:
            best_value = child_value
            best_path = child_path
        elif is_max_turn and child_value > best_value:
            best_value = child_value
            best_path = child_path
        elif not is_max_turn and child_value < best_value:
            best_value = child_value
            best_path = child_path

    return best_value, best_path


def alpha_beta(depth, index, is_max_turn, values, alpha, beta, path=None, show_pruning=False):
    tree_depth = int(math.log(len(values), 2))

    if path is None:
        path = []
    if depth == tree_depth:
        index = index - 2**tree_depth
        return values[index], path + [values[index]]

    best = MIN if is_max_turn else MAX
    best_path = []

    for i in range(2):
        value, child_path = alpha_beta(depth + 1, index * 2 + i, not is_max_turn, values, alpha, beta, path + [nodeNameOf(index)])

        if is_max_turn:
            best = max(best, value)
            alpha = max(alpha, best)
        else:
            best = min(best, value)
            beta = min(beta, best)

        if beta <= alpha:
            if(show_pruning):
                print("Pruning node", nodeNameOf(index), "with alpha =", alpha, "and beta =", beta, "at depth", depth)
            break

        if value == best:
            best_path = child_path

    return best, best_path


MIN, MAX = float('-inf'), float('inf')

if __name__ == "__main__":
    is_max_turn = True
    # values = [1, 2, 3, 4, 5, 6, 7, 8]  # binary tree
    values = [int(x) for x in input("Enter a binary tree (a power 2 number of nodes): ").split(", ")]
    print("\n=================== Start of Normal Minimax ===================")
    best_score, path = minimax(0, 1, is_max_turn, values)
    print("Best score:", best_score)
    print("Path to the best score:", path)

    print("\n=================== Start of Minimax with Alpha Beta Pruning  ===================")
    best_score, path = alpha_beta(0, 1, is_max_turn, values, MIN, MAX, show_pruning=True)
    print("Best score:", best_score)
    print("Path to the best score:", path)
