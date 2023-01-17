from datetime import datetime
import JarvisAI
import re
import pprint
import random

obj = JarvisAI.JarvisAssistant()


def t2s(text):
    obj.text2speech(text)

# wakeWord = obj.mic_input()
# if re.search('jarvis wake up|jarvis I need you|jarvis', wakeWord):


'''
initiate greeting sequence to be played on jarvis startup
'''


def greet():
    greet_text = ""
    "for full date message"
    # weekday=datetime.ctime(datetime.now())
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        greet_text = "Good Morning Sir. "
    elif hour >= 12 and hour < 18:
        greet_text = "Good Afternoon Sir. "
    else:
        greet_text = "Good Evening Sir. "
    # greet_text+="Today is the {}".format(weekday)

    if hour > 12:
        greet_text += "It's "+str(hour-12)+" " + \
            str(datetime.now().minute)+" PM "+" now."
    else:
        greet_text += "It's "+str(hour)+" " + \
            str(datetime.now().minute)+" AM "+" now."

    # fetch and retuens current weather conditions for Dakhla
    greet_text += obj.weather("dakhla")
    return greet_text


# executes greet function
t2s(greet())

res = obj.mic_input()

while res:

    res = obj.mic_input()

    if re.search('weather|temperature', res):
        city = res.split(' ')[-1]
        weather_res = obj.weather(city=city)
        print(weather_res)
        t2s(weather_res)

    if re.search('news', res):
        news_res = obj.news()
        pprint.pprint(news_res)
        t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
        t2s(news_res[0])
        t2s(news_res[1])

    if re.search('tell me about', res):
        topic = res.split(' ')[-1]
        wiki_res = obj.tell_me(topic)
        print(wiki_res)
        t2s(wiki_res)

    if re.search('date', res):
        date = obj.tell_me_date()
        print(date)
        t2s(date)

    if re.search('time', res):
        time = obj.tell_me_time()
        print(time)
        t2s(time)

    if re.search('jokes', res):
        obj.jokes()

    if re.search('search in youtube for', res) or re.search('searching in youtube for', res) or re.search('search youtube for', res):
        search = res.split(' ')[-1]
        t2s("searching for "+search+" in youtube")
        open_result = obj.website_opener(
            "youtube.com/results?search_query="+search)

    if re.search('search in google for', res) or re.search('searching in google for', res) or re.search('search google for', res) or re.search('google search for', res):
        search = res.split(' ')[-1]
        t2s("searching for "+search+" in google")
        open_result = obj.website_opener(
            "google.com/results?search_query="+search)

    if re.search('open directory name', res):
        dict_dir = {
            'games': 'C:\\Users\lenovo\Desktop\Games',
            'dev tools': 'C:\\Users\lenovo\Desktop\Dev Tools'
        }

        dir = res.split(' ', 1)[1]
        path = dict_dir.get(dir)
        if path is None:
            t2s('Directory path not found')
            print('dir path not found')
        else:
            t2s('opening: ' + dir)
            obj.open_any_dir(path)

    if re.search('open', res):
        domain = res.split(' ')[-1]
        t2s("Opening "+domain)
        if domain == "facebook" or "youtube" or "gmail":
            open_result = obj.website_opener(domain + ".com")
        else:
            open_result = obj.website_opener(domain)
            print(open_result)

    if re.search('launch', res):
        dict_app = {
            'chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
            'league': 'E:\Riot Games\League of Legends\LeagueClient.exe',
            'yogi': 'E:\Games\Yu-Gi-Oh.Legacy.of.the.Duelist.Link.Evolution-GoldBerg\Yu-Gi-Oh! Legacy of the Duelist Link Evolution\YuGiOh.exe'
        }

        app = res.split(' ', 1)[1]
        path = dict_app.get(app)
        if path is None:
            t2s('Application path not found')
            print('Application path not found')
        else:
            t2s('Launching: ' + app)
            obj.launch_any_app(path_of_app=path)

    if re.search('close', res):
        dict_app = {
            'chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
            'league': 'E:\Riot Games\League of Legends\LeagueClient.exe',
            'yogi': 'E:\Games\Yu-Gi-Oh.Legacy.of.the.Duelist.Link.Evolution-GoldBerg\Yu-Gi-Oh! Legacy of the Duelist Link Evolution\YuGiOh.exe'
        }

        app = res.split(' ', 1)[1]
        path = dict_app.get(app)
        if path is None:
            t2s('Application already closed')
            print('Application already closed')
        else:
            t2s('Closing: ' + app)
            obj.close_any_app(path_of_app=path)

    if re.search('hello', res):
        print('Hi')
        t2s('Hi')

    if re.search('how are you', res):
        li = ['good', 'fine', 'great']
        response = random.choice(li)
        print(f"I am {response}")
        t2s(f"I am {response}")

    if re.search('what is your name|who are you', res):
        print("My name is Jarvis, I am your personal assistant")
        t2s("My name is Jarvis, I am your personal assistant")

    if re.search('initiate standby mode|standbymode', res):
        obj.standbyMode()

    if re.search('shut down', res):
        obj.shutdown()

    if re.search('open my gmail', res):
        open_result = obj.website_opener("gmail.com")
        print(open_result)

    if re.search('what can you do', res):
        li_commands = {
            "open websites": "Example: 'open youtube.com",
            "time": "Example: 'what time it is?'",
            "date": "Example: 'what date it is?'",
            "launch applications": "Example: 'launch chrome'",
            "tell me": "Example: 'tell me about India'",
            "weather": "Example: 'what weather/temperature in Mumbai?'",
            "news": "Example: 'news for today' ",
        }
        ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
        I can open websites for you, launch application and more. See the list of commands-"""
        print(ans)
        pprint.pprint(li_commands)
        t2s(ans)
