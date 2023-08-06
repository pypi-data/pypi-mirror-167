# __init__.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2016 Róbert Čerňanský



"""Component tests for :class:`ArchivingApplication` API."""



from .test_actions import *
from .test_execute_set_commands import *



__all__ = test_actions.__all__ + test_execute_set_commands.__all__
