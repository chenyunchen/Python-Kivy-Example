# -*- coding: utf-8 -*-

import kivy
kivy.require("1.0.5")

import urllib
import requests
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# Declare both screens
class PhoneScreen(Screen):
    pass
class ConfirmScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
class ResultScreen(Screen):
    pass
class EmergencyScreen(Screen):
    def emergency(self):
        api_key = ""
        api_secret = ""
        to = "+"
        text = "警告! 警告! 預計老師將於稍後點名! 請同學火速趕至教室上課! 謝謝"
        lg = "zh-cn"
        urlencodetext = urllib.urlencode({'text': text})
        requests.post('https://rest.nexmo.com/tts/json?api_key='+api_key+'&api_secret='+api_secret+'&to='+to+'&'+urlencodetext+'&lg='+lg)
        to = "+"
        requests.post('https://rest.nexmo.com/tts/json?api_key='+api_key+'&api_secret='+api_secret+'&to='+to+'&'+urlencodetext+'&lg='+lg)
class FinalScreen(Screen):
    def pressmsg(self):
        endpoint = 'https://rest.nexmo.com/sms/json'
        msg = {
                'reqtype': 'json',
                'api_key': '',
                'api_secret': '',
                'from': '123456789000',
                'to': '+',
                'type': 'unicode',
                'text': '您好，在此提醒您，您將在 14:35 有 專題發表 這個事件，謝謝'
             }
        r = requests.post(endpoint, data=msg)

    def pressvoice(self):
        api_key = ""
        api_secret = ""
        to = "+"
        text = "您好，在此提醒您，您將在 14:35 有 專題發表 這個事件，謝謝"
        lg = "zh-cn"
        urlencodetext = urllib.urlencode({'text': text})
        requests.post('https://rest.nexmo.com/tts/json?api_key='+api_key+'&api_secret='+api_secret+'&to='+to+'&'+urlencodetext+'&lg='+lg)

class ChangeApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(PhoneScreen(name='phone'))
        sm.add_widget(ConfirmScreen(name='confirm'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ResultScreen(name='result'))
        sm.add_widget(EmergencyScreen(name='emergency'))
        sm.add_widget(FinalScreen(name='final'))
        return sm

if __name__ == '__main__':
    ChangeApp().run()
