# -*- coding: utf-8 -*- 
import requests
info = requests.get('http://sparta-game-bot.herokuapp.com/api/heroes/361243026')
s = info.text
s = s.encode('utf-8')
with open('data.json', 'w') as f:
    f.write(s)