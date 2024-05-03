from src.Hangman import *

class Game:
    def play_game(self):
        is_playing = True
        while is_playing:
            session_wins = 0
            session_losses = 0
            is_ready_to_play(session_wins, session_losses)
            selected_word = select_word()
            GUESSED_LETTERS.clear()
            hangman_drawings(WRONG_GUESSES_START)
            welcome_message(selected_word)
            
            victories = game_loop(selected_word, GUESSED_LETTERS, MAX_WRONG_GUESSES, WRONG_GUESSES_START)
            
            if victories == 1:
                session_wins += 1
                print(f"\nYour final score this session is: {session_wins} wins and {session_losses} losses")
                game_result = "win"  

            else:
                session_losses += 1
                print(f"\nYour final score this session is: {session_wins} wins and {session_losses} losses")
                game_result = "loss"

            if not is_playing_again():
                is_playing = False
                return game_result
                
