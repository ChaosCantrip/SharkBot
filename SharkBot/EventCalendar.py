import json
import os.path
from typing import Self, Optional
from datetime import datetime, timedelta, date
from SharkBot import Item, Utils, Member

_DATE_FORMAT = "%d/%m/%Y"
_SOURCE_FILE = "data/static/collectibles/event_calendars.json"
_TRACKING_FOLDER = "data/live/event_calendars"
Utils.FileChecker.directory(_TRACKING_FOLDER)

class EventCalendar:
    event_calendars: list[Self] = []
    _current_calendar: Optional[Self] = None
    _last_checked_date: date = datetime.now().date() - timedelta(days=1)

    def __init__(self, name: str, start_date: str, rewards: list[str]):
        self.name = name
        self._tracking_file = f"{_TRACKING_FOLDER}/{self.name}.json"
        self.start_date = datetime.strptime(start_date, _DATE_FORMAT).date()
        self.end_date = self.start_date + timedelta(days=len(rewards))
        self.rewards: list[list[Item.Item]] = [[Item.get(item_id) for item_id in items] for items in rewards]
        self.member_tracker: dict[int, int] = {}

        if os.path.isfile(self._tracking_file):
            with open(self._tracking_file, "r") as infile:
                _member_tracker_data = json.load(infile)
                self.member_tracker = {int(key): value for key, value in _member_tracker_data.items()}

    def __repr__(self):
        output = {
            "Object": "EventCalendar",
            "name": self.name,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "items": [[item.id for item in items] for items in self.rewards]
        }
        return json.dumps(output, indent=2)

    def __str__(self):
        output = {
            "Object": "EventCalendar",
            "name": self.name,
            "duration": f"{str(self.start_date)} to {str(self.end_date - timedelta(days=1))}",
            "end_date": str(self.end_date),
            "items": {str(self.start_date + timedelta(days=i)): [f"{items.count(item)}x {item.name} ({item.id})" for item in set(items)] for i, items in enumerate(self.rewards)}
        }
        return json.dumps(output, indent=2)

    @classmethod
    def get_current(cls) -> Optional[Self]:
        current_date = datetime.now().date()
        if current_date == cls._last_checked_date:
            return cls._current_calendar

        for event_calendar in cls.event_calendars:
            if event_calendar.start_date <= current_date < event_calendar.end_date:
                cls._current_calendar = event_calendar
                break
        else:
            cls._current_calendar = None

        cls._last_checked_date = current_date
        return cls._current_calendar

    def get_current_index(self) -> int:
        current_date = datetime.now().date()
        return (current_date - self.start_date).days

    def get_rewards(self, index: Optional[int] = None) -> list[Item.Item]:
        if index is None:
            index = self.get_current_index()
        return self.rewards[index]

    def write_member_tracker(self) -> None:
        with open(self._tracking_file, "w+") as _outfile:
            json.dump(self.member_tracker, _outfile, indent=2)

    def member_can_claim(self, member: Member.Member, index: Optional[int] = None) -> bool:
        if index is None:
            index = self.get_current_index()

        if member.id in self.member_tracker:
            return self.member_tracker[member.id] < index
        else:
            return True

    def mark_member_claimed(self, member: Member.Member, index: Optional[int] = None) -> None:
        if index is None:
            index = self.get_current_index()

        self.member_tracker[member.id] = index
        self.write_member_tracker()

def load_calendars() -> None:
    EventCalendar.event_calendars = []
    with open(_SOURCE_FILE, "r") as infile:
        _source_data: list[dict[str, str | list[str]]] = json.load(infile)
    for calendar_data in _source_data:
        EventCalendar.event_calendars.append(
            EventCalendar(**calendar_data)
        )

load_calendars()
