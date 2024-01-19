import os
import pyttsx3
import speech_recognition as sr
from elevenlabs import Voice,VoiceSettings



""" Jarvis speech including his voice and listening abilities are maintained from here, 
by utilizing pytts3 and Google's speech recognition system. This means his ears require an API to function.

ElevenLabs API can also be integrated here."""

class Speech_and_Voice:
    

    #speech engine
    voicebox = pyttsx3.init()
    
    #speech recognition
    def recognize_speech():

        # Create a recognizer object

        recognizer = sr.Recognizer()

        # Use the default microphone as the audio source
        with sr.Microphone() as source:

            print("Say something:")

            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            
            try:
                # Capture audio from the microphone
                audio = recognizer.listen(source, timeout=100)
                print("Got it! Processing...")

                # Use Google Web Speech API to recognize the audio
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text

            except sr.UnknownValueError:
                print("Sorry, couldn't understand what you said.")
                
                
            except sr.RequestError as e:
                print(f"Could not request results from Google Web Speech API; {e}")


    #elevenlabs 
                    
    voice = Voice(

        voice_id = "ig5dwxV3TesVspR3Zzh2", #change voice id here
        settings = VoiceSettings(
            stability = 1,
            similarity_boost = 0.5,
            style = 0.0,
            use_speaker_boost = True

            )
        )
        

#Use elevenlabs API if need be - voice settings can be managed from this class and generation can be carried out in the main function
                #you will substitute ptts3 engine with elevenlabs, note to import set_api_key, play and generate for functionality.
