from api_handler import APIHandler

if __name__ == "__main__":
    print(APIHandler.send_open_ai_chat_message("write a haiku about ai").choices[0].message)
    print(APIHandler.send_open_ai_chat_message("write a haiku about ai").choices[0].message)
    print(APIHandler.send_open_ai_chat_message("write a haiku about ai").choices[0].message)