from datetime import datetime, timedelta

DATE_FORMAT = "%d/%m/%Y"


class MemberShopData:

    def __init__(self, data: dict):
        self._items = data["items"]
        self._reset_date = datetime.strptime(data["reset_date"], DATE_FORMAT)

    @property
    def needs_reset(self):
        return self._reset_date < datetime.utcnow()

    def reset(self):
        self._items.clear()
        while self._reset_date < datetime.utcnow():
            self._reset_date += timedelta(days=7)

    def get_times_bought(self, item_id: str) -> int:
        return self._items.get(item_id, 0)

    def add_times_bought(self, item_id: str, amount: int):
        self._items[item_id] = self.get_times_bought(item_id) + amount

    @property
    def data(self) -> dict:
        return {
            "items": self._items,
            "reset_date": datetime.strftime(self._reset_date, DATE_FORMAT)
        }