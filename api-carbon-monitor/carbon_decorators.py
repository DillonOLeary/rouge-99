"""
This files contains decorator functions for API calls
"""
import functools
from collections import defaultdict

KNOWN_SUSTAINABILITY_NUMBERS = {
    "send_open_ai_chat_message": {
        "carbon": 4.3,
        "electricity": .001,
        "water": 25
    }
}

class APIConsumptionManagement:
    def __init__(self):
        self.call_counts = defaultdict(lambda: 0)
    
    def track_calls(self, function_name):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                self.call_counts[function_name] += 1
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def get_calculations(self):
        total_carbon = 0.0
        total_electricity = 0.0
        total_water = 0.0
        
        for function_name, num_calls in self.call_counts.items():
            if function_name in KNOWN_SUSTAINABILITY_NUMBERS:
                total_carbon += num_calls*KNOWN_SUSTAINABILITY_NUMBERS[function_name]["carbon"]
                total_electricity += num_calls*KNOWN_SUSTAINABILITY_NUMBERS[function_name]["electricity"]
                total_water += num_calls*KNOWN_SUSTAINABILITY_NUMBERS[function_name]["water"]
                
        return total_carbon, total_electricity, total_water