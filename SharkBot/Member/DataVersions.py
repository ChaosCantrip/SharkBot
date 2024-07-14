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


class Version3(VERSION):

    @staticmethod
    def _convert(member_data: dict) -> dict:
        member_data["cooldowns"] = {
            "hourly": "01/01/2000-00:00:00",
            "daily": "01/01/2000-00:00:00",
            "weekly": "01/01/2000-00:00:00"
        }
        return member_data


class Version4(VERSION):

    @staticmethod
    def _convert(member_data: dict) -> dict:
        member_data["permissions"] = {
            "admin": False
        }
        return member_data


class Version5(VERSION):

    @staticmethod
    def _convert(member_data: dict) -> dict:
        member_data["creatures"] = []
        return member_data


class Version6(VERSION):

    @staticmethod
    def _convert(member_data: dict) -> dict:
        member_data["tickets"] = []
        return member_data


class Version7(VERSION):

    @staticmethod
    def _convert(member_data: dict) -> dict:
        member_data["gems"] = 0
        return member_data


class Version8(VERSION):

    @staticmethod
    def _convert(member_data: dict) -> dict:
        member_data["power_tokens"] = 0
        return member_data


versions: list[type[VERSION]] = [
    Version1,
    Version2,
    Version3,
    Version4,
    Version5,
    Version6,
    Version7,
    Version8
]
