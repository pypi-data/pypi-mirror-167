# test_backup_removal.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2016 Róbert Čerňanský



""":class:`TestInternalTarBackupRemoval`, :class:`TestExternalTarBackupRemoval`."""



__all__ = ["TestInternalTarBackupRemoval", "TestExternalTarBackupRemoval"]



# {{{ INCLUDES

import unittest

import os
import shutil

from AutoArchive._services.archiver._external_tar_archiver_provider import _ExternalTarArchiverProvider
from AutoArchive._services.archiver._internal_tar_archiver_provider import _InternalTarArchiverProvider
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from AutoArchive._services.archiver.tests.archiver_test_utils import _BackupDefinitionBuilder
from AutoArchive.tests import ComponentTestUtils

# }}} INCLUDES



# {{{ CLASSES

# TODO: Test for removal of kept backup.
class TestInternalTarBackupRemoval(unittest.TestCase):
    """Tests of internal tar archiver provider for backup removal functionality."""

    @classmethod
    def setUpClass(cls):
        ArchiverTestUtils._setUpClassArchiverComponent()



    @classmethod
    def tearDownClass(cls):
        ArchiverTestUtils._tearDownClassArchiverComponent()



    def setUp(self):
        self.__archiverProvider = _InternalTarArchiverProvider(ComponentTestUtils.getComponentTestContext().workDir)



    def test_RemoveBackup(self):
        """Tests the removal of a backup."""

        backupDefinition = _BackupDefinitionBuilder().build()
        backupFilePath = self.__archiverProvider.backupFiles(backupDefinition)

        self.__archiverProvider.removeBackup(backupDefinition)

        self.assertFalse(os.path.isfile(backupFilePath), "The backup file was not removed.")


class TestExternalTarBackupRemoval(unittest.TestCase):
    """Tests of external tar archiver provider for backup removal functionality."""

    __SNAPSHOTS_SUBDIR = "snapshots"



    @classmethod
    def setUpClass(cls):
        ArchiverTestUtils._setUpClassArchiverComponent()



    @classmethod
    def tearDownClass(cls):
        ArchiverTestUtils._tearDownClassArchiverComponent()



    def setUp(self):
        self.__snapshotsDir = None
        self.__archiverProvider = None

        self.__snapshotsDir = os.path.join(
            ComponentTestUtils.getComponentTestContext().workDir, self.__SNAPSHOTS_SUBDIR)
        os.mkdir(self.__snapshotsDir)
        self.__archiverProvider = _ExternalTarArchiverProvider(ComponentTestUtils.getComponentTestContext().workDir)



    def tearDown(self):
        shutil.rmtree(self.__snapshotsDir)



    def test_RemoveBackup(self):
        """Tests the removal of a non-incremental backup."""

        backupDefinition = _BackupDefinitionBuilder().build()
        backupFilePath = self.__archiverProvider.backupFiles(backupDefinition)

        self.__archiverProvider.removeBackup(backupDefinition)

        self.assertFalse(os.path.isfile(backupFilePath), "The backup file was not removed.")



    def test_removeBackupIncrements(self):
        """Tests the removal of backup levels of an incremental backup.

        Creates incremental backups of level 0 and level 1.  Removes the level 1 backup.  Asserts that level 1 backup
        was removed and the level 0 remained."""

        backupDefinition = _BackupDefinitionBuilder().build()

        # create the level 0 and level 1 backups
        backupFilePath0 = self.__archiverProvider.backupFilesIncrementally(backupDefinition)
        backupFilePath1 = self.__archiverProvider.backupFilesIncrementally(backupDefinition, level = 1)

        self.__archiverProvider.removeBackupIncrements(backupDefinition, level = 1)

        self.assertFalse(os.path.exists(backupFilePath1), "The backup file was not removed.")
        self.assertTrue(os.path.exists(backupFilePath0), "The backup file was removed.")



    def test_removeBackupIncrements_SetBackupLevel(self):
        """Tests that obsolete backup levels are being removed.

        Creates incremental backups of level 0 and level 1.  Removes the level 1 backup.  Asserts that the next level
        that would be created is level 1."""

        backupDefinition = _BackupDefinitionBuilder().build()

        # create the level 0 and level 1 backups
        self.__archiverProvider.backupFilesIncrementally(backupDefinition)
        self.__archiverProvider.backupFilesIncrementally(backupDefinition, level = 1)

        self.__archiverProvider.removeBackupIncrements(backupDefinition, level = 1)

        self.assertEqual(1, self.__archiverProvider.getMaxBackupLevel(backupDefinition.backupId))

# }}} CLASSES
