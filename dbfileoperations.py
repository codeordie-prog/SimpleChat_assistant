from database import User_Database_Manager as userdata
from langchain.pydantic_v1 import BaseModel 


class FileOperationsFunctions(userdata):

    def __init__(self):

        #initialize the parent class first

        super().__init__()

        #get user dictionary with user_data parsed from the user_data.json file

        self.dictionary = self.get_userdata_dictionary(self.path_to_readonly_files,self.user_filename)

    
       
    def get_user_profile(self) -> dict:
        "useful when need be to find out your creator's name and age"
        profile = self.dictionary["profile"]
        return profile

    #getter for interests - returns a dictionary with all the interests

    
    def get_user_interests(self) -> dict:
        "gets you the creator's interests. usefull for tailoring your recommendations and suggestions according to creator's interests"
        interests = self.dictionary["interests"]
        return interests

    #getter for longterm goals, returns a list of longterm goals

           
    def get_user_longterm_goals(self) -> list:
        "useful for getting creator's longterm goal"
        try:
           longterm_goals = self.dictionary["goals"]["longterm"]
           return longterm_goals
        
        except KeyError:
            print("Key entered doesn't exist")
        except ValueError:
            print("Value entered doesn't exist")


    #get shortterm goals- returns a list of shortterm goals
    
    def get_user_shortterm_goals(self) -> list:
        "useful for getting creator's shortterm goals"
        shortterm_goals = self.dictionary["goals"]["shortterm"]
        return shortterm_goals

    #get specific interests
    def get_specific_interest(self,specific_interest) -> list:

        try:

            lower_case_specific_interests = specific_interest.lower()
            interests = self.dictionary["interests"][lower_case_specific_interests]
            return interests
        
        except KeyError:
            print("The specified interest doesn't match the users interests")
                
            


        

