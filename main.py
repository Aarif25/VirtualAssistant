import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib
import aiResponse  # new import

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open apna college" in c.lower():
        webbrowser.open("https://www.apnacollege.in/start")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLib.songs.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, song not found.")
    else:
        
        response = aiResponse.chat_with_gpt(c)
        print("GPT:", response)
        speak(response)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    r = sr.Recognizer()
    while True:
        print("Recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
                word = r.recognize_google(audio)
                print(word)

            if word.lower() == "hello":
                speak("Yes, how can I help you?")
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("You said:", command)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Other error: {e}")
