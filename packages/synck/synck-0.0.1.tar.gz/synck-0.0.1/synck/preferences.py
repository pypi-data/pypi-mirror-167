import uuid

from attr import attrib, attrs
from pref import Pref

from synck import application_name, author
from synck.paths import get_default_parent_directory


@attrs
class SynckPreferences(Pref):
    """
    Synck preferences
    DO NOT INSTANTIATE DIRECTLY - USE get_pref()!
    """

    parent_directory: str = attrib(default=str(get_default_parent_directory()))  # pathlib.Path compatible
    node_id: str = attrib(default=str(uuid.uuid4()))  # self-initializes

    # set either:
    #   aws_profile
    # or
    #   aws_access_key_id and aws_secret_access_key
    aws_profile: str = attrib(default=None)
    aws_access_key_id: str = attrib(default=None)
    aws_secret_access_key: str = attrib(default=None)

    sentry_dsn: str = attrib(default=None)  # only needed if using Sentry (www.sentry.io)

    verbose: bool = attrib(default=False)


def get_pref() -> SynckPreferences:
    """
    Use this to access synck preferences (don't instantiate SynckPreferences directly)
    :return: synck preferences
    """
    return SynckPreferences(application_name, author)
