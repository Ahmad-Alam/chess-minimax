import chess
import numpy as np

#making the heuristic function, evaluating the leaf nodes
def heuristic_chess(board):
    outcome = board.outcome()    
    winner = outcome
    if winner:
        return +1
    elif winner == False:  
        return -1
    elif outcome == None:
        fPawn = len(board.pieces(chess.PAWN,chess.WHITE)) - len(board.pieces(chess.PAWN,chess.BLACK))
        fKnight = len(board.pieces(chess.KNIGHT,chess.WHITE)) - len(board.pieces(chess.KNIGHT,chess.BLACK))
        fBishop = len(board.pieces(chess.BISHOP,chess.WHITE)) - len(board.pieces(chess.BISHOP,chess.BLACK))
        fRook = len(board.pieces(chess.ROOK,chess.WHITE)) - len(board.pieces(chess.ROOK,chess.BLACK))
        fQueen = len(board.pieces(chess.QUEEN,chess.WHITE)) - len(board.pieces(chess.QUEEN,chess.BLACK))

        heuristic_value = (fPawn + 3*fKnight + 4*fBishop + 5*fRook + 9*fQueen)/100
        return heuristic_value

    else: 
        return 0
    
#setting a break for shortening the algorithm 
def is_cutoff(board, current_depth, depth_limit=2): 
    outcome = board.outcome()
    if outcome != None:
        return True
    elif current_depth == depth_limit:
        return True
    else:
        return False

#calling the minimax without alpha-beta pruning
def h_minimax(board, depth_limit=2):
    return (max_node(board, 0, depth_limit))


#helper functions
def max_node(board, current_depth, depth_limit=2):

    if(is_cutoff(board, current_depth, depth_limit=2)):
        return (heuristic_chess(board), None)
    
    allMoves = board.legal_moves    #list all moves
    (value, move) = (-np.infty, -np.infty)

    for i in allMoves:  #iterate through each move
        move = chess.Move.from_uci(str(i))  #push a move in the board to update it
        board.push(move)
        (value1, move1) = min_node(board, current_depth + 1, depth_limit)   #updated board is sent in the recursive call
        
        if(value1 > value): #if new value is greater than old value update the heuristic value
            (value, move) = (value1, move)
        board.pop()

    return (value, move)


def min_node(board, current_depth, depth_limit=2):
    if(is_cutoff(board, current_depth, depth_limit=2)):
        return (heuristic_chess(board), None)

    allMoves = board.legal_moves
    (value, move) = (np.infty, np.infty)

    for i in allMoves:
        move = chess.Move.from_uci(str(i))
        board.push(move)
        (value1, move1) = max_node(board, current_depth + 1, depth_limit)
        if(value1 < value):
            (value, move) = (value1, move)
        board.pop()

    return (value, move)


