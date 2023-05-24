# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:39:04 2022

@author: user
"""


# import required module
import speech_recognition as sr

def anup():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='hi-In')

            # for listening the command in indian english
            print("the query is printed='", Query, "'")


        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return Query


# call the function
anup()
