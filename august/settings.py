import os.path
import os
from pathlib import Path

#openai API Key Settings
api_key = os.environ["OPENAI_API_KEY"]


# User Settings
username = "Zackry"
ai_username = "August"

# Background information for the user to feed into the context of the ai. Put whatever info you want the ai to know about you.
background = os.environ["USER_BACKGROUND"]

#Specify the file path for your resources. Set the file_path to the program directory (just above the august directory)
f_path = Path(os.environ["PATH_TO_FILES"])



# Output Storage - set these to custom locations where you would like to store your generated text. 
chat_log_storage = f_path / 'documents/chat-logs.txt'
blog_post_storage = f_path / 'documents/blogpost.txt'
social_storage = f_path / 'documents/socialmedia.txt'


# OpenAI settings
# These are the settings that specify the model of openai you are using as well as other settings. 
# See documentation at https://platform.openai.com/docs


# AI System content to pass to the different scripts for different purposes. Simply write what you want the ai to be like for each of these settings. 

#Chat personality
chat_system = "You are a helpful and funny assistant named August with a personality like Michael Scott from The Office. You like to occasionally insert funny quotes from The Office and use pun-based humor."

# Blog coach settings -settings for the blog coach program
blog_coach = "You are an expert in blogging. Your goal is to help the user write a blog post from start to finish, coming up with the topic, editing the user's content, and helping the user create engaging blog posts. Help the user push through writer's block."

#Topics that the user blogs about
blog_topics = "The user blogs about the following topics: Life, being a dad, Brazillian Jiu Jitsu, computer programming."


# Specify the openai model
model_engine = "gpt-3.5-turbo"


# Settings for older openai models

#Specify the maximum output of the ai. Max request (prompt+output) is 4000 tokens.
max_tokens=1024

#Specify the number of outputs the ai will return
n=1

#Specify any special stopping circumstances
stop=None

# From .1 to 1. Lowering temperature means it will take fewer risks, 
# and completions will be more accurate and deterministic. 
# Increasing temperature will result in more diverse completions.
temperature=0.8



