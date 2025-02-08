import threading


class SingletonMeta(type):
    """Metaclass to enforce singleton behavior with thread safety."""
    _instances = {}
    _lock = threading.Lock()  # Ensure thread safety

    def __call__(cls, *args, **kwargs):
        with cls._lock:  # Lock to prevent race conditions
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


# class SingletonMeta:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls, *args, **kwargs)
#         return cls._instance
#
#     def __init__(self, value):
#         if not hasattr(self, 'initialized'):
#             self.value = value
#             self.initialized = True
#
#     def display_value(self):
#         print(f"The value is {self.value}")

# class SingletonMeta(type):
#     """Metaclass to enforce singleton behavior."""
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]