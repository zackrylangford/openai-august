import settings
from pathlib import Path


#Save conversation between user and chatgpt to txt file

def append_chat_logs(file_name, prompt, response):
	file_in = open(file_name, 'a')
	user_input = (f"{settings.username}: {prompt}")
	ai_output = (f"{settings.ai_username}: {response}")
	file_in.write(user_input+"\n\n"+ai_output+"\n\n")
            
	file_in.close()

# Save quick write blog post
def record_blog_post(file_name, prompt, response):
	file_in = open(file_name, 'a')
	user_input = (f"{settings.username}: Write a blog post about: {prompt}")
	ai_output = (f"{settings.ai_username}: {response}")
	file_in.write(user_input+"\n\n"+ai_output+"\n\n")
            
	file_in.close()

# Save blog coach blog post 

def blog_coach_saved(file_name, response):
	file_in = open(file_name, 'w')
	ai_output = (f"{response}")
	file_in.write(ai_output)
	file_in.close()

# Add generated tweets to bottom of blog coach blog post

def add_tweets(file_name, tweets):
	"""Adds social media posts to the bottom of the blog post file"""
	file_in = open(file_name, 'a')
	ai_output = (f"\n\nTweet Ideas:\n\n{tweets}")
	file_in.write(ai_output)
	file_in.close()

# Add generated LinkedIn post to bottom of blog coach post

def add_linked(file_name, linked):
	"""Adds social media posts to the bottom of the blog post file"""
	file_in = open(file_name, 'a')
	ai_output = (f"\n\nLinkedIn Post Idea:\n\n{linked}")
	file_in.write(ai_output)
	file_in.close()

# Add keywords and url generated for image generation to bottom of blog coach post

def add_keywords(file_name, key_words):
	"""Adds keywords generated for image at bottom of the blog post file"""
	file_in = open(file_name, 'a')
	ai_output = (f"\n\nImage Keywords:\n\n{key_words}")
	file_in.write(ai_output)
	file_in.close()
	print(f"The following keywords were generated for your image: {key_words}")

def add_url(file_name, url):
	"""Adds image url to the bottom of the blog post file"""
	file_in = open(file_name, 'a')
	ai_output = (f"\n\nImage URL:{url}")
	file_in.write(ai_output)
	file_in.close()

# Save the greeting of August for future reference in chat

def greeting_saved(file_name, response):
	file_in = open(file_name, 'w')
	ai_output = (f"{response}")
	file_in.write(ai_output)
	file_in.close()




