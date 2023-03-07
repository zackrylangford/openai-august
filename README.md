# August-GPT

This is a simple application that allows the user to prompt the gpt-3.5-turbo model from openai in a chat format. Currently, the application runs in the terminal and records the conversation in at .txt format for later review.

August can walk you through the creation of a blog post with prompts and help edit and format a blog post with the command --coach. 

There is also a script to have August write a full blog post about a topic that is entered by the user. Simply input --blog and August will walk the user through a blog post creation program and output the blog post into a .txt file in a specified directory in the settings. 

- 👆 make sure to update the settings to reflect your username as well as create a new username for your AI. You can also specify the directory that you would like to save chat and blog post output. 

- 👋 August is programmed with a couple of commands to use take advantage of the gpt model. See the list of commands here [COMMANDS](COMMANDS.md)

- 🤖 I named the AI "August" so it felt a little more personal. 



# Installation

1. Clone this repository locally
```
git clone https://github.com/zackrylangford/openai-chatgpt.git
```

2. Create openai API account and generate API key from [OpenAI] (https://openai.com/api/) 

Insert your API key into the settings.py file. For security best practices, use environment variables in order to protect your API key. For more information on how to set up environment variables with openai, see: [Best Practices for API Keys](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)

settings.py
```
api_key = os.environ["OPENAI_API_KEY"]
```

3. Install openai package in your envrionment. You may need to set up a virtual environment in order to isoloate your packages to avoid any conflicts. 

```
pip install openai
```

4. Make any changes to the AI to play around with length of output, number of responses, etc. in the settings.py file. 


5. Run the script in your terminal and have fun!
```
python3 august.py
```

# More Information 

For troubleshooting and help with getting set up or to figure out how to make more changes, see [openai.com](https://openai.com) and go through the documentation under the API section. 

# Contact

Questions or comments? 

[Email Zack Langford](mailto::zack@cloudzack.com)
