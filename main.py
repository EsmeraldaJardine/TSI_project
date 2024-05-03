from src.Login import LogIn
from src.Hangman import *
from src.HangmanDrawing import hangman_drawings
from src.WriteCSVFile import UpdateCsvWinsLosses

class Main:
    def main():
        log_in = LogIn()
        logged_in_customer = log_in.log_in()
        print("customer email: ", logged_in_customer.get_email())
        while is_ready_to_play() == True:
            selected_word = select_word()
            hangman_drawings(WRONG_GUESSES_START)
            welcome_message(selected_word)
            game_loop(selected_word, GUESSED_LETTERS, MAX_ATTEMPTS, WRONG_GUESSES_START)
            write_to_csvfile = UpdateCsvWinsLosses()
            
            if SESSION_WINS != 0:
                write_to_csvfile.update_customer_game_result(logged_in_customer.get_email(), "customer.csv", True)
            elif SESSION_LOSSES != 0:
                write_to_csvfile.update_customer_game_result(logged_in_customer.get_email(), "customer.csv", False)
            if is_playing_again():
                continue
            else:
                
                break  

if __name__ == '__main__':
    Main.main()


