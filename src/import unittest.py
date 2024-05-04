import unittest
from unittest.mock import patch
from src.Game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_play_game(self):
        # Mocking the input and output for testing
        with patch('builtins.input', side_effect=['y', 'n']):
            with patch('builtins.print') as mock_print:
                result = self.game.play_game()
                self.assertEqual(result, "win")  # Assuming the player wins the game
                mock_print.assert_called_with("\nYour final score this session is: 1 wins and 0 losses")

                result = self.game.play_game()
                self.assertEqual(result, "loss")  # Assuming the player loses the game
                mock_print.assert_called_with("\nYour final score this session is: 1 wins and 1 losses")

if __name__ == '__main__':
    unittest.main()