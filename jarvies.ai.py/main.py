import speech_recognition as sr
import pyttsx3
import openai
import datetime
import webbrowser
import os
import platform
import psutil
import subprocess

# Set OpenAI API Key
openai.api_key = "your-api-key"  # Replace with your OpenAI API key

# Initialize speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and return text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # To handle background noise
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        print("Sorry, there is an issue with the speech recognition service.")
        return ""

# Function to get a response from OpenAI GPT
def generate_response(prompt):
    try:
        # Using the chat-based interface (ChatCompletion)
        response = openai.chat.Completion.create(
            model="gpt-3.5-turbo",  # Use the appropriate model (gpt-4 is also available)
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "Sorry, I couldn't process your request."

# Function to handle meeting-related commands
def handle_meeting_commands(command):
    if "start a meeting" in command:
        speak("Starting a new meeting.")
        webbrowser.open("https://meet.jit.si/YourMeetingRoom")  # Replace with your meeting link
    elif "join a meeting" in command:
        speak("Please tell me the meeting link.")
        meeting_link = listen()
        if meeting_link:
            speak("Joining the meeting.")
            webbrowser.open(meeting_link)
    elif "share the screen" in command:
        speak("To share the screen, please click the share screen button in your meeting interface.")
    elif "end meeting" in command:
        speak("Ending the meeting. Please close the meeting tab in your browser.")


# Function to execute various commands
def execute_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "open browser" in command or "search" in command:
        speak("Opening web browser.")
        webbrowser.open("https://www.google.com")
        speak("What would you like to search for?")
        search_query = listen()  # Wait for search query after opening the browser
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Searching for {search_query}")
    elif "play music" in command:
        speak("Playing music.")
        os.system("open -a Music")  # macOS command
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com", new=2)  # Opens in default browser
        speak("What would you like to search for on YouTube?")
        search_query = listen()  # Wait for search query after opening YouTube
        if search_query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            speak(f"Searching for {search_query} on YouTube.")
    elif "open facebook" in command:
        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com", new=2)  # Opens in default browser
    elif "open twitter" in command:
        speak("Opening Twitter.")
        webbrowser.open("https://www.twitter.com", new=2)  # Opens in default browser
    elif "open email" in command:
        speak("Opening Gmail.")
        webbrowser.open("https://mail.google.com", new=2)  # Opens in default browser
    elif "open terminal" in command:
        speak("Opening Terminal.")
        os.system("open -a Terminal")  # macOS command to open Terminal
    elif "open safari" in command:
        speak("Opening Safari.")
        os.system("open -a Safari")  # Opens Safari
    elif "open chrome" in command:
        speak("Opening Google Chrome.")
        os.system("open -a 'Google Chrome'")  # Opens Google Chrome
    elif "open firefox" in command:
        speak("Opening Mozilla Firefox.")
        os.system("open -a 'Firefox'")  # Opens Firefox
    elif "open textedit" in command:
        speak("Opening TextEdit.")
        os.system("open -a TextEdit")  # Opens TextEdit
    elif "open pages" in command:
        speak("Opening Pages.")
        os.system("open -a Pages")  # Opens Pages (Apple word processor)
    elif "open numbers" in command:
        speak("Opening Numbers.")
        os.system("open -a Numbers")  # Opens Numbers (Apple spreadsheet application)
    elif "open keynote" in command:
        speak("Opening Keynote.")
        os.system("open -a Keynote")  # Opens Keynote (Apple presentation software)
    elif "open preview" in command:
        speak("Opening Preview.")
        os.system("open -a Preview")  # Opens Preview
    elif "open calendar" in command:
        speak("Opening Calendar.")
        os.system("open -a Calendar")  # Opens Calendar
    elif "open mail" in command:
        speak("Opening Mail.")
        os.system("open -a Mail")  # Opens Mail app
    elif "open contacts" in command:
        speak("Opening Contacts.")
        os.system("open -a Contacts")  # Opens Contacts
    elif "open notes" in command:
        speak("Opening Notes.")
        os.system("open -a Notes")  # Opens Notes
    elif "open reminders" in command:
        speak("Opening Reminders.")
        os.system("open -a Reminders")  # Opens Reminders
    elif "open maps" in command:
        speak("Opening Maps.")
        os.system("open -a Maps")  # Opens Maps
    elif "open messages" in command:
        speak("Opening Messages.")
        os.system("open -a Messages")  # Opens Messages
    elif "open photos" in command:
        speak("Opening Photos.")
        os.system("open -a Photos")  # Opens Photos
    elif "open vlc" in command:
        speak("Opening VLC Media Player.")
        os.system("open -a VLC")  # Opens VLC Media Player
    elif "shutdown" in command:
        speak("Shutting down the system.")
        os.system("sudo shutdown now")  # macOS command
    elif "restart" in command:
        speak("Restarting the system.")
        os.system("sudo reboot")  # macOS command
    elif "battery status" in command:
        battery = psutil.sensors_battery()
        percent = battery.percent
        speak(f"Battery is at {percent} percent.")
    elif "cpu usage" in command:
        cpu_percent = psutil.cpu_percent(interval=1)
        speak(f"CPU usage is at {cpu_percent} percent.")
    elif "memory usage" in command:
        memory = psutil.virtual_memory()
        speak(f"Memory usage is at {memory.percent} percent.")
    elif "disk usage" in command:
        disk = psutil.disk_usage('/')
        speak(f"Disk usage is at {disk.percent} percent.")
    elif "close window" in command:
        speak("Closing the current window.")
        os.system("osascript -e 'tell app \"System Events\" to keystroke \"w\" using command down'")  # macOS
    elif "close all windows" in command:
        speak("Closing all windows.")
        if platform.system() == "Windows":
            os.system("taskkill /F /IM explorer.exe")  # Close all windows in Windows
            os.system("start explorer")  # Restart Windows Explorer to restore the taskbar
        elif platform.system() == "Darwin":  # macOS
            os.system("osascript -e 'tell application \"System Events\" to keystroke \"q\" using command down'")
        elif platform.system() == "Linux":
            os.system("pkill -9 -u $USER")  # Close all windows in Linux
    elif "minimize window" in command:
        speak("Minimizing the current window.")
        if platform.system() == "Darwin":  # macOS
            os.system("osascript -e 'tell app \"System Events\" to keystroke \"m\" using command down'")
        elif platform.system() == "Windows":  # Windows
            os.system("nircmd sendkeypress alt+space minimize")
        elif platform.system() == "Linux":
            os.system("xdotool getactivewindow windowminimize")  # Minimize the active window
    elif "exit" in command or "quit" in command:
        speak("It was a pleasure assisting you. Take care and have a great day!")
        exit()  # Stop the assistant

    elif "open settings" in command or "open system preferences" in command:
        speak("Opening System Preferences.")
        os.system("open -a 'System Preferences'")  # Opens System Preferences
    elif "open wifi" in command:
        speak("Opening Wi-Fi settings.")
        os.system("open -b com.apple.preference.network")  # Opens Wi-Fi Preferences
    elif "open bluetooth" in command:
        speak("Opening Bluetooth settings.")
        os.system("open -b com.apple.preference.bluetooth")  # Opens Bluetooth Preferences
    elif "open sound" in command:
        speak("Opening Sound settings.")
        os.system("open -b com.apple.preference.sound")  # Opens Sound Preferences
    elif "open display" in command:
        speak("Opening Display settings.")
        os.system("open -b com.apple.preference.displays")  # Opens Display Preferences
    elif "open keyboard" in command:
        speak("Opening Keyboard settings.")
        os.system("open -b com.apple.preference.keyboard")  # Opens Keyboard Preferences
    elif "open date and time" in command:
        speak("Opening Date and Time settings.")
        os.system("open -b com.apple.preference.datetime")  # Opens Date & Time Preferences
    elif "open security" in command:
        speak("Opening Security & Privacy settings.")
        os.system("open -b com.apple.preference.security") 
    else:
        response = generate_response(command)
        speak(response)

# Main function to run the assistant
def assistant_loop():
    speak("Hello, I am your A.I assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            execute_command(command)
        if "exit" in command or "quit" in command:
           speak("It was a pleasure assisting you. Take care and have a great day!")
           break

# Run the assistant
if __name__ == "__main__":
    assistant_loop()