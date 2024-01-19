from langchain_community.tools.convert_to_openai import format_tool_to_openai_function
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.agents import AgentExecutor
from agenttools import AgentTools
from llm_manager import LanguageModelManager,PromptTemplate
from typing import Type

#create and manage the agent from here
#include the agent executor

class Agent(AgentTools,LanguageModelManager,PromptTemplate):

    """This class creates and manages the agent
    it inherits AgentTools, LanguageModelManger and PromptTemplate classes.
    it integrates data and methods from the inherited classes to form an agent that is used in the main function to execute conversations"""

    def __init__(self):

        #initialize the inherited classes
        super().__init__()

        self.agent_executor = self.create_agent_executor() #the executor


    #bind llm with tools
    def bind_llm_with_tools(self) -> Type:

        llm = self.llm #accessed from LanguageModelManager class

        tools = self.tools #accessed from the AgentTools class

        llm_with_tools = llm.bind(functions = [format_tool_to_openai_function(tool) for tool in tools]) #binding the llm with tools

        return llm_with_tools
    
    
    #make the agent
    def create_agent(self) -> Type:

        prompt = self.get_prompt_template_for_agent() #accessed from LanguageModelManager class

        llm_with_tools = self.bind_llm_with_tools() #accessed from this class

        agent = (

        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_openai_function_messages(
                x["intermediate_steps"]
            ),
            "chat_history": lambda x: x["chat_history"],
        }
        | prompt
        | llm_with_tools
        | OpenAIFunctionsAgentOutputParser()
        )

        return agent
    
    
    #make the agent executor - this will be used for conversations in main function
    def create_agent_executor(self) -> Type:

        tools = self.tools

        agent = self.create_agent()

        agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True)

        return agent_executor
    








        








        



