import os

from api_handler import APIHandler
from carbon_decorators import APIConsumptionManagement
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

if __name__ == "__main__":

    api_tracker = APIConsumptionManagement()
    client = OpenAI(
        api_key=os.getenv("OPEN_AI_API_KEY")
    )
    handler = APIHandler(api_tracker, client)
    handler.send_open_ai_chat_message("write a haiku about ai").choices[0].message
    handler.send_open_ai_chat_message("write a haiku about ai").choices[0].message
    print(handler.send_open_ai_chat_message("write a haiku about ai").choices[0].message)