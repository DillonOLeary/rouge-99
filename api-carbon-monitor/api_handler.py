import os

from carbon_decorators import APIConsumptionManagement
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPEN_AI_API_KEY")
)
api_tracker = APIConsumptionManagement()

class APIHandler:
    @api_tracker.track_calls("send_open_ai_chat_message")
    def send_open_ai_chat_message(message_content):
        return client.chat.completions.create(
            model="gpt-3.5-turbo",
            store=True,
            messages=[
                {"role": "user", "content": message_content}
            ]
        )