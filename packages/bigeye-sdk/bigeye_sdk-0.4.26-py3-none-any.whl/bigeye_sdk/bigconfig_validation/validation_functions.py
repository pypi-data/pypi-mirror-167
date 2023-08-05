from typing import Any

import yaml


def safe_split_dict_entry_lines(key: str, value: Any):
    return yaml.safe_dump({key: value}, indent=True).strip().split('\n')
