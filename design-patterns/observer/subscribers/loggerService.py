from .subscriber import Subscriber

class LoggerService(Subscriber):
    
    def processEvent(self, event):
        print(f"logging the save actione: {event.name}")