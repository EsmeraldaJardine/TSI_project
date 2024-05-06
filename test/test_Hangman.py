import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch
from io import StringIO
from src.Hangman import *



class TestHangman(unittest.TestCase):

    fake_words = ["test", "hangman", "python"]
    fake_player_input = {'3-attempts':['t', 'e', 's'],
                         '5-attempts':['a', 't', 'b', 'e', 's'],
                         '6-attempts':['a', 'f', 'b', 'd', 'c', 'g']
                         }


    @patch('getpass.getpass', side_effect=['n',''])
    def test_is_ready_to_play(self, mock_input):
        self.assertFalse(is_ready_to_play())
        self.assertTrue(is_ready_to_play())


    def test_select_word(self):
        #test to make sure the selected word is in the list of words
        with patch('builtins.open', unittest.mock.mock_open(read_data='\n'.join(self.fake_words))):
            # A helper function to create a mock to replace the use of `open'
            selected_word = select_word()
            self.assertIn(selected_word, self.fake_words)


    def test_validate_input(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # fake_out is used store the output of the StringIO object
         
            self.assertTrue(validate_input("a"))
            self.assertEqual(fake_out.getvalue().strip(), "")

            self.assertFalse(validate_input("ab"))
            self.assertEqual(fake_out.getvalue().strip(), "Enter only a SINGLE character")

            fake_out.truncate(0)  # Clear the output
            fake_out.seek(0)  # Reset to the beginning
            self.assertFalse(validate_input("1"))
            self.assertEqual(fake_out.getvalue().strip(), "Please only enter an alphabetic character")

    def test_join_guessed_letters(self):
        selected_word = "test"
        guessed_letters = {'t', 'e'}
        expected_output = "t e _ t"
        self.assertEqual(join_guessed_letters(selected_word, guessed_letters), expected_output)

    def test_is_game_over(self):
        selected_word = "test"
        max_wrong_guesses = 6
        wrong_guesses = 6
        self.assertTrue(is_game_over(set(selected_word), selected_word, max_wrong_guesses, wrong_guesses)[0])
        # game ends when wrong_guesses == max_wrong_guesses
        self.assertEqual(is_game_over(set(selected_word), selected_word, max_wrong_guesses, wrong_guesses)[1], 0) 
        # checks that "wins" is 0 when wrong_guesses == max_wrong_guesses
        self.assertTrue(is_game_over(set(selected_word), selected_word, max_wrong_guesses, 0)[0]) 
        # game ends when guessed_letters == selected_word and there are no wrong guesses 
        self.assertEqual(is_game_over(set(selected_word), selected_word, max_wrong_guesses, 0)[1], 1)
        # checks that "wins" is 1 when guessed_letters == selected_word and there are no wrong guesses

    def test_is_playing_again(self):
        with patch('builtins.input', side_effect=['y']):
            self.assertTrue(is_playing_again())
        with patch('builtins.input', side_effect=['n']):
            self.assertFalse(is_playing_again())
        with patch('builtins.input', side_effect=['x', 'y']):
            self.assertTrue(is_playing_again())
            # The first input is invalid, so the function should ask again

    @patch('src.Hangman.get_player_input')
    def test_game_over_correct_guesses(self, mock_input):
        # Mocking player inputs to simulate correct guesses
        mock_input.side_effect = self.fake_player_input['3-attempts']  # Providing inputs for correct guesses only
        
        selected_word = "test"

        victories = game_loop(selected_word, MAX_WRONG_GUESSES, WRONG_GUESSES_START)

        self.assertEqual(victories, 1)  # Expecting a victory, so victories should be 1
        self.assertEqual(mock_input.call_count, 3)  # Expecting 3 calls to get_player_input
    
    @patch('src.Hangman.get_player_input')
    def test_game_over_with_3_incorrect_guesses(self, mock_input):
        mock_input.side_effect = self.fake_player_input['5-attempts']  # 'a', 'b', and 'c' are incorrect guesses
        
        selected_word = "test"

        victories = game_loop(selected_word, MAX_WRONG_GUESSES, WRONG_GUESSES_START)
        self.assertEqual(victories, 1)  # Expecting a victory, so victories should be 1
        self.assertEqual(mock_input.call_count, 5)

    @patch('src.Hangman.get_player_input')
    def test_game_over_with_incorrect_guesses(self, mock_input):
        mock_input.side_effect = self.fake_player_input['6-attempts']  # 'a', 'b', and 'c' are incorrect guesses
        
        selected_word = "test"

        victories = game_loop(selected_word, MAX_WRONG_GUESSES, WRONG_GUESSES_START)
        self.assertEqual(victories, 0)  # Expecting no victories
        self.assertEqual(mock_input.call_count, 6)

if __name__ == '__main__':
    unittest.main()
