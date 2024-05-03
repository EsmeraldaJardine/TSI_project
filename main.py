from src.Login import LogIn
from src.Hangman import *
from src.HangmanDrawing import hangman_drawings
from src.WriteCSVFile import UpdateCsvWinsLosses

class Main:
    def main():
        log_in = LogIn()
        is_logged_in = log_in.log_in()
        customer_details = log_in.get_customer_attributes()
        while is_logged_in:
            total_wins = int(customer_details['total_wins'])
            total_losses = int(customer_details['total_losses'])
            print(f"Welcome {customer_details['first_name']} {customer_details['last_name']}!")
            print(f"Your total score is: {total_wins} wins and {total_losses} losses")
            session_wins = 0
            session_losses = 0
            while True:
                is_ready_to_play(session_wins, session_losses)
                selected_word = select_word()
                GUESSED_LETTERS.clear()
                hangman_drawings(WRONG_GUESSES_START)
                welcome_message(selected_word)
                
                victories = game_loop(selected_word, GUESSED_LETTERS, MAX_WRONG_GUESSES, WRONG_GUESSES_START)
                write_to_csvfile = UpdateCsvWinsLosses()
                
                if victories == 1:
                    session_wins += 1
                    total_wins += 1
                    write_to_csvfile.update_customer_game_result(log_in.email_address, "customer.csv", True)
                    print("updated win")   

                else:
                    session_losses += 1
                    total_losses += 1
                    write_to_csvfile.update_customer_game_result(log_in.email_address, "customer.csv", False)
                    print("updated loss")
        
                if not is_playing_again():
                    print(f"\nYour final score is: {session_wins} wins and {session_losses} losses")
                    print(f"Your updated profile score is: {total_wins} wins and {total_losses} losses")
                    print(f"\nGoodbye {customer_details['first_name']} {customer_details['last_name']}!")
                    exit()

        print("Goodbye!")

if __name__ == '__main__':
    Main.main()


