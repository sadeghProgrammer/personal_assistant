#===============**************sadegh_assistant****************===================

#----------------+++imports+++----------

#in terminal: import: 1.SpeechRecognition   2.gtts  3.playsound     4.pyaudio
from _socket import timeout
from contextlib import redirect_stderr

import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import requests
import yfinance as yf

# ==================== Section_1:take sound and replace to text==================

crypto_api='https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Clitecoin%2Csolana&vs_currencies=usd'
def elii_listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio=r.listen(source,phrase_time_limit=4)
        text=''
        try:
            text=r.recognize_google(audio)
        except sr.RequestError as re:
            print(re)
        except sr.UnknownValueError as uve:
            print(uve)
        except sr.WaitTimeoutError as wte:
            print(wte)
    text=text.lower()
    return text

#=====================speack==========================
def elii_talk(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='en')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#==================-----reply-----=====================
def sadegh_reply(text):
    if 'what' in text and 'name' in text:
        elii_talk('my name is sadegh and I am your persional assistant')

    elif 'stop' in text :
        elii_talk('It was pleasure to help you, I wish you a wonderful day')
    elif 'why' in text and 'exist' in text:
        elii_talk('i was created to work for you')
    elif 'when' in text and 'sleep' in text:
        elii_talk('i never sleap.')
    elif 'you' in text and 'stupid' in text:
        elii_talk('no, I am not stupid.')
    elif 'favorite' in text or'favourite' in text and 'move' in text:
        elii_talk('my favorite movie is Titanic.')

# -------------------- crypto_API -----------------------------------------------
    elif 'bitcoin' in text:
        response = requests.get(crypto_api)
        crypto_json = response.json()
        elii_talk('the current price for Bitcoin is' + str(crypto_json['bitcoin']['usd'])+'us dollars')

    elif 'litecoin' in text:
        response = requests.get(crypto_api)
        crypto_json = response.json()
        elii_talk('the current price for litecoin is' + str(crypto_json['litecoin']['usd'])+'us dollars')

    elif 'solana' in text:
        response = requests.get(crypto_api)
        crypto_json = response.json()
        elii_talk('the current price for solana is' + str(crypto_json['solana']['usd'])+'us dollars')
    # -------------------- crypto_API -----------------------------------------------

    elif 'apple' in text:
        apple = yf.Ticker('AAPL')
        print(apple.info['regularMarketPrice'])
        elii_talk('at this moment you can purchase one apple share for ' + str(apple.info['regularMarketPrice'])+'US Dollars')

    elif 'facebook' in text:
        facebook = yf.Ticker('FB')
        print(facebook.info['regularMarketPrice'])
        elii_talk('at this moment you can purchase one facebook share for ' + str(facebook.info['regularMarketPrice'])+'US Dollars')

    elif 'tesla' in text:
        tesla = yf.Ticker('TSLA')
        print(tesla.info['regularMarketPrice'])
        elii_talk('at this moment you can purchase one tesla share for ' + str(tesla.info['regularMarketPrice'])+'US Dollars')


    else:
        elii_talk('Excuse me, I did not get that. Can ou please repeat it?')


#==================-----assistant-----=====================
def excute_assistant():
    elii_talk('Hi, I am heare to support you. Can you please tell me your name?')
    listen_name=elii_listen()
    elii_talk('Hi '+listen_name+'what can I do for you?')
    while True:
        listen_sadegh=elii_listen()
        print(listen_sadegh)
        sadegh_reply(listen_sadegh)



        if 'stop' in listen_sadegh:
            break


excute_assistant()

#==================-----API-----=====================

crypto_api='https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Clitecoin%2Csolana&vs_currencies=usd'
response=requests.get(crypto_api)
crypto_json=response.json()
