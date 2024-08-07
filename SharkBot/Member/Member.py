import json
import os
from typing import Self

import colorama

from SharkBot import Utils
from SharkBot.Member import Cooldowns, Permissions, MemberCreatures, MemberTickets, MemberShopData
from . import DataConverter

_MEMBERS_DIRECTORY = "data/live/members"

Utils.FileChecker.directory(_MEMBERS_DIRECTORY)


class Member:
    members: list[Self] = []
    members_dict: dict[int, Self] = {}

    def __init__(self, member_data: dict):
        data_changed, member_data = DataConverter.convert(member_data)
        self.id: int = member_data["id"]
        self.balance: int = member_data["balance"]
        self.gems: int = member_data["gems"]
        self.power_tokens: int = member_data["power_tokens"]
        self.shop_data: MemberShopData = MemberShopData(member_data["shop_data"])
        self.cooldowns: Cooldowns = Cooldowns(**member_data["cooldowns"])
        self.permissions: Permissions = Permissions(**member_data["permissions"])
        self.creatures: MemberCreatures = MemberCreatures(member_data["creatures"])
        self.tickets: MemberTickets = MemberTickets(member_data["tickets"])
        self.data_version: int = member_data["data_version"]

        if data_changed:
            self.write_data()

    @classmethod
    def create(cls, member_id: int) -> Self:
        member = cls({
            "id": member_id
        })
        cls.members.append(member)
        cls.members_dict[member_id] = member
        return member

    @classmethod
    def get(cls, member_id: int, create: bool = True) -> Self:
        if member_id in cls.members_dict:
            return cls.members_dict[member_id]
        elif create:
            return cls.create(member_id)
        else:
            raise Exception(f"Member {member_id} not found.")

    @property
    def data(self) -> dict:
        return {
            "id": self.id,
            "balance": self.balance,
            "gems": self.gems,
            "power_tokens": self.power_tokens,
            "shop_data": self.shop_data.data,
            "cooldowns": self.cooldowns.data,
            "permissions": self.permissions.data,
            "creatures": self.creatures.data,
            "tickets": self.tickets.data,
            "data_version": self.data_version
        }

    def write_data(self):
        with open(f"{_MEMBERS_DIRECTORY}/{self.id}.json", "w+") as outfile:
            json.dump(self.data, outfile, indent=4)

    @classmethod
    def load_members(cls):
        cls.members.clear()
        cls.members_dict.clear()
        for file in os.listdir(_MEMBERS_DIRECTORY):
            with open(f"{_MEMBERS_DIRECTORY}/{file}", "r") as infile:
                member_data = json.load(infile)
            member = cls(member_data)
            cls.members.append(member)
            cls.members_dict[member_data["id"]] = member


Member.load_members()
print(colorama.Fore.GREEN + f"Loaded data for {len(Member.members)} members.")
