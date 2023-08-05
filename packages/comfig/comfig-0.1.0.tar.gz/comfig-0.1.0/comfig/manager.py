from typing import List
from pathlib import Path

USER_HOME = Path.home()


def get(field_name: str) -> str:
    ...


def set(field_name: str, field_value: str) -> str:
    ...


def delete(field_name: str) -> str:
    ...


def list() -> List[str]:
    ...
