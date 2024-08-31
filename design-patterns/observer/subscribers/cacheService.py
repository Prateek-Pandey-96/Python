from .subscriber import Subscriber

class CacheService(Subscriber):
    
    def processEvent(self, event):
        print(f"updating the cache: {event.name}")