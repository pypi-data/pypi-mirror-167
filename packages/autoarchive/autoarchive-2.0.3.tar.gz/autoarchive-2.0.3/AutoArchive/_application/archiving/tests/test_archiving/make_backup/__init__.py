# __init__.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2014 Róbert Čerňanský



"""Component tests for :term:`IArchiving.makeBackup` API."""



from .test_archive_types import *
from .test_show_final_error import *
from .test_incremental_backup_creation import *
from .test_backup_restarting import *
from .test_keep_old_backups import *
from .test_keep_old_incremental_backups import *
from .test_options_priority import *
from .test_execute_commands import *



__all__ = test_archive_types.__all__ + test_show_final_error.__all__ + test_incremental_backup_creation.__all__ + \
    test_backup_restarting.__all__ + test_keep_old_backups.__all__ + test_keep_old_incremental_backups.__all__ + \
    test_options_priority.__all__ + test_execute_commands.__all__
