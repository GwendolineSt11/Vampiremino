import os
from pymino import Bot, Client
from pymino.ext import *
import logging
import pytz
import datetime
import json
from datetime import datetime
import amino
from amino.id import Id
import requests


bot = Bot(
    command_prefix="!",
    community_id='210127143',
    console_enabled=True,
    device_id='19DDCCD74FD9DAF165A96046950D899B1CB1FE1D0B8A1BA53C914175EE59D36D106C7AA7396A521EC3',
    device_key='E7309ECC0953C6FA60005B2765F99DBBC965C8E9',
    signature_key='DFA5ED192DDA6E88A12FE12130DC6206B1251E44',
    service_key='c22b5523-e67e-4460-8bb1-92a8cb3b0112',
    intents=True,
    online_status=True,
    proxy="https://vampiremino-21656f34130d.herokuapp.com/interactions/"
    )
chatId = ''
tz = pytz.timezone('America/Mexico_City')

response = requests.get('https://vampiremino-21656f34130d.herokuapp.com/interactions/')
try:
    data = response.json()
except json.decoder.JSONDecodeError as e:
    print(f"JSON decode error: {e}")
    print(f"Response content: {response.text}")
    print(f"Response status code: {response.status_code}")


@bot.on_ready()
async def on_ready():
    print(f"Logged in as {bot.profile.username}")


#@bot.task(interval=60)
#async def task(ctx, fecha_desde: str, fecha_hasta: str):
    #chat = bot.fetch_chat(chatId)
    #fecha_desde = datetime.strptime(fecha_desde, '%Y-%m-%d').replace(tzinfo=tz)
    #fecha_hasta = datetime.strptime(fecha_hasta, '%Y-%m-%d').replace(tzinfo=tz)
    #if bot.is_ready:
        #with open('mensajes_extraidos.txt', 'w', encoding='utf-8') as file:
            #async for message in chat.history(after=fecha_desde, before=fecha_hasta, limit=None):
                #file.write(f'{message.author}: {message.content}\n')
    #print(f"An order of extracted messages on its way!\n From: {chatId}.")


@bot.on_error()
async def on_error(error: Exception):
    print(f"An error occurred: {error}")

bot.run("kikikhristine@hotmail.com", "TheHuntress4nn4")
