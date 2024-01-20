
# Simple Chat assistant powered by ChatGPT 

This is a simple chat assistant created using OpenAI ChatGPT API, Google speech_recognition API, pytts3x library and Langchain framework

1. ChatGPT API - gives the assistant reasoning capabilities
2. Google's speech_recognition - gives the assistant listening capabilities
3. pyttsx3 library - gives the assistant voice capabilities - note this can be easily substituted with other tools like elevenlabs API
4. Langchain framework - enables the creation of tools that the llm can use, memory, prompt for context and many other capabilities some yet
                    to be added like document loading for helping with different documents.

it uses personal data to make association tailored in accordance to the user needs - e.g in my case i use interests, goals to make tools for the agent that it can use when needed - this is completely open for customization with respect to data you choose to feed the agent.

You can run the main.py file and choose interaction mode - speech or text

# Notes

1. File database.py - has paths to user documents - you can create a json file with any information you wish to give the assistant access to,   this may include personal interests that the assistant can reference from to make your association tailored according to your needs.

2. File dbfileoperations.py - has functions that retrieve information from the data you choose to create in database.py.
                            - These functions can be modified with respect to the kind of data fed to the assistant, in my case i chose to list  my profile, interests and goals in several aspects of my life

3. File agenttools.py - has the tools for the model. The agent uses these tools when only there is need. e.g when prompted through the chat
                    conversation to recommend a book, it will reference to the user's interests by utilizing the tool "get_book_interests" and through the information provided, it will recommend a book within the interests of the user.

4. File  llm_manager.py - has classes associated with the properties of the llm - these include prompt, prompt_template and other properties.
                    if need be to adjust or change the prompt for the llm, it can be modified from this file

5. File speech_and_voice.py - has the Google speech recognition API function, and pyttsx3 voice settings. Any other voice tool can be added here
                             e.g elevenlabs AI tools can be added from here


