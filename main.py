from src.Login import LogIn
from src.Hangman import *
from src.HangmanDrawing import hangman_drawings
from src.WriteCSVFile import UpdateCsvWinsLosses

class Main:
    def main():
        log_in = LogIn()
        log_in.log_in()
        total_wins = 0
        total_losses = 0
        while is_ready_to_play(total_wins, total_losses) == True:
            selected_word = select_word()
            GUESSED_LETTERS.clear()
            hangman_drawings(WRONG_GUESSES_START)
            welcome_message(selected_word)
            
            victories = game_loop(selected_word, GUESSED_LETTERS, MAX_WRONG_GUESSES, WRONG_GUESSES_START)
            write_to_csvfile = UpdateCsvWinsLosses()
            
            if victories == 1:
                total_wins += 1
                write_to_csvfile.update_customer_game_result(log_in.email_address, "customer.csv", True)
                print("updated win")   

            else:
                total_losses += 1
                write_to_csvfile.update_customer_game_result(log_in.email_address, "customer.csv", False)
                print("updated loss")
    
            if is_playing_again():
                continue
            else:
                break  

if __name__ == '__main__':
    Main.main()


