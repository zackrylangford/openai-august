import openai
from datetime import datetime
import os.path
import settings
from commands import *
from functions import *
from pathlib import Path


#Import API Key from settings
openai.api_key = settings.api_key

# Initial Greeting and prompt based on time of day
now = datetime.now()
now = int(now.strftime('%H%M'))

if now < 1200:
    user_greet = "Good morning, August!"
elif now <= 1700:
    user_greet = "Good afternoon, August!"
else:
    user_greet = "Good evening, August!"

greeting(f"{user_greet}")


prompt = input(f"\n{settings.username}: ")

# Conversation Loop
while prompt != '--quit':

    if prompt == '--blog':
        blog_post(prompt)
        prompt = input(f"\n{settings.username}: ")

    elif prompt == '--romeo':
        romeo(prompt)
        prompt = input(f"\n{settings.username}: ")

    elif prompt == '--coach':
        blog_coach(prompt)
        prompt = input(f"\n{settings.username}: ")
        
    else:
        open_chat(prompt)
        prompt = input(f"\n{settings.username}: ")



