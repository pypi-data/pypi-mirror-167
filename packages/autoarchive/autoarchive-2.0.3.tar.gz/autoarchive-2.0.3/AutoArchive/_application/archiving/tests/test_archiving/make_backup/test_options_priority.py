# test_options_priority.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2017 Róbert Čerňanský



""":class:`TestOptionsPriority`."""



__all__ = ["TestOptionsPriority"]



# {{{ INCLUDES

import unittest

from AutoArchive._infrastructure.configuration import Options, ArchiverTypes
from AutoArchive.tests import ComponentTestUtils
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from ...archiving_test_utils import ArchivingTestUtils

# }}} INCLUDES



# {{{ CLASSES

class TestOptionsPriority(unittest.TestCase):
    """Test of :meth:`._Archiving.makeBackup()` method for priority of configuration options vs. .aa file."""



    @classmethod
    def setUpClass(cls):
        ArchivingTestUtils._setUpClassArchivingComponent()



    @classmethod
    def tearDownClass(cls):
        ArchivingTestUtils._tearDownClassArchivingComponent()



    def setUp(self):
        ArchivingTestUtils._setUpArchivingComponent()



    def tearDown(self):
        ArchivingTestUtils._tearDownArchivingComponent()



    # {{{ makeBackup() tests for options priority

    def test_makeBackupConfigOptionOverride(self):
        """Tests the makeBackup() method for overriding a configuration option by the
        :term:`archive specification file`.

        Overrides :attr:`.Options.ARCHIVER` configured option by a new value in :term:`archive specification file` and
        creates a backup.  Checks that the service was called to create the backup type specified in archive
        specification file was created."""

        AA_SPEC_ARCHIVER = ArchiverTypes.TarGzInternal

        options = {
            Options.USER_CONFIG_DIR: ComponentTestUtils.getComponentTestContext().userConfigDir,
            Options.ARCHIVER: ArchiverTypes.TarBz2Internal
        }

        archiverMock = ArchiverTestUtils.createArchiverMock()

        ArchivingTestUtils._createBackup(archiverMock, options, archiverType = AA_SPEC_ARCHIVER)

        # test that the service was called to create backup type configured in .aa file
        self.assertEqual(ArchivingTestUtils._ARCHIVER_TYPE_TO_BACKUP_TYPE_MAP[AA_SPEC_ARCHIVER],
                         archiverMock.backupFiles.call_args[0][0].backupType)



    # Strictly speaking, this is a test for Configuration component functionality
    def test_makeBackupConfigOptionOverrideForce(self):
        """Tests the makeBackup() method for overriding a ``force-`` config. option by the
        :term:`archive specification file`.

        Overrides :attr:`.Options.FORCE_ARCHIVER` configured option by a new value in :term:`archive specification file`
        and creates a backup.  Checks that the service was called to create the backup type specified in the
        ``force-`` option (i. e. that the ``force-`` option was not overridden)."""

        AA_SPEC_ARCHIVER = ArchiverTypes.TarGzInternal
        FORCED_ARCHIVER = ArchiverTypes.TarBz2Internal

        options = {
            Options.USER_CONFIG_DIR: ComponentTestUtils.getComponentTestContext().userConfigDir,
            Options.FORCE_ARCHIVER: FORCED_ARCHIVER
        }

        archiverMock = ArchiverTestUtils.createArchiverMock()

        ArchivingTestUtils._createBackup(archiverMock, options, AA_SPEC_ARCHIVER)

        # test that the service was called to create forced backup type
        self.assertEqual(ArchivingTestUtils._ARCHIVER_TYPE_TO_BACKUP_TYPE_MAP[FORCED_ARCHIVER],
                         archiverMock.backupFiles.call_args[0][0].backupType)

    # }}} makeBackup() tests for options priority

# }}} CLASSES
