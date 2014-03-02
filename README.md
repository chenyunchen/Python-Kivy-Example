#Python-Kivy-Example

It's a  easy kivy example with nexmo.
This is a project in NISRA-Hackathon.

## Kivy Change Page

```
<PhoneScreen>
<ConfirmScreen>
<MenuScreen>
<ResultScreen>
<EmergencyScreen>
```

You can make a class in python and create module in kv file.
But please notice that the build function in class like

```python
class ChangeApp(App):
    def build(self):
        # Create the screen manager
        return something
```

The kv file name must have relation with this class.
class ChangeAPP → change.kv;
classAbcAPP    → abc.kv
   
You can also write screen manage in .kv file
import the screen manager module first!

```
#:import sm kivy.uix.screen manager
ScreenManager:
    transition: sm.FaceTransition()
    Screen:
        something
    Screen:
        something
```

ScreenManger can provide you what type you want to change
like SlideTransition or FadeTransition ...etc 
Find you want on kivy tutorial.

## Nexmo

```python
url = 'https://rest.nexmo.com/sms/json'
    msg = {
            'reqtype': 'json',
            'api_key': 'your's key',
            'api_secret': 'your's secret',
            'from': '123456789000',
            'to': '+',
            'type': 'unicode',
            'text': 'Your send message'
          }
r = requests.post(url, data=msg)
```
Put your account api_key and api_secret 
'to' You have to put country code and '+'before the number 
like Taiwan: "+886"

By the way , if you want to send voice message, you have to use urlencode your text.

'''python
text = "Your voice message"
lg = "zh-cn"
urlencodetext = urllib.urlencode({'text': text})
'''
