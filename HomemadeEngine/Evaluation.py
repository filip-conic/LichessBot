import chess
from HomemadeEngine.PieceTables import *
from EngineConstants import *

def evaluate_position(board):
    if board.is_checkmate():
        if board.turn == chess.BLACK:
            return 100000
        else: 
            return -100000
    
    if board.is_stalemate():
        return 0
    
    evaluation = 0

    # Basic piece count evaluation
    for piece in EVAL_PIECES:
        w_pieces = len(board.pieces(piece, WHITE))
        b_pieces = len(board.pieces(piece, BLACK))
        evaluation += PIECE_VALUES[piece] * (w_pieces - b_pieces)

    pawn_sum = sum([PAWN_TABLE[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawn_sum = pawn_sum + sum([-PAWN_TABLE[chess.square_mirror(i)] for i in board.pieces(chess.PAWN, chess.BLACK)])
    knight_sum = sum([KNIGHTS_TABLE[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knight_sum = knight_sum + sum(
        [-KNIGHTS_TABLE[chess.square_mirror(i)] for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishop_sum = sum([BISHOPS_TABLE[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishop_sum = bishop_sum + sum(
        [-BISHOPS_TABLE[chess.square_mirror(i)] for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rook_sum = sum([ROOKS_TABLE[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
    rook_sum = rook_sum + sum([-ROOKS_TABLE[chess.square_mirror(i)] for i in board.pieces(chess.ROOK, chess.BLACK)])
    queens_sum = sum([QUEENS_TABLE[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
    queens_sum = queens_sum + sum(
        [-QUEENS_TABLE[chess.square_mirror(i)] for i in board.pieces(chess.QUEEN, chess.BLACK)])
    kings_sum = sum([KINGS_TABLE[i] for i in board.pieces(chess.KING, chess.WHITE)])
    kings_sum = kings_sum + sum([-KINGS_TABLE[chess.square_mirror(i)] for i in board.pieces(chess.KING, chess.BLACK)])

    boardvalue = evaluation + pawn_sum + knight_sum + bishop_sum + rook_sum + queens_sum + kings_sum

    return boardvalue