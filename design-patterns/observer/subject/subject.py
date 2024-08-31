from abc import ABC, abstractmethod
class Subject(ABC):
    
    @abstractmethod
    def addSubscriber(self, subscriber):
        pass
    
    @abstractmethod
    def removeSubscriber(self, subscriber):
        pass
    
    @abstractmethod
    def notifyAll(self, event):
        pass