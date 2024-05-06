from Login import LogIn
from WriteCSVFile import UpdateCsvWinsLosses
from Game import Game

class Main:
    def main():
        log_in = LogIn()
        is_logged_in = log_in.log_in()
        customer_details = log_in.get_customer_attributes()
        
        while is_logged_in:
            total_wins = int(customer_details['total_wins'])
            total_losses = int(customer_details['total_losses'])
            print(f"\nWelcome {customer_details['first_name']} {customer_details['last_name']}!")
            print(f"Your total score is: {total_wins} wins and {total_losses} losses")

            game = Game()
            is_playing = True

            while is_playing:
                is_playing, result = game.play_game()
                write_to_csv = UpdateCsvWinsLosses()
                
                if result == "win":
                    total_wins += 1
                    write_to_csv.update_customer_game_result(log_in.email_address, "customer.csv", True)
    

                elif result == "loss":
                    total_losses += 1
                    write_to_csv.update_customer_game_result(log_in.email_address, "customer.csv", False)
                
                print(f"\nYour updated profile score is: {total_wins} wins and {total_losses} losses")
                
            print(f"\nGoodbye {customer_details['first_name']} {customer_details['last_name']}!")
            exit()

        print("Goodbye!")

if __name__ == '__main__':
    Main.main()


