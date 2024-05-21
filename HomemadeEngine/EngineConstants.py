import chess
from chess import PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING, WHITE, BLACK
from HomemadeEngine.PieceTables import *

EVAL_PIECES = [PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING]
COLORS = [WHITE, BLACK]

PAWN_VAL = 1
KNIGHT_VAL = 3.05
BISHOP_VAL = 3.33
ROOK_VAL = 5.63
QUEEN_VAL = 9.5

PIECE_VALUES = { PAWN: PAWN_VAL,
                 KNIGHT: KNIGHT_VAL,
                 BISHOP: BISHOP_VAL,
                 ROOK: ROOK_VAL,
                 QUEEN: QUEEN_VAL,
                 KING: float('inf') }

PIECE_TO_TABLE = { PAWN: PAWN_TABLE,
                   KNIGHT: KNIGHTS_TABLE,
                   BISHOP: BISHOPS_TABLE,
                   ROOK: ROOKS_TABLE,
                   QUEEN: QUEENS_TABLE,
                   KING: KINGS_TABLE }
