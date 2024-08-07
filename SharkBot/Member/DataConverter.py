from .DataVersions import *


class DataConverter:

    @staticmethod
    def _get_latest_version() -> type[VERSION]:
        return versions[-1]

    @classmethod
    def convert(cls, member_data: dict) -> tuple[bool, dict]:
        if "data_version" not in member_data:
            member_data["data_version"] = 1
        if member_data["data_version"] == cls._get_latest_version().get_version_number():
            return False, member_data
        else:
            return True, cls._get_latest_version().convert(member_data)
