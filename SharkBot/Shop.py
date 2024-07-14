from typing import Optional

from SharkBot import Ticket, Costs


class GemsItem:

    def __init__(self, amount: int):
        self._amount = amount

    # ===== Properties =====

    @property
    def amount(self):
        return self._amount

    def __str__(self):
        return f":gem: {self.amount}"


class TicketItem:

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


class ShopItem:

    def __init__(self, id: str, item: TicketItem | GemsItem, cost: Costs.COSTS, limit: Optional[int]):
        self._id = id
        self._item = item
        self._cost = cost
        self._limit = limit

    # ===== Properties =====

    @property
    def id(self):
        return self._id

    @property
    def item(self):
        return self._item

    @property
    def cost(self):
        return self._cost

    @property
    def limit(self):
        return self._limit


class ShopCategory:

    def __init__(self, id: str, name: str, description: str, items: list[ShopItem]):
        self._id = id
        self._name = name
        self._description = description
        self._items = items

    # ===== Properties =====

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def items(self):
        return self._items


SHOP = [
    ShopCategory(
        id="gems_shop",
        name="Gems Shop",
        description="Buy gems with money.",
        items=[
            ShopItem(
                id="gems_1",
                item=GemsItem(10),
                cost=Costs.MoneyCost(100),
                limit=10
            ),
            ShopItem(
                id="gems_2",
                item=GemsItem(10),
                cost=Costs.MoneyCost(250),
                limit=20
            ),
            ShopItem(
                id="gems_3",
                item=GemsItem(10),
                cost=Costs.MoneyCost(500),
                limit=20
            )
        ]
    )
]
