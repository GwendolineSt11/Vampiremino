import os
from pymino import Bot, Client
from pymino.ext import *
import logging
import pytz
import datetime
from datetime import datetime
import amino
from amino.id import Id
import requests


bot = Bot(
    command_prefix="!",
    community_id='super_mario',
    console_enabled=True,
    device_id='0136a754f2e4de68cbb2a5f94632bb04bafc0c0c4d73b364af2c9e1b0d2da51b840416c96592cabb7e',
    device_key='c1caaf081376b4bc83df15ef7deda917a4b56f55',
    signature_key='a5200a71589409a4629dda94c5ae9ee91bd7a2d0',
    service_key='c22b5523-e67e-4460-8bb1-92a8cb3b0112',
    intents=True,
    online_status=True,
    proxy="http://127.0.0.1:8000"
    )
chatId = ''
tz = pytz.timezone('America/Mexico_City')


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
