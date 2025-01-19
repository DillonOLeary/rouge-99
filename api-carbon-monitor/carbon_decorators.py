"""
This files contains decorator functions for API calls
"""
import functools
from collections import defaultdict


class APIConsumptionManagement:
    def __init__(self):
        self.call_counts = defaultdict(lambda: 0)
    
    def track_calls(self, function_name):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                self.call_counts[function_name] += 1
                print(self.call_counts)
                return func(*args, **kwargs)
            return wrapper
        return decorator