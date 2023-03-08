    
import os
import openai
import settings


openai.api_key = settings.api_key




user_prompt = input()


response = openai.Image.create(
prompt=f"{user_prompt}",
n=1,
size="512x512"
) 
image_url = response['data'][0]['url']
print(f"Potential images for your post: {image_url}")