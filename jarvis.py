import pyttsx3 #pip install pyttsx3 (offline)
import speech_recognition as sr #pip install speechRecognition
import datetime #show date time)
import wikipedia #pip install wikipedia
import webbrowser  #for browser)
import os
import winshell
import pyjokes # for jokes
import ctypes #windows bypass lock windows



engine = pyttsx3.init('sapi5')                            #API MS (V) SAP
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    assname="king"
    speak("I am King 1.0 .  I am your Assistant Sir, Please tell me how may I help you")       


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")    

        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = mycommand();

    return command


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        command = takeCommand().lower()

        # Logic for executing tasks based on command
        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in command:
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in command:
            webbrowser.open("stackoverflow.com")   


        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'open twitter' in command:
            webbrowser.open("twitter.com")

        elif 'open my channel' in command:
            webbrowser.open("https://studio.youtube.com/channel/UCnQoG_Eh_aS1FkktMQXckoA")   

        elif 'open w3school' in command:
            webbrowser.open("www.w3schools.com")

        elif 'play music' in command:
            music_dir = 'F:\\F\\ALL Audio Song\\new song'
            songs = os.listdir(music_dir)
            print(songs)    
            random= os.startfile(os.path.join(music_dir, songs[1]))

        elif 'how are you' in command: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir")   

        elif 'jokes' in command: 
            speak(pyjokes.get_joke()) 

        elif 'exit' in command or 'go back' in command: 
            speak("Thanks for giving me your time") 
            exit()    

        elif 'fine' in command or "good" in command: 
            speak("It's good to know that your fine")    

        elif "what is your name" in command: 
            speak("my name is King 1 point 0") 
            speak("please tell me how may I help you")    

        elif "who made you" in command or "who created you" in command:  
            speak("I have been created by Mr.akash.") 

        elif "who are you" in command: 
            speak("I am your virtual assistant. created by Mr.Akash.")        

        elif 'lock window' in command: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation()    

        elif 'empty recycle bin' in command: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled")        

        #elif "camera" in command or "take a photo" in command: 
            #ec.capture(0, "Jarvis Camera ", "img.jpg")    

        #elif "restart" in command: 
            #subprocess.call(["shutdown", "/r"])
       

        elif 'open facebook' in command:
            webbrowser.open("www.facebook.com")    

        elif 'who am i' in command:
            speak("your name is Mr.Akash")     

        elif 'search' in command or 'play' in command: 
              
            command = command.replace("search", "")         
            command = command.replace("play", "")   
            webbrowser.open(command)   

        elif 'open cam' in command or 'camtasia' in command: 
            codePath = 'C:\\Program Files (x86)\\TechSmith\\Camtasia Studio 8\\CamtasiaStudio.exe'
            os.startfile(codePath)    

        elif 'open photoshop' in command: 
            codePath = 'C:\\Program Files (x86)\\Adobe\\Photoshop 7.0\\Photoshop.exe'
            os.startfile(codePath)     

        elif "really" in command: 
            speak("yes")         