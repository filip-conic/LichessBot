import unittest
import chess
from HomemadeEngine.ChessEngine import evaluate_position, get_best_move

class TestEvaluationMethod(unittest.TestCase):
    def test_whiteMateIn1(self):
        fen = '5k2/2Q2Q2/8/3NKB2/4P3/P3B1P1/1P3P1P/R6R b - - 30 53'
        board = chess.Board()
        board.set_fen(fen)
        eval = evaluate_position(board)
        self.assertEqual(100000, eval)

    def test_blackFreeCapture(self):
        fen = 'rnbqkbnr/ppp1pppp/8/4p3/8/8/PPPPPPPP/RNBQKB1R w KQkq - 0 3'
        board = chess.Board()
        board.set_fen(fen)
        best_move = get_best_move(board, chess.BLACK)
        print(best_move)
        print(board.turn == chess.WHITE)
    
if __name__ == "__main__":
    unittest.main()

