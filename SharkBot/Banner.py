from typing import Self
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


class Pull:

    def __init__(self, lootpool_id: str, number: int):
        self._lootpool_id = lootpool_id
        self._number = number

    # ===== Properties =====

    @property
    def lootpool_id(self):
        return self._lootpool_id

    @property
    def number(self):
        return self._number


class BuyOption:

    def __init__(self, name: str, cost: TicketCost, pulls: list[Pull]):
        self._name = name
        self._cost = cost
        self._pulls = pulls

    # ===== Properties =====

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @property
    def pulls(self):
        return self._pulls


class Banner:
    banners: list[Self] = []
    banners_map: dict[str, Self] = {}

    def __init__(self, id: str, name: str, description: str, active: bool, buy_options: list[BuyOption]):
        self._id = id
        self._name = name
        self._description = description
        self._active = active
        self._buy_options = buy_options

        self.banners.append(self)
        self.banners_map[self.id] = self

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
    def active(self):
        return self._active

    @property
    def buy_options(self):
        return self._buy_options

    # ===== Class Methods =====

    @classmethod
    def get_banner(cls, id: str):
        return cls.banners_map.get(id)

    @classmethod
    def get_active_banners(cls):
        return [banner for banner in cls.banners if banner.active]


Banner(
    id="hourly_pull",
    name="Hourly Pull Banner",
    description="Collect a small amount of creature power from pulls",
    active=True,
    buy_options=[
        BuyOption(
            name="3x",
            cost=TicketCost("hourly_pull", 3),
            pulls=[
                Pull("hourly_pull", 3)
            ]
        )
    ]
)
Banner(
    id="daily_pull",
    name="Daily Pull Banner",
    description="Collect a moderate amount of creature power from pulls",
    active=True,
    buy_options=[
        BuyOption(
            name="3x",
            cost=TicketCost("daily_pull", 3),
            pulls=[
                Pull("daily_pull", 3)
            ]
        )
    ]
)
Banner(
    id="weekly_pull",
    name="Weekly Pull Banner",
    description="Collect a creature power from pulls",
    active=True,
    buy_options=[
        BuyOption(
            name="3x",
            cost=TicketCost("weekly_pull", 3),
            pulls=[
                Pull("weekly_pull", 3)
            ]
        )
    ]
)
