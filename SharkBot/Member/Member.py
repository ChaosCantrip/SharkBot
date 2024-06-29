from typing import Self
from SharkBot import Utils
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
        self.data_version: int = member_data["data_version"]

        if data_changed:
            pass
            # self.write_data()

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
