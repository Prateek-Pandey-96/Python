from abc import ABC, abstractmethod


class Subscriber(ABC):
    
    @abstractmethod
    def processEvent(self, event):
        pass