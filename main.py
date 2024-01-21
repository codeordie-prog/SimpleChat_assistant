
from speech_and_voice import Speech_and_Voice as sv
from agenttools import AgentTools as agent
from agentmanager import Agent
from langchain_core.messages import AIMessage, HumanMessage
import sys,os


agent_manager_tool = Agent()

#introduce the instances here

voicebox = sv.voicebox #for speech
conversation = agent_manager_tool.agent_executor #for executing conversation


#chat history

chat_history = []

def main():
    
    
    try:

        mode = int(input(" Choose mode to engage with JARVIS :\n1.speech\n2.text\n "))

        if mode == 1:

            intro()
            chat()
            
        elif mode == 2:

            intro()
            text()

        else:
            
            print(" enter either 1 or 2 ")
            main()

    except TypeError:

        print("choose 1 or 2")
        main()

    except ValueError:

        print("wrong value ")
        main()

def intro():

    try :

        introduction_request = "In less than 4 short sentences introduce yourself. do not exceed 4 short sentences"

        response = conversation.invoke({"input": introduction_request,"chat_history": chat_history})
        chat_history.extend(
        [
            HumanMessage(content=introduction_request),
            AIMessage(content=response["output"]),
        ]
        )
        voicebox.say(response["output"])
        voicebox.runAndWait()

    except TypeError:
        pass


#sends queries to JARVIS and speaks the responses    
def send_query(query_input : str ):

    response = conversation.invoke({"input" : query_input, "chat_history": chat_history})

    chat_history.extend(
        [
            HumanMessage(content=query_input),
            AIMessage(content=response["output"]),
        ]
        )
       
    print(response["output"])

    voicebox.say(response["output"])
    voicebox.runAndWait()

# says a goodbye when asked to stop or asks the user to say something  
def default_responses(response : str ):

    print(response)
    voicebox.say(response)
    voicebox.runAndWait()



def chat():

    try:

        #introduce an infinite loop

        while(True):

            query = sv.recognize_speech()

            if query != None :

                if query == 'stop':

                    default_responses(response = "ok boss, goodbye, let us catch up later")
                    sys.exit()


                else :

                    send_query(query)
                    
            
            else:

                default_responses(response = "please say something")
                chat()

    except TypeError:
        
        print("make sure you say something")
        chat()


def text():

    try:

        while(True):

            user_input = input("Enter query : ").strip("")

            if user_input != None:

                if user_input == 'stop':

                    default_responses(response = "Ok boss, Goodbye, Talk later")
                    sys.exit()

                else:

                   send_query(user_input)

            else:

                default_responses(response = "please type something")
                text()



    except TypeError:

        print("enter query")
        text()



if __name__ == "__main__":

    main()