# August-GPT: Chat with the AI

🤖 August-GPT is an easy-to-use chat application that utilizes OpenAI's GPT-3.5-Turbo model. The chat platform allows you to communicate with the AI through prompts and get responses on a wide range of topics.

🔥 Here are some features of August-GPT that you can take advantage of:

✨ **Update Settings**: Before starting, ensure to update the settings file to reflect your username and set up a new username for your AI. You can also specify the directory where you want to store chat and blog post output.

📑 **Create a Blog Post**: Do you need help creating a blog post? August-GPT can assist you by guiding you through a step-by-step process with prompts. Furthermore, you can edit and format your post to your liking.

📝 **Resume and Cover Letter**: August-GPT can assist you in writing your resume and cover letter by rewriting them based on job descriptions. Refer to the instructions in the `COMMANDS.md` file to learn how to do it.

🛠️ **Installation**: Here's how to get started with August-GPT:

1. Clone this repository locally:
   ```
   git clone https://github.com/zackrylangford/openai-chatgpt.git
   ```

2. Create an account with OpenAI API and obtain an API key from their website. Provide your API key in the `settings.py` file. We recommend that you use environment variables to protect your API keys.

    ```
    settings.py
    api_key = os.environ["OPENAI_API_KEY"]
    ```

3. Install the OpenAI package in your environment. You can isolate your Python packages in a virtual environment to avoid conflicts.

    ```
    pip install openai
    ```

4. Update your username and background information in the `settings.py` file.

5. Navigate to your terminal and run the script to start chatting with the AI! `python3 august.py`

💡 **Tips**: 

- To address any issues or get help setting up the application, visit the [OpenAI website](https://openai.com) under the API section.
- Protect your API keys by using environment variables, which keeps security high.
- Keep your chat output and blog post output organized by specifying which directory August-GPT should store files in.

💬 **Contact**: Should you have any inquiries or feedback, please do not hesitate to [email Zack Langford](mailto::zack@cloudzack.com).