# __init__.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2016 Róbert Čerňanský



"""Component tests for :class:`_InternalTarArchiverProvider` and :class:`_ExternalTarArchiverProvider` API."""



from .test_backup_types import *
from .test_content import *
from .test_backup_removal import *
from .test_external_tar_incremental import *
from .test_backup_preservation import *



__all__ = test_backup_types.__all__ + test_content.__all__ + test_backup_removal.__all__ + \
          test_external_tar_incremental.__all__ + test_backup_preservation.__all__
