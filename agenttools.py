
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentType
from dbfileoperations import FileOperationsFunctions as fop
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.tools.convert_to_openai import format_tool_to_openai_function
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.agents import AgentExecutor




#the fileoperation object
fp = fop()

class AgentTools:

    """These tools can be modified to fit the data provided to the agent. The ones defined below are in accordance to the data I
    provided to the agent.."""

    
    #tool 1 - interests - gets computer science interests
    @tool
    def get_computer_science_interests():

        "returns the computer science interests of the creator"

        return fp.get_specific_interest(specific_interest="computerscience")

    #tool 2 - interests - get spiritual interests
    @tool
    def get_spiritual_interests():

        "returns spiritual interests of the creator"

        return fp.get_specific_interest("spirituality")

    #tool 3 - interests - gets philosophy interests
    @tool
    def get_philosophy_interests():

        "returns philosophy interests of the creator"

        return fp.get_specific_interest(specific_interest="philosophy")
        
    
    #tool 4 -interests - gets science interests
    @tool
    def get_science_interests():

        "returns general science interests of the creator"

        return fp.get_specific_interest("science")

    
    #tool 5 - interests - gets movies interests
    @tool
    def get_movie_interests():

        "returns creator's movie interests"

        return fp.get_specific_interest("movies")

    
    #tool 6 - interests - music
    @tool
    def get_music_interests():

        "returns creator's music interests"

        return fp.get_specific_interest("music")


    #tool 7 - interests - books
    @tool
    def get_book_interests():

        "returns creator's book interests"

        return fp.get_specific_interest("books")

    
    #tool 8 - profile - returns user profile
    @tool
    def get_creator_profile():

        "returns the profile, including name, age and residence of the creator"

        return fp.get_user_profile()

    #tool 9 - long term goals
    @tool
    def get_creator_longterm_goals():

        "returns creator's longterm goals, ambition, and his cosmic vision of existence"

        return fp.get_user_longterm_goals()

    
    #tool 10 - shortterm goals
    @tool
    def get_creator_shortterm_goals():

        "returns creator's shortterm goals"

        return fp.get_user_shortterm_goals()
    

    

    tools = [get_computer_science_interests,get_book_interests,get_creator_longterm_goals,get_creator_profile,get_movie_interests,
             get_music_interests,get_philosophy_interests,get_spiritual_interests,get_creator_shortterm_goals,get_science_interests]
        
       





    


