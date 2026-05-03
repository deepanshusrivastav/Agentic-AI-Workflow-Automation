import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_task_plan(user_input):
    prompt = f"""
    You are an AI agent planner.

    Break the following task into clear actionable steps:
    Task: {user_input}

    Return steps in a numbered list.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
