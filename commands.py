import datetime
import wikipedia
import webbrowser
import pyjokes
import requests
import os
import pyautogui
from voice import speak, listen

def execute_command(query):
    if "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")
    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")
    elif "wikipedia" in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    elif "open youtube" in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open google" in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open github" in query:
        webbrowser.open("https://github.com")
        speak("Opening GitHub")
    elif "open chatgpt" in query:
        webbrowser.open("https://chatgpt.com")
        speak("Opening ChatGPT")
    elif "open gmail" in query:
        webbrowser.open("https://mail.google.com")
        speak("Opening Gmail")
    elif "open linkedin" in query:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")
    elif "search google" in query:
        speak("What should I search?")
        search = listen()
        if search:
            webbrowser.open(f"https://www.google.com/search?q={search}")
    elif "search youtube" in query:
        speak("What should I search on YouTube?")
        search = listen()
        if search:
            webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
    elif "joke" in query:
        speak(pyjokes.get_joke())
    elif "open calculator" in query:
        os.system("calc")
    elif "open notepad" in query:
        os.system("notepad")
    elif "screenshot" in query:
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        speak("Screenshot saved")
    elif "weather forecast" in query or "forecast" in query:
        speak("Which city should I check?")
        city = listen()
        if city:
            API_KEY = "adf3d6b26091626ba1cd77568f697268"
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
            data = requests.get(url).json()

            if "list" in data:
                speak(f"Here is the forecast for {city}")
                last_date = ""
                count = 0
                for item in data["list"]:
                    date = item["dt_txt"].split(" ")[0]
                    if date != last_date:
                        temp = item["main"]["temp"]
                        desc = item["weather"][0]["description"]
                        speak(f"{date}: {temp} degree Celsius with {desc}")
                        last_date = date
                        count += 1
                    if count == 5:
                        break
            else:
                speak("Unable to fetch forecast")
        else:
            speak("City not detected")
    elif "weather" in query:
        speak("Which city should I check?")
        city = listen()
        if city:
            API_KEY = "apikey"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            data = requests.get(url).json()
            if "main" in data:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                speak(f"{city} is {temp} degree Celsius with {desc}")
            else:
                speak("City not found")
        else:
            speak("City not detected")
    elif "news" in query:
        API_KEY = "apikey"
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
        data = requests.get(url).json()
        if "articles" in data:
            speak("Here are the top headlines")

            for article in data["articles"][:5]:
                speak(article["title"])

        else:
            speak("Unable to fetch news")
    else:
        return False
    return True
