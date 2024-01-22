
import os,json

class User_Database_Manager:

    """Handles user data that will be useful to the LLM model.
       creates and dumbs data provided to a json file format that is stored in the user files in the provided path
       retrieves the json file and parses it to a dictionary .
       filepaths can be updated using the function update_file_path"""

    #constructor

    def __init__(self):


        self.path_to_readonly_files = "C:/Users/LENOVO/Desktop/python/Library/readonly"

        self.writtable_filepath = "C:/Users/LENOVO/Desktop/python/Library/writtable"

        self.user_filename = "user_data.json"

        self.data = "" #this is where the data goes in - make it as a dictionary then dump it as json file using the create_json_file function
        
        

    #create the json file and return 
        
    def create_json_file(self):

        data = self.data

        try:

            fullpath = os.path.join(self.path_to_readonly_files, self.user_filename)

            with open(fullpath, "w") as file:

                json.dump(data,file, indent = 4)

        except FileNotFoundError as e:

            print("File or Directory not found check the filepath provided" , e)

        except IOError:

            print("IOError occured")
        
    

    #parse the json file to a dictionary

    def parse_json_to_dictionary(self, path_to_readonly_files : str ,file_name : str):

        try:

            fullpath = os.path.join(path_to_readonly_files,file_name)

            with open(fullpath, "r") as file:

                dictionary = json.load(file)

            return dictionary

        except FileNotFoundError as e:

            print("File not found, therefore could not perform the parsing request, check the path provided", e)
    
    # gets the specific userdata dictionary from the json file

    def get_userdata_dictionary(self,filepath : str, filename : str):

        user_data_dictionary = None

        try:

            user_data_dictionary = self.parse_json_to_dictionary(filepath,filename)

            return user_data_dictionary

        except FileNotFoundError:

            print("File not found please confirm the path and the name")

    #update readonly filepath
            
    def update_readonly_filepath(self, newpath : str):

        self.path_to_readonly_files = newpath

    #update writtable filepath
        
    def update_writtable_filepath(self, newpath : str):

        self.writtable_filepath = newpath















    

        
