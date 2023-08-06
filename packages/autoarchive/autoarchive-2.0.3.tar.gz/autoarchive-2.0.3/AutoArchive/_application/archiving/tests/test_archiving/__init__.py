# __init__.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2014 Róbert Čerňanský



"""Component tests for :term:`IArchiving` API."""



from .make_backup import *
from .configured_archive_info import *
from .stored_archive_info import *



__all__ = make_backup.__all__ + configured_archive_info.__all__ + stored_archive_info.__all__
