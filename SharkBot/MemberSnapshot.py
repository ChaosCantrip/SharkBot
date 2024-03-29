import json
import os
from typing import Optional, Union

import SharkBot

_SNAPSHOTS_DIRECTORY = "data/live/snapshots/members"

class MemberSnapshot:

    def __init__(self, member):
        self.member: SharkBot.Member.Member = member
        self.path: str = f"{_SNAPSHOTS_DIRECTORY}/{member.id}.json"

    def get_current(self) -> Optional[dict[str, str | int | dict]]:
        if self.member.raw_display_name is None:
            return None
        return {
            "id": str(self.member.id),
            "display_name": self.member.display_name,
            "avatar_url": self.member.avatar_url,
            "balance": self.member.balance,
            "bank_balance": self.member.bank_balance,
            "counts": self.member.counts,
            "xp": self.member.xp.xp,
            "level": self.member.xp.level,
            "stats": self.member.stats.data,
            "cooldowns": self.member.cooldowns.db_data,
            "effects": self.member.effects.db_data,
            "missions": self.member.missions.db_data,
            "collection": self.member.collection.db_data
        }

    def get_last(self) -> Optional[dict]:
        if not os.path.exists(self.path):
            return None
        else:
            with open(self.path, "r") as infile:
                return json.load(infile)

    @property
    def has_changed(self) -> bool:
        old_snapshot = self.get_last()
        if old_snapshot is None:
            return True
        else:
            return old_snapshot != self.get_current()

    def write(self, snapshot: Optional[dict]):
        if snapshot is None:
            snapshot = self.get_current()
        with open(self.path, "w+") as outfile:
            json.dump(snapshot, outfile, indent=2)

SharkBot.Utils.FileChecker.directory(_SNAPSHOTS_DIRECTORY)