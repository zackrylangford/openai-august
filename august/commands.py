# This runs the blog coach feature, which prompts the user with questions to help the user write content for a blog post that is then edited and formatted into a completed blog post based on the specifications in the assistant settings.
import random
import openai
import settings
from datetime import datetime
from functions import *
from pathlib import Path
from settings import f_path
import os.path
import os


#Import API Key from settings
openai.api_key = settings.api_key

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%B %d, %Y %H:%M:%S")


def greeting(greeting):
    """Initial greeting when program starts"""
    completion = openai.ChatCompletion.create(
    model=settings.model_engine,
    messages=[
        {"role": "system", "content": f"{settings.chat_system}"},
        {"role": "assistant", "content": f"The current date and time is {dt_string}. Greet the user based on the current time. {settings.background}"},
        {"role": "user", "content": f"{greeting}"}
    ]
    )
    response = completion.choices[0].message.content
    print(f"\n{settings.ai_username}: {response.strip()}")

    #Save response in new variable for use in other conversations
    gs = f_path / "resources/.convo.txt"
    greeting_saved(f"{gs}",response.strip())

def open_chat(prompt):
    """General chat settings"""
    completion = openai.ChatCompletion.create(
    model=settings.model_engine,
    messages=[
        {"role": "system", "content": f"{settings.chat_system}"},
        {"role": "assistant", "content": f"The current date and time is {dt_string}. {settings.background}"},
        {"role": "user", "content": f"{prompt}"}
    ]
    )
    response = completion.choices[0].message.content

    # Print the response from ChatGPT in the terminal
    print(f"\n{settings.ai_username}: {response.strip()}")
    
    # Add conversation to txt logs
    append_chat_logs(f"{settings.chat_log_storage}", prompt, response.strip())

        


def blog_coach(prompt):
    """Will coach the user through the writing and publishing of a single blog post"""
    #Saved previous greeting
    file_path = f_path / "resources/.convo.txt"
    with open(file_path, 'r') as file:
        greet_saved = file.read()

        # Initial question to figure out what the user wants to blog about.
        completion = openai.ChatCompletion.create(
        model=settings.model_engine,
        messages=[
            {"role": "system", "content": f"{settings.blog_coach}"},
            {"role": "assistant", "content": f"Previous response:{greet_saved}.User Background: {settings.background}{settings.blog_topics} Ask the user which topic do they want to write about today and make a suggestion based on the user background and blog topics that the user typically blogs about."},
        ]
        )
        response = completion.choices[0].message.content
        print(f"\n{settings.ai_username}: {response.strip()}")

        user_prompt = input(f"\n{settings.username}: ")

    
        # Recieve the user input and prompt them with a writing prompt
        completion = openai.ChatCompletion.create(
        model=settings.model_engine,
        messages=[
            {"role": "system", "content": f"{settings.blog_coach}"},
            {"role": "assistant", "content": f"Previous conversation:{greet_saved}{response} {settings.background} "},
            {"role": "user", "content": f"Suggest three unique and specific writing prompts to get them started with their blog post about {user_prompt}"},
            ]
            )
        response = completion.choices[0].message.content
        print(f"\n{settings.ai_username}: {response.strip()}")

        user_prompt = input(f"\n{settings.username}: ")

        # Edit the user input for grammar, format it for a blog post, add a title and headings
        completion = openai.ChatCompletion.create(
        model=settings.model_engine,
        messages=[
        {"role": "system", "content": f"{settings.blog_coach}"},
        {"role": "assistant", "content": f"{response}{settings.background}"},
        {"role": "user", "content": f"Edit the following for grammar, expand and format into a blog post from my point of view, come up with a unique and creative title: {user_prompt}"},
        ]
        )
        response = completion.choices[0].message.content
    
    blog_coach_saved(f"{settings.blog_post_storage}", response.strip())
    print(f"\n{settings.ai_username}: {response.strip()}\n****\n\nThe above post was saved to a new file on your Desktop!")

    #Ask the user for optional Tweets derived from the blog post
    tweet_prompt = input(f"{settings.ai_username}: \n\nWould you like me to come up with some Tweets based on the blog post we just wrote? (y/n)")
    if tweet_prompt == "y":
        blog_path = f_path / "documents/blogpost.txt"
        with open(blog_path, 'r') as file:
            blog_saved = file.read()
            
            completion = openai.ChatCompletion.create(
            model=settings.model_engine,
            messages=[
                {"role": "system", "content": f"{settings.blog_coach}"},
                {"role": "assistant", "content": f"Blog post that we just wrote:{blog_saved}.{settings.username}'s background: {settings.background}"},
                {"role": "user", "content": f"Write 3-5 unique insights, funny sayings, or twitteresque type content from the blog post we just wrote based on {settings.username}'s background for {settings.username}'s Twitter account: {blog_saved}"},
            ]
            )
            response = completion.choices[0].message.content
        add_tweets(f"{settings.blog_post_storage}", response.strip())
        print(f"\n{settings.ai_username}: {response.strip()}\n****\n\nTweets were saved to your blog post file")

    linked_in = input(f"{settings.ai_username}: \n\nWould you like me to come up with some ideas for a LinkedIn post based on the blog post we just wrote? (y/n)")
    if linked_in == "y":
        blog_path = f_path / "documents/blogpost.txt"
        with open(blog_path, 'r') as file:
            blog_saved = file.read()
            
            completion = openai.ChatCompletion.create(
            model=settings.model_engine,
            messages=[
                {"role": "system", "content": f"{settings.blog_coach}"},
                {"role": "assistant", "content": f"Blog post that we just wrote:{blog_saved}.{settings.username}'s background: {settings.background}"},
                {"role": "user", "content": f"Write 2 unique LinkedIn posts from the following blog post using {settings.username}'s background for {settings.username}'s Twitter account: {blog_saved}"},
            ]
            )
            response = completion.choices[0].message.content
        add_linked(f"{settings.blog_post_storage}", response.strip())
        print(f"\n{settings.ai_username}: {response.strip()}\n****\n\nLinkedIn posts were saved to your blog post file")
        



def blog_post(prompt):
    """A quick blog post written by August"""
    prompt = input(f"\n{settings.ai_username}: What do you want to blog about?\n\n{settings.username}:  ")

    completion = openai.ChatCompletion.create(
    model=settings.model_engine,
    messages=[
        {"role": "user", "content": f"Write a blog post with paragraph headings about {prompt}"}
    ]
    )

    response = completion.choices[0].message.content

    # Print the response from ChatGPT in the terminal
    print(f"\n{settings.ai_username}: {response.strip()}")
    
    # Add conversation to txt logs
    record_blog_post(f"{settings.blog_post_storage}", prompt, response.strip())



# Location of Romeo and Juliet .txt file
file_path = f_path / "resources/romeo_juliet.txt"


def romeo(prompt):
    """Grab a random sample from Romeo and Juliet and feed it into August"""
    print(f"Processing the following excerpt from Romeo and Juliet:\n")
    with open(file_path, 'r') as file:
        lines = file.readlines()
        random_lines = random.sample(lines, 40)
        line_string = ''.join(random_lines)
        prompt = line_string

         # Print the excerpt to the terminal for reference
        print(prompt)

        completion = openai.ChatCompletion.create(
        model=settings.model_engine,
        
        # Adjust the model to get different output
        messages=[
            {"role": "system", "content": f"You're an expert in Shakespeare that likes to reference 90s pop culture in blog posts."},
            {"role": "user", "content": f"Rewrite the following Romeo and Juliet excerpt in modern English and change the characters to characters from The Office TV show: {prompt}"}
        ]
        )
        response = completion.choices[0].message.content

    #Print response in terminal
    print(f"\n{settings.ai_username}: {response.strip()}")
    
    # Record response in txt file
    record_blog_post(f"{settings.blog_post_storage}", prompt, response.strip())



        
















 









        



