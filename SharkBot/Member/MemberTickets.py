from SharkBot import Ticket
from SharkBot.Errors import NotEnoughTicketsError


class MemberTickets:

    def __init__(self, data: list[str]):
        self.tickets: list[Ticket] = [Ticket.get(ticket_id) for ticket_id in data]

    @property
    def data(self) -> list[str]:
        return [ticket.id for ticket in self.tickets]

    def add_tickets(self, ticket: Ticket, amount: int):
        for i in range(amount):
            self.tickets.append(ticket)

    def remove_tickets(self, ticket: Ticket, amount: int):
        if self.tickets.count(ticket) < amount:
            raise NotEnoughTicketsError(ticket)
        for i in range(amount):
            self.tickets.remove(ticket)