

import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env variables

openai.api_key = os.getenv("OPENAI_API_KEY")  # Now reads key from environment



def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change to "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant named Jarvis."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"OpenAI API Error: {e}"
