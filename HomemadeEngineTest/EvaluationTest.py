import unittest
import chess
from HomemadeEngine.ChessEngine import get_best_move, negamax_get_best_move, negamax_NEW
from HomemadeEngine.Evaluation import evaluate_position

class TestEvaluationMethod(unittest.TestCase):
#     def test_whiteMateIn1(self):
#         fen = '5k2/2Q2Q2/8/3NKB2/4P3/P3B1P1/1P3P1P/R6R b - - 30 53'
#         board = chess.Board()
#         board.set_fen(fen)
#         eval = evaluate_position(board)
#         self.assertEqual(100000, eval)

#     def test_blackFreeCapture(self):
#         fen = 'rnbqkbnr/ppp1pppp/8/4p3/8/8/PPPPPPPP/RNBQKB1R w KQkq - 0 3'
#         board = chess.Board()
#         board.set_fen(fen)
#         best_move = get_best_move(board, chess.BLACK)
#         neg_best = negamax_get_best_move(board)
#         print("\n")
#         print(best_move)
#         print("neg best move: " + str(neg_best))
#         print(board.turn == chess.WHITE)
#         print("\n")
    
    # def test_negamaxWhiteTakeQueen(self):
    #     fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    #     board = chess.Board()
    #     board.set_fen(fen)
        
    #     best_move = negamax_get_best_move(board)
    #     best_move_mini = get_best_move(board, chess.WHITE)
    #     self.assertEqual(str(best_move), str(best_move_mini))

    # def test_negamaxBlackFirstMove(self):
    #         fen = 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1'
    #         board = chess.Board()
    #         board.set_fen(fen)
            
    #         best_move = negamax_get_best_move(board)
    #         best_move_mini = get_best_move(board, chess.WHITE)
    #         self.assertEqual(str(best_move), str(best_move_mini))

        
    def test_negamaxWhiteTakeQueen(self):
        fen = 'rnb1kbnr/ppp2ppp/3p4/4pq2/3NP1Q1/8/PPPP1PPP/RNB1KB1R w KQkq - 2 5'
        board = chess.Board()
        board.set_fen(fen)
        alpha = 1000
        beta = -1000
        print(-negamax_NEW(board, 3, 1000, -1000))


if __name__ == "__main__":
    unittest.main()

