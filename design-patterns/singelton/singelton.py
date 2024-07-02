from typing import Any

class SingeltonMeta(type):
    __instances = {}
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]
    
class Logger(metaclass=SingeltonMeta):
    def __init__(self) -> None:
        self.status = "Not connected"

    def disconnect(self):
        self.status = "Disconnected"
    
    def connect(self):
        self.status = "Connected"

logger1 = Logger()
logger1.connect()

logger2 = Logger()
logger2.disconnect()

print(logger1.status)
