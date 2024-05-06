class StubReadCSVFile:
    def get_file_data(self, file_name):
        if file_name == "test.csv":

            return [
                ['John', 'Doe', 'john@example.com', 'password123', '0', '0'],
                ['Alice', 'Smith', 'alice@example.com', 'password456', '3', '2'],
                 ['test@test', 'Mr', 'Test', 100, 100],
                 ['a', 'a', 'a', 0, 0],
            ]
