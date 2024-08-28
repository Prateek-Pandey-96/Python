from ticket import Ticket
from processingStrategy import ProcessingStrategy

class Manager:
    def __init__(self):
        self.tickets = []

    def addTicket(self, ticket: Ticket) -> None:
        self.tickets.append(ticket)
    
    def processTicket(self, ticket: Ticket) -> None:
        print(f"processing ticket: {ticket.id}")
        print("------------")
    
    def processTickets(self, strategy: ProcessingStrategy) -> None:
        tickets = strategy.processTickets(self.tickets)
        if len(tickets) == 0:
            return
        
        for ticket in tickets:
            self.processTicket(ticket)