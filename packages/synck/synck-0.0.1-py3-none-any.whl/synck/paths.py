from pathlib import Path

from synck import application_name


def get_default_parent_directory() -> Path:
    return Path(Path.home(), application_name)
