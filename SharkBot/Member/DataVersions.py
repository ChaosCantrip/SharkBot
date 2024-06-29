from typing import Self


class VERSION:

    @classmethod
    def get_version_number(cls) -> int:
        return int(cls.__name__[7:])

    @classmethod
    def _get_last_version(cls) -> Self:
        return versions[cls.get_version_number() - 2]

    @classmethod
    def convert(cls, member_data: dict) -> dict:
        if member_data["data_version"] != cls.get_version_number() - 1:
            member_data = cls._get_last_version().convert(member_data)
        member_data["data_version"] = cls.get_version_number()
        return cls._convert(member_data)

    @staticmethod
    def _convert(member_data: dict) -> dict:
        return member_data


class Version1(VERSION):

    @staticmethod
    def _convert(member_data: dict) -> dict:
        return member_data


class Version2(VERSION):

    @staticmethod
    def _convert(member_data: dict) -> dict:
        member_data["balance"] = 0
        return member_data


versions: list[type[VERSION]] = [
    Version1,
    Version2
]
