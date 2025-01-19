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
    print("Calling OpenAI API")
    handler.send_open_ai_chat_message("write a haiku about ai").choices[0].message
    print("Calling OpenAI API")
    handler.send_open_ai_chat_message("write a haiku about ai").choices[0].message
    print("Calling OpenAI API")
    handler.send_open_ai_chat_message("write a haiku about ai").choices[0].message
    print("Calling OpenAI API")
    handler.send_open_ai_chat_message("write a haiku about ai").choices[0].message
    print("Calling OpenAI API")
    handler.send_open_ai_chat_message("write a haiku about ai").choices[0].message
    
    print("\nReporting sustainability data from API Consumption Manager:")
    co2, kW, water = api_tracker.get_calculations()
    print(f"{round(co2, 2)}g CO2e, {round(kW, 3)}kWh, {round(water, 1)}ml water")