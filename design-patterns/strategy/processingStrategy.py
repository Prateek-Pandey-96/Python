from abc import ABC, abstractmethod
from typing import List
from ticket import Ticket
import random

class ProcessingStrategy(ABC):
    @abstractmethod
    def processTickets(self, tickets: List[Ticket])->List[Ticket]:
        pass

class FifoProcessingStrategy(ProcessingStrategy):
    def processTickets(self, tickets: List[Ticket]) -> List[Ticket]:
        tickets_copy = tickets.copy()
        return tickets_copy
    
class LifoProcessingStrategy(ProcessingStrategy):
    def processTickets(self, tickets: List[Ticket]) -> List[Ticket]:
        tickets_copy = tickets.copy()
        return tickets_copy[::-1]

class RandomProcessingStrategy(ProcessingStrategy):
    def processTickets(self, tickets: List[Ticket]) -> List[Ticket]:
        tickets_copy = tickets.copy()
        random.shuffle(tickets_copy)
        return tickets_copy