from typing import Type
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# this file contains classes and methods for managing the large language model

class LanguageModelManager:

    """Manages the large language model by:
    1. setting the properties like prompt, models, temperature
    2. has getter and setter methods for: a. getting and setting prompt_message
                                          b. getting models available
                                          c. adding a model
                                          d. getting a specific model with indexing
                                          e. getting the prompt template prepared for an agent

    """
    #constructor
    def __init__(self):

        self.prompt = "You are my friend JARVIS. use tools provided if need be to interact with me"

        self.models = ["gpt-3.5-turbo", "gpt-4-1106-preview"]

        self.llm = ChatOpenAI(temperature = 0, model = self.models[1])

        self.chat_history = []


    #get the prompt
    def get_prompt_message(self) -> str:

        return self.prompt
    
    #set the prompt
    def set_prompt_message(self, newprompt: str):

        try:

            self.prompt = newprompt

        except ValueError:

            print("Enter a string message for the new prompt")

    #get all the models listed
    def get_models_available(self) -> list:

        return self.models
    
    #add new model
    def add_new_model(self, modelname: str):

        self.models.append(modelname)


    #get_specific model using indexing   
    def get_model(self,index: int) -> str:
        
        try:
           
           return self.models[index]
        
        except ModelNotFoundError :

            raise ModelNotFoundError("The model requested is not in the list of available models")
        
        except IndexError as e:

            print("Index keyed is out of range", e)

    #gets the prompt template generated
    def get_prompt_template_for_agent(self) -> Type:

        prompt_template_class_object = PromptTemplate(self.get_prompt_message())

        return prompt_template_class_object.generate_the_template()
    

#generates prompt template for the agent
class PromptTemplate:

    """This class creates the prompt template passed to the agent
    Advantages of using this template which includes the prompt in the LanguageModelManager class as the system message is:
    
    1. Creates memory for the agent
    2. Maintains context in the conversations through consistently injecting the system message to the agent"""    

    #constructor
    def __init__(self, prompt : str):

        self.system_message = prompt

        self.memory_key = "chat_history"


    #generates the prompt template
    def generate_the_template(self) -> Type:

        prompt = ChatPromptTemplate.from_messages(

                    [
                        (
                            "system",

                             self.system_message,
                        ),

                        MessagesPlaceholder(variable_name = self.memory_key),

                        (
                            "user",
                          
                            "{input}"
                        ),

                        MessagesPlaceholder(variable_name = "agent_scratchpad"),
                    ]

                )
        
        return prompt
        


#custom exception
class ModelNotFoundError(Exception):

    """Custom exception class for ModelNotFoundError"""

    def __init__(self, message = "Model not found"):

        self.message = message

        super().__init__(self.message)
    