import csv, os
class ReadCSVFile:

    def fix_working_directory(self):
        current_working_directory = os.getcwd()
        while "test" in current_working_directory or "src" in current_working_directory:
            os.chdir("/")
            current_working_directory = os.getcwd()

    def get_file_data(self,file_name):
        try:
            self.fix_working_directory()
            file_data = []
            with open("resource/" + file_name, 'rt')as data_file:
                file_reader = csv.reader(data_file)
                for row in file_reader:
                    file_data.append(row)
            return file_data
        except FileNotFoundError:
            print(f"File {file_name} not found")
            return None
        
    
    def get_last_lines(self, file_name, number_of_lines):
        return self.get_file_data(file_name)[-1 * number_of_lines]

