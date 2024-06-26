class Customer:

    first_name_position = 1
    last_name_position = 2
    email_position = 0
    password_position = 3
    games_won_position = 4
    games_lost_position = 5

    def __init__(self, raw_customer):
        self.__first_name = raw_customer[self.first_name_position]
        self.__last_name = raw_customer[self.last_name_position]
        self.__email = raw_customer[self.email_position]
        self.__password = raw_customer[self.password_position]
        self.__total_games_won = raw_customer[self.games_won_position]
        self.__total_games_lost= raw_customer[self.games_lost_position]

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_name(self):
        return self.__first_name + " " + self.__last_name

    def get_email(self):
        return self.__email

    def compare_password(self, password):
        return password == self.__password
    
    def get_total_games_won(self):
        return self.__total_games_won
    
    def get_total_games_lost(self):
        return self.__total_games_lost
    

