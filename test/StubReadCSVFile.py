class StubReadCSVFile:

    def fix_working_directory(self):
        pass

    def get_file_data(self, file_name):
        if file_name == "test.csv":

            return [
                ['John', 'Doe', 'john@example.com', 'password123', '0', '0'],
                ['Alice', 'Smith', 'alice@example.com', 'password456', '3', '2'],
                 ['test@test', 'Mr', 'Test', 100, 100],
                 ['a', 'a', 'a', 0, 0],
            ]
        else:
            return None
        
    def get_last_lines(self, file_name, number_of_lines):
        data= self.get_file_data(file_name)
        if data is not None:
            return data[-1 * number_of_lines]
        else:
            return None
        
