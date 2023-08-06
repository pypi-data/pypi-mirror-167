# test_incremental_backup_creation.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2017 Róbert Čerňanský



""":class:`TestIncrementalBackupCreation`."""



__all__ = ["TestIncrementalBackupCreation"]



# {{{ INCLUDES

import unittest
import itertools
import re

import mock

from AutoArchive._infrastructure.configuration import Options
from AutoArchive._ui.cmdline._cmdline_ui import CmdlineUi
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from ...archiving_test_utils import ArchivingTestUtils

# }}} INCLUDES



# {{{ CLASSES

class TestIncrementalBackupCreation(unittest.TestCase):
    "Test of :meth:`._Archiving.makeBackup()` method for the incremental backup."

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



    # {{{ makeBackup() tests for incremental archiving

    def test_makeBackupIncremental(self):
        """Tests the makeBackup() method to create an incremental archive.

        Calls an incremental backup creation and check that the right service method was called and the passed backup
        level value was the same as the maximal backup level was set to."""

        MAX_BACKUP_LEVEL = 10

        archiverMock = ArchiverTestUtils.createArchiverMock()

        # call the backup creation
        ArchivingTestUtils._createIncrementalBackup(archiverMock, maxBackupLevel = MAX_BACKUP_LEVEL)

        # check that the backupFilesIncrementally() was called and that it was called with correct value of the
        # backup level argument
        self.assertTrue(archiverMock.backupFilesIncrementally.called)
        self.assertEqual(MAX_BACKUP_LEVEL, archiverMock.backupFilesIncrementally.call_args[0][2])



    def test_makeBackupIncrementalLevel(self):
        """Tests the makeBackup() method to create an incremental backup of a specified level.

        Sets-up the service so it returns maximal backup level 2.  Calls an incremental backup creation of the level 1.
        Checks that the right service method was called with the same backup level."""

        MAX_BACKUP_LEVEL = 2
        BACKUP_LEVEL = MAX_BACKUP_LEVEL - 1

        archiverMock = ArchiverTestUtils.createArchiverMock()

        # call the backup creation
        ArchivingTestUtils._createIncrementalBackup(archiverMock, {Options.LEVEL: BACKUP_LEVEL}, MAX_BACKUP_LEVEL)

        # check that the backupFilesIncrementally() was called with correct value of the backup level argument
        self.assertEqual(BACKUP_LEVEL, archiverMock.backupFilesIncrementally.call_args[0][2])



    def test_makeBackupIncrementalLevelTooHigh(self):
        """Tests the makeBackup() method to create an incremental backup of specified level which is too high.

        Sets-up the service so it returns maximal backup level 2.  Calls an incremental backup creation of the level 3.
        Checks that the right service method was called with the same backup level as the maximal.  Also checks that
        the message that the backup level is too high was shown."""

        MAX_BACKUP_LEVEL = 2
        BACKUP_LEVEL = MAX_BACKUP_LEVEL + 1

        archiverMock = ArchiverTestUtils.createArchiverMock()
        componentUiMock = mock.Mock(spec_set = CmdlineUi)

        # call the backup creation
        ArchivingTestUtils._createIncrementalBackup(archiverMock, {Options.LEVEL: BACKUP_LEVEL}, MAX_BACKUP_LEVEL,
                                                    componentUiMock = componentUiMock)

        # check that the backupFilesIncrementally() was called with correct value of the backup level argument
        self.assertEqual(MAX_BACKUP_LEVEL, archiverMock.backupFilesIncrementally.call_args[0][2])

        # check that warning message that the level is too high was shown
        warningCallsArgs = (methodCall[1]
                            for methodCall in componentUiMock.method_calls
                            if methodCall[0] == "showWarning")
        socketIgnoredCallsArgs = itertools.dropwhile(
            lambda callArg: re.search("level.*too.*high", callArg[0], re.IGNORECASE) is None, warningCallsArgs)
        self.assertIsNotNone(next(socketIgnoredCallsArgs, None),
                             "A warning message that the level is too high was not shown.")



    def test_makeBackupIncrementalRemoveObsolete(self):
        """Tests the makeBackup() method for removal of obsolete backups.

        Enables option for obsolete backups removal and sets-up service so that maximal backup level is 2.  Calls an
        incremental backup creation of level 1.  Asserts that a service method for backup removal was called with
        correct "level" parameter."""

        MAX_BACKUP_LEVEL = 2
        BACKUP_LEVEL = MAX_BACKUP_LEVEL - 1

        archiverMock = ArchiverTestUtils.createArchiverMock()

        options = {
            Options.LEVEL: BACKUP_LEVEL,
            Options.REMOVE_OBSOLETE_BACKUPS: True
        }

        # call the backup creation
        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, MAX_BACKUP_LEVEL)

        # check that the removeBackupIncrements() was called with correct value of the backup level argument
        self.assertEqual(BACKUP_LEVEL + 1, archiverMock.removeBackupIncrements.call_args[0][1])

    # }}} makeBackup() tests for incremental archiving


# }}} CLASSES
