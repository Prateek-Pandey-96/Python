from manager import Manager
from ticket import Ticket
from processingStrategy import *

if __name__ == '__main__':
    
    manager = Manager()
    manager.addTicket(Ticket(1, "first", "monitor not working!"))
    manager.addTicket(Ticket(2, "second", "keyboard not working!"))
    manager.addTicket(Ticket(3, "third", "mouse not working!"))

    manager.processTickets(LifoProcessingStrategy())