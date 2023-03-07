import settings
from pathlib import Path


#Save conversation between user and chatgpt to txt file

def append_chat_logs(file_name, prompt, response):
	file_in = open(file_name, 'a')
	user_input = (f"{settings.username}: {prompt}")
	ai_output = (f"{settings.ai_username}: {response}")
	file_in.write(user_input+"\n\n"+ai_output+"\n\n")
            
	file_in.close()


def record_blog_post(file_name, prompt, response):
	file_in = open(file_name, 'a')
	user_input = (f"{settings.username}: Write a blog post about: {prompt}")
	ai_output = (f"{settings.ai_username}: {response}")
	file_in.write(user_input+"\n\n"+ai_output+"\n\n")
            
	file_in.close()

def blog_coach_saved(file_name, response):
	file_in = open(file_name, 'w')
	ai_output = (f"{response}")
	file_in.write(ai_output)
	file_in.close()


def greeting_saved(file_name, response):
	file_in = open(file_name, 'w')
	ai_output = (f"{response}")
	file_in.write(ai_output)
	file_in.close()