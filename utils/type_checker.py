from typing import TypeAlias

Locator:TypeAlias = tuple[str, str]

ADD_USER:list[str] = ["role", "name", "status", "username", "password", "confirm_password"]

EDIT_USER:list[str] = ["role", "name", "status", "username"]