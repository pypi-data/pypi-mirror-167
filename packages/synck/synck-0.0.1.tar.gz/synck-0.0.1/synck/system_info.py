import getpass
import platform
import sys
from functools import lru_cache


@lru_cache()
def get_user_name():
    return getpass.getuser()


@lru_cache()
def get_computer_name():
    return platform.node()


@lru_cache()
def is_windows():
    return sys.platform.lower().startswith("win")


@lru_cache()
def is_linux():
    return sys.platform.lower().startswith("linux")
