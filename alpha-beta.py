import chess
import numpy as np

def h_minimax_alpha_beta(board, depth_limit=2):
    return (max_node_ab(board, 0, depth_limit))

def max_node_ab(board, current_depth, depth_limit=2, alpha=np.infty, beta=-np.infty):
    if(is_cutoff(board, current_depth, depth_limit=2)):
        return (heuristic_chess(board), None)
    
    allMoves = board.legal_moves
    (value, move) = (-np.infty, -np.infty)

    for i in allMoves:
        move = chess.Move.from_uci(str(i))
        board.push(move)

        (value1, move1) = min_node_ab(board, current_depth + 1, depth_limit)

        if(value1 > value):
            (value, move) = (value1, move)
            alpha = max(alpha, value)   #evaluating if it should be pruned
        board.pop()

        if(value >= beta):
            return (value, move)

    return (value, move)


def min_node_ab(board, current_depth, depth_limit=2, alpha=np.infty, beta=-np.infty):
    if(is_cutoff(board, current_depth, depth_limit=2)):
        return (heuristic_chess(board), None)

    allMoves = board.legal_moves
    (value, move) = (np.infty, np.infty)

    for i in allMoves:
        move = chess.Move.from_uci(str(i))
        board.push(move)
        
        (value1, move1) = max_node_ab(board, current_depth + 1, depth_limit)
        
        if(value1 < value):
            (value, move) = (value1, move)
            beta = min(beta, value)
        board.pop()

        if(value <= alpha):
            return (value, move)

    return (value, move)

