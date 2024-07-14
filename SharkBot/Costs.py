from SharkBot import Ticket


class TicketCost:

    def __init__(self, ticket_id: str, amount: int):
        self._ticket = Ticket.get(ticket_id)
        self._amount = amount

    # ===== Properties =====

    @property
    def ticket(self):
        return self._ticket

    @property
    def amount(self):
        return self._amount

    def __str__(self):
        return f"{self.amount}x :ticket: {self.ticket.name}"


class GemCost:

    def __init__(self, amount: int):
        self._amount = amount

    # ===== Properties =====

    @property
    def amount(self):
        return self._amount

    def __str__(self):
        return f":gem: {self.amount}"


class MoneyCost:

    def __init__(self, amount: int):
        self._amount = amount

    # ===== Properties =====

    @property
    def amount(self):
        return self._amount

    def __str__(self):
        return f":dollar: {self.amount}"


COSTS = GemCost | TicketCost | MoneyCost
