class APIHandler:
    def __init__(self, api_tracker, client):
        self.api_tracker = api_tracker
        self.client = client
        self.send_open_ai_chat_message = self.api_tracker.track_calls("send_open_ai_chat_message")(
            self.send_open_ai_chat_message
        )
    
    def send_open_ai_chat_message(self, message_content):
        return self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            store=True,
            messages=[
                {"role": "user", "content": message_content}
            ]
        )