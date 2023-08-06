from typing import Dict, Any


class AudienceNameGetter:
    def __init__(self) -> None:
        self.__user_friendly_part_length = 8

    def get_user_friendly_export_id(self, config: Dict[str, Any]) -> str:
        user_friendly_part = config["export_id"][: self.__user_friendly_part_length].upper()
        return f"E-{user_friendly_part}"

    def get(self, config: Dict[str, Any]) -> str:
        return f"{self.get_user_friendly_export_id(config)} {config['export_title']}"
