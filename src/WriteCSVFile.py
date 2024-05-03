import csv, os

class UpdateCsvWinsLosses:
        
    def update_customer_game_result(self,customer_email, file_name, is_win):
        updated_file_data = []
        with open("resource/" + file_name, 'rt')as data_file:
            file_reader = csv.reader(data_file)
            for row in file_reader:
                if row[Customer.email_position] == customer_email:
                    if is_win:
                        row[Customer.games_won_position] = str(int(row[Customer.games_won_position]) + 1)
                    else:
                        row[Customer.games_lost_position] = str(int(row[Customer.games_lost_position]) + 1)
                updated_file_data.append(row)

        with open("resource/" + file_name, 'wt')as data_file:
            file_writer = csv.writer(data_file)
            file_writer.writerows(updated_file_data)

                    