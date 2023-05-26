import random

def sticks(stick):
    for i in range(stick):
        print("|", end="")
    print()

def successors_generator(stick):
    successors = []
    for i in range(1, min(stick, 4)):
        successors.append(stick - i)
    return successors

def AlphaBeta(stick, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or stick == 0:
        return 0
    
    if is_maximizing_player:
        max_eval = -float('inf')
        for successor in successors_generator(stick):
            eval = AlphaBeta(successor, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    
    else:
        min_eval = float('inf')
        for successor in successors_generator(stick):
            eval = AlphaBeta(successor, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def get_best_move(stick):
    best_eval = -float('inf')
    best_move = 1
    alpha = -float('inf')
    beta = float('inf')
    for i in range(1, min(stick, 4)):
        eval = AlphaBeta(stick - i, 15, alpha, beta, False)
        if eval > best_eval:
            best_eval = eval
            best_move = i
        alpha = max(alpha, eval)
    return best_move

stick = 25

sticks(stick)

while stick > 0:

    # Turno de la maquina (aleatorio)
    palos_ia = random.randint(1, 3)
    palos_ia = min(palos_ia, stick)
    print(f"La IA quita {palos_ia} palos.")
    stick -= palos_ia
    sticks(stick)
    if stick == 0:
        print("MiniMax win")
        break

    # Turno de AlphaBeta (minimax mejorado)
    drop = get_best_move(stick)
    print(f"AlphaBeta quita {drop} palos.")
    stick -= drop
    sticks(stick)
    if stick == 0:
        print("Maquina aleatoria win(no deberia ganar)")
        break