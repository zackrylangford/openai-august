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

        


def blog_coach():
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
        tweet_prompt = input(f"\n\n{settings.ai_username}: Would you like me to come up with some Tweets based on the blog post we just wrote? (y/n)")
        if tweet_prompt == "y":
            blog_path = f_path / "documents/blogpost.txt"
            with open(blog_path, 'r') as file:
                blog_saved = file.read()
            
            completion = openai.ChatCompletion.create(
            model=settings.model_engine,
            messages=[
                {"role": "system", "content": f"{settings.blog_coach}"},
                {"role": "assistant", "content": f"Blog post that we just wrote:{blog_saved}.{settings.username}'s background: {settings.background}"},
                {"role": "user", "content": f"Write 3-5 unique insights, funny sayings, or twitteresque type content with hashtags and emojies from the blog post we just wrote based on {settings.username}'s background for {settings.username}'s Twitter account: {blog_saved}"},
            ]
            )
            response = completion.choices[0].message.content
            add_tweets(f"{settings.social_storage}", response.strip())
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
                        {"role": "assistant", "content": f"{settings.username}'s background: {settings.background}"},
                        {"role": "user", "content": f"Write one unique long form LinkedIn post from the following blog post using {settings.username}'s background for {settings.username}'s Twitter account: {blog_saved}"},
                    ]
                    )
                    response = completion.choices[0].message.content
                add_linked(f"{settings.social_storage}", response.strip())
                print(f"\n{settings.ai_username}: Linked in Post Idea:\n{response.strip()}\n****\n\nLinkedIn post was saved to your blog post file")
            elif tweet_prompt == "n":
                print("OK, got it, no LinkedIn post")

        
    # Generate an image for the blog using keywords and add link to bottom of blog post page
            image_add = input(f"{settings.ai_username}: \n\nWould you like me to generate an image with keywords from the blog post we just wrote? (y/n)")
            if image_add == "y":
                blog_path = f_path / "documents/blogpost.txt"
                with open(blog_path, 'r') as file:
                    blog_saved = file.read()
            
                    completion = openai.ChatCompletion.create(
                    model=settings.model_engine,
                    messages=[
                        {"role": "system", "content": f"{settings.blog_coach}"},
                        {"role": "assistant", "content": f"Blog post that we just wrote:{blog_saved}.{settings.username}'s background: {settings.background}"},
                        {"role": "user", "content": f"Generate a string of four keywords seperated by commas on one line that are good images for the following blog post: {blog_saved}"},
                    ]
                    )
                    key_words = completion.choices[0].message.content
            
                    add_keywords(f"{settings.blog_post_storage}", key_words.strip())
    
                    style_type = ['abstract', 'photo','surreal','impressionist','cubism', 'art deco']
                    response = openai.Image.create(
                    prompt=(f"{random.choice(style_type)}, {key_words}"),
                    n=1,
                    size="512x512"
                    ) 
                    image_url = response['data'][0]['url']
                    print(f"Potential image for your blog post: {image_url}")
                    add_url(f"{settings.blog_post_storage}", image_url.strip())
                    print(f"\n\n*****\n\n\nImage saved to your blog post document")
                    print(f"\nYour blog post is complete! Great work!")




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



def resume_coach():
    """Rewrite the users resume geared towards a specific job posting and write a cover letter draft"""  
    # Location of job posting and resume
    job_path = f_path / "resources/job-posting/job-posting.txt"
    resume_path = f_path / "resources/resume/resume.txt"
    with open(job_path, 'r') as file1, open(resume_path, 'r') as file2:
        job_posting = file1.read()
        resume = file2.read()
        # Print the job posting to the terminal for reference
        print(job_posting)

        completion = openai.ChatCompletion.create(
        model=settings.model_engine,
        
        # August now processes the job posting and resume
        messages=[
        {"role": "system", "content": f"You're a resume and cover letter assistant, helping {settings.username} with a job application."},
        {"role": "assistant", "content": f"Job posting: {job_posting}{settings.username}'s resume: {resume}"},
        {"role": "user", "content": f"Rewrite {settings.username}'s resume to optimize for the job posting"}
        ]
        )
        response = completion.choices[0].message.content

    #Verify the document is being rewritten
    print(f"\n{settings.ai_username}: Resume is being rewritten!")
    
    # Record response in txt file
    resume_saved(f"{settings.resume_storage}", response.strip())



def cover_letter():
    """Rewrite the users cover letter geared towards a specific job posting"""  
    # Location of job posting and resume
    job_path = f_path / "resources/job-posting/job-posting.txt"
    cover_path = f_path / "resources/resume/cover-letter.txt"
    resume_path = f_path / "resources/resume/resume.txt"
    with open(job_path, 'r') as file1, open(resume_path, 'r') as file2, open(cover_path, 'r') as file3:
        job_posting = file1.read()
        resume_path = file2.read()
        cover_let = file3.read()

        # Print the job posting to the terminal for reference
        print(job_posting)

        completion = openai.ChatCompletion.create(
        model=settings.model_engine,
        
        # August now processes the job posting and resume
        messages=[
        {"role": "system", "content": f"You're a resume and cover letter assistant, helping {settings.username} with a job application."},
        {"role": "assistant", "content": f"Job posting: {job_posting}. {settings.username}'s resume: {settings.username}'s cover letter: {cover_let}"},
        {"role": "user", "content": f"Based on {settings.username}'s resume and cover letter, rewrite {settings.username}'s cover letter to optimize for the job posting"}
        ]
        )
        response = completion.choices[0].message.content

    #Verify the document is being rewritten
    print(f"\n{settings.ai_username}: Cover letter is being rewritten!")
    
    # Record response in txt file
    resume_saved(f"{settings.cover_letter_storage}", response.strip())     








def md_writing():
    """Edit and rewrite markdown file for clarity"""  
    # Location of job posting and resume
    tech_doc = f_path / "resources/markdown/tech-doc.md"
    with open(tech_doc, 'r') as file:
        markdown_file = file.read()

        completion = openai.ChatCompletion.create(
        model=settings.model_engine,
        
        # August now processes the job posting and resume
        messages=[
        {"role": "system", "content": f"You're a technical writing assistant, helping {settings.username} with markdown files for GitHub repositories."},
        {"role": "assistant", "content": f"Markdown File: {markdown_file}"},
        {"role": "user", "content": f"Rewrite the markdown file for a Github repository for clarity and expand to help the reader understand it better. Use emojies, lists, and anything to help make it better."}
        ]
        )
        response = completion.choices[0].message.content

    #Verify the document is being rewritten
    print(f"\n{settings.ai_username}: Cover letter is being rewritten!")
    
    # Record response in txt file
    md_saved(f"{settings.tech_doc_storage}", response.strip())   


def contrib_doc():
    """Read a Github README.md file and create a contribution.md file """  
    # Location of job posting and resume
    readme_doc = f_path / "resources/markdown/readme-doc.md"
    with open(readme_doc, 'r') as file:
        readme_file = file.read()

        completion = openai.ChatCompletion.create(
        model=settings.model_engine,
        
        # August now processes the job posting and resume
        messages=[
        {"role": "system", "content": f"You're a technical writing assistant, helping {settings.username} with technical writing for GitHub repositories."},
        {"role": "assistant", "content": f"Read Me File: {readme_file}"},
        {"role": "user", "content": f"Take the read me file and write a brand new markdown file that give guidelines for contributing to this open source project described in the Read me file. Title the document contributions.md. This contributions.md file will be in a Github repository, so tailor the document to GitHub audience."}
        ]
        )
        response = completion.choices[0].message.content

    #Verify the document is being rewritten
    print(f"\n{settings.ai_username}: Contrib doc has been written!")
    
    # Record response in txt file
    md_saved(f"{settings.contrib_doc_storage}", response.strip())   


def conduct_doc():
    """Read a Github README.md file and Contributions file and create a code of conduct file """  
    # Location of read me file and contributions file
    read_me_path = f_path / "resources/markdown/readme-doc.md"
    contrib_path = f_path / "resources/markdown/contrib-doc.md"
    with open(read_me_path, 'r') as file1, open(contrib_path, 'r') as file2:
        readme_file = file1.read()
        contrib_file = file2.read()

        completion = openai.ChatCompletion.create(
        model=settings.model_engine,
        
        # August now processes the job posting and resume
        messages=[
        {"role": "system", "content": f"You're a technical writing assistant, helping {settings.username} with technical writing for a GitHub repository."},
        {"role": "assistant", "content": f"Read Me File: {readme_file} and Contributions File: {contrib_file}"},
        {"role": "user", "content": f"Take the read me file and contributions files and write a brand new markdown file that gives code of conduct guidelines to this open source project. Title the document codeofconduct.md. This file will be in a Github repository, so tailor the document to GitHub audience."}
        ]
        )
        response = completion.choices[0].message.content

    #Verify the document is being rewritten
    print(f"\n{settings.ai_username}: Code of conduct doc has been written!")
    
    # Record response in txt file
    md_saved(f"{settings.conduct_doc_storage}", response.strip())   


            
def code_blog():
    """Take a chunk of code and write a technical blog post explaining what it does""" 
    # Location of code 
    code_doc = f_path / "resources/code/code-doc.txt"
    with open(code_doc, 'r') as file:
        code_file = file.read()

        completion = openai.ChatCompletion.create(
        model=settings.model_engine,
        
        # August now processes the job posting and resume
        messages=[
        {"role": "system", "content": f"You're a technical writing assistant, helping {settings.username} with technical writing about code for a blog."},
        {"role": "assistant", "content": f"Read Me File: {code_file}"},
        {"role": "user", "content": f"Take the given code and write a blog post explaining what the code does and break it down into steps to recreate it. Break the blog post up into sections with detailed instructions for the reader in how to recreate the code for other projects. Fix any code that doesn't work or make sense. Insert some funny quips in the explanations."},
        ]
        )
        response = completion.choices[0].message.content

    #Verify the document is being rewritten
    print(f"\n{settings.ai_username}: Code blog has been written!")
    
    # Record response in txt file
    code_blog_saved(f"{settings.code_blog_storage}", response.strip())  







 









        





            
















 









        



