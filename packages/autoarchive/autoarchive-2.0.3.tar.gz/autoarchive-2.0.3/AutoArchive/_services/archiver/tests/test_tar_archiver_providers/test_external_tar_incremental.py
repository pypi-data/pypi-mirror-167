# test_external_tar_incremental.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2017 Róbert Čerňanský



""":class:`TestExternalTarIncremental`."""



__all__ = ["TestExternalTarIncremental"]



# {{{ INCLUDES

import unittest

import glob
import os
import shutil
import time

from AutoArchive._services.archiver._external_tar_archiver_provider import _ExternalTarArchiverProvider
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from AutoArchive._services.archiver.tests.archiver_test_utils import _BackupDefinitionBuilder
from AutoArchive.tests import ComponentTestUtils

# }}} INCLUDES



# {{{ CLASSES

class TestExternalTarIncremental(unittest.TestCase):
    """Tests of external tar archiver provider for incremental backups."""

    __SNAPSHOTS_SUBDIR = "snapshots"



    @classmethod
    def setUpClass(cls):
        ArchiverTestUtils._setUpClassArchiverComponent()



    @classmethod
    def tearDownClass(cls):
        ArchiverTestUtils._tearDownClassArchiverComponent()



    def setUp(self):
        self.__archiverProvider = None
        self.__testFileStructurePath = None
        self.__extractPath = None
        self.__snapshotsDir = None

        self.__snapshotsDir = os.path.join(
            ComponentTestUtils.getComponentTestContext().workDir, self.__SNAPSHOTS_SUBDIR)
        os.mkdir(self.__snapshotsDir)
        self.__archiverProvider = _ExternalTarArchiverProvider(ComponentTestUtils.getComponentTestContext().workDir)



    def tearDown(self):
        if self.__extractPath:
            ArchiverTestUtils._removeExtractedBackup(self.__extractPath)
        for irrelevantFile in glob.glob(ComponentTestUtils.irrelevantValidFilePath + "*"):
            os.remove(irrelevantFile)
        if self.__testFileStructurePath:
            ArchiverTestUtils._removeTestFileStructure(self.__testFileStructurePath)

        shutil.rmtree(self.__snapshotsDir)



    # {{{ incremental backup creation tests

    def test_backupFilesIncrementally_Level0(self):
        """Tests the creation of an incremental backup of level 0.

        Creates an incremental backup and extracts it.  Asserts that the backup content is identical to the archived
        file structure."""

        self.__testFileStructurePath = ArchiverTestUtils._makeTestFileStructure()

        backupDefinition = _BackupDefinitionBuilder()\
            .withRoot(self.__testFileStructurePath)\
            .withIncludeFiles(os.listdir(self.__testFileStructurePath))\
            .build()
        backupFilePath = self.__archiverProvider.backupFilesIncrementally(backupDefinition)

        self.__extractPath = ArchiverTestUtils._extractBackup(backupFilePath)
        self.assertTrue(ArchiverTestUtils._compareDirs(self.__testFileStructurePath, self.__extractPath))



    def test_backupFilesIncrementally_LinksLevel0(self):
        """Tests the creation of an incremental backup of level 0 with file structure containing symlinks.

        Creates an incremental backup and extracts it.  Asserts that the backup content is identical to the archived
        file structure."""

        self.__testFileStructurePath = ArchiverTestUtils._makeTestFileStructure(links = True)

        backupDefinition = _BackupDefinitionBuilder()\
            .withRoot(self.__testFileStructurePath)\
            .withIncludeFiles(os.listdir(self.__testFileStructurePath))\
            .build()
        backupFilePath = self.__archiverProvider.backupFilesIncrementally(backupDefinition)

        self.__extractPath = ArchiverTestUtils._extractBackup(backupFilePath)
        self.assertTrue(ArchiverTestUtils._compareDirs(self.__testFileStructurePath, self.__extractPath))



    def test_backupFilesIncrementally_Level1(self):
        """Tests the creation of an incremental backup of level 1.

        Creates an incremental backup of level 0, modifies the test file structure and creates level 1 backup.  Extracts
        it and asserts that the backup content is identical to the archived file structure."""

        self.__testFileStructurePath = ArchiverTestUtils._makeTestFileStructure()

        backupDefinition = _BackupDefinitionBuilder()\
            .withRoot(self.__testFileStructurePath)\
            .withIncludeFiles(os.listdir(self.__testFileStructurePath))\
            .build()

        # create the level 0 backup
        backupFilePath0 = self.__archiverProvider.backupFilesIncrementally(backupDefinition)

        # rest a little so that file modifications has significantly different time stamps
        time.sleep(1.2)

        # modify the test file structure
        os.remove(os.path.join(self.__testFileStructurePath, str.format(ArchiverTestUtils._DIR_NAME, index = 0),
                               str.format(ArchiverTestUtils._FILE_NAME, index = 1)))
        with open(os.path.join(self.__testFileStructurePath, str.format(ArchiverTestUtils._DIR_NAME, index = 1),
                               "incremental.t"), "w") as testFile:
            testFile.write("Content of the incremental test file.")
        with open(os.path.join(self.__testFileStructurePath, str.format(ArchiverTestUtils._DIR_NAME, index = 1),
                               str.format(ArchiverTestUtils._FILE_NAME, index = 1)), "a") as testFile:
            testFile.write("Additional content of the file for incremental test.")

        # create the level 1 backup
        backupFilePath1 = self.__archiverProvider.backupFilesIncrementally(backupDefinition, level = 1)

        self.assertLess(os.path.getsize(backupFilePath1), os.path.getsize(backupFilePath0))
        self.__extractPath = ArchiverTestUtils._extractBackup((backupFilePath0, backupFilePath1))
        self.assertTrue(ArchiverTestUtils._compareDirs(self.__testFileStructurePath, self.__extractPath))



    def test_backupFilesIncrementally_SpecifiedLevel(self):
        """Tests the creation of an incremental backup of a specified backup level.

        Creates an incremental backup of level 0, modifies the test file structure and creates level 1 backup.  Modifies
        the test file structure again and creates level 1 backup again.  Extracts first and last increments and asserts
        that the backup content is identical to the archived file structure."""

        self.__testFileStructurePath = ArchiverTestUtils._makeTestFileStructure()

        backupDefinition = _BackupDefinitionBuilder()\
            .withRoot(self.__testFileStructurePath)\
            .withIncludeFiles(os.listdir(self.__testFileStructurePath))\
            .build()

        # create the level 0 backup
        backupFilePath0 = self.__archiverProvider.backupFilesIncrementally(backupDefinition)

        # rest a little so that file modifications has significantly different time stamps
        time.sleep(1.2)

        # modify the test file structure
        with open(os.path.join(self.__testFileStructurePath, str.format(ArchiverTestUtils._DIR_NAME, index = 1),
                               "incremental.t"), "w") as testFile:
            testFile.write("Content of the incremental test file.")

        # create the level 1 backup
        self.__archiverProvider.backupFilesIncrementally(backupDefinition, level = 1)

        time.sleep(1.2)

        # modify the test file structure again
        with open(os.path.join(self.__testFileStructurePath, str.format(ArchiverTestUtils._DIR_NAME, index = 1),
                               "incremental2.t"), "w") as testFile:
            testFile.write("Content of the incremental2 test file.")

        # create the level 1 backup again
        backupFilePath1 = self.__archiverProvider.backupFilesIncrementally(backupDefinition, level = 1)

        self.__extractPath = ArchiverTestUtils._extractBackup((backupFilePath0, backupFilePath1))
        self.assertTrue(ArchiverTestUtils._compareDirs(self.__testFileStructurePath, self.__extractPath))

    # }}} incremental backup creation tests



    # {{{ getMaxBackupLevel() tests

    def test_getMaxBackupLevel(self):
        """Tests the obtaining the maximal backup level."""

        TEST_BACKUP_ID = "test backup ID"

        self.__testFileStructurePath = ArchiverTestUtils._makeTestFileStructure()

        backupDefinition = _BackupDefinitionBuilder()\
            .withBackupId(TEST_BACKUP_ID)\
            .withRoot(self.__testFileStructurePath)\
            .withIncludeFiles(os.listdir(self.__testFileStructurePath))\
            .build()
        self.__archiverProvider.backupFilesIncrementally(backupDefinition)

        maxBackupLevel = self.__archiverProvider.getMaxBackupLevel(TEST_BACKUP_ID)

        self.assertEqual(1, maxBackupLevel)



    def test_getMaxBackupLevel_NoBackupYet(self):
        """Tests the obtaining the maximal backup level when no backup was created yet."""

        maxBackupLevel = self.__archiverProvider.getMaxBackupLevel(ArchiverTestUtils._IRRELEVANT_BACKUP_ID)

        self.assertEqual(0, maxBackupLevel)



    def test_getMaxBackupLevel_NameClash(self):
        """Tests the :meth:`_TarArchiverProviderBase.getMaxBackupLevel()` for similar backup IDs.

        Creates two incremental :term:`backups <backup>` so snapshot files are stored for them.  Backup IDs are
        deliberately chosen to be similar (one ID is a substring of the other).  Created number of backup levels of the
        archive with shorter ID will be lower than of the other.  As the shorter name substring matches also the longer
        name, this tests the possibility of incorrect file name matching while determining the backup level by counting
        the snapshot files.  Checks that the reported maximal backup level of the archive with shorter name is
        correct."""

        BACKUP_ID_1 = "test_backup"
        BACKUP_ID_2 = BACKUP_ID_1 + "_2"

        self.__testFileStructurePath = ArchiverTestUtils._makeTestFileStructure()

        # creates the level 0 backup for BACKUP_ID_1
        backupDefinition = _BackupDefinitionBuilder()\
            .withBackupId(BACKUP_ID_1)\
            .withRoot(self.__testFileStructurePath)\
            .withIncludeFiles(os.listdir(self.__testFileStructurePath))\
            .build()
        self.__archiverProvider.backupFilesIncrementally(backupDefinition)

        # creates levels 0 and 1 backups for BACKUP_ID_2
        backupDefinition = _BackupDefinitionBuilder()\
            .withBackupId(BACKUP_ID_2)\
            .withRoot(self.__testFileStructurePath)\
            .withIncludeFiles(os.listdir(self.__testFileStructurePath))\
            .build()
        self.__archiverProvider.backupFilesIncrementally(backupDefinition)
        self.__archiverProvider.backupFilesIncrementally(backupDefinition, level = 1)

        maxBackupLevel = self.__archiverProvider.getMaxBackupLevel(BACKUP_ID_1)

        self.assertEqual(1, maxBackupLevel)

    # }}} getMaxBackupLevel() tests



    # {{{ getStoredBackupIds() tests

    def test_getStoredBackupIds(self):
        """Tests the obtaining backup IDs of all known backups."""

        TEST_BACKUP_IDS = ("test backup 1", "test backup 2", "test backup 3")

        self.__testFileStructurePath = ArchiverTestUtils._makeTestFileStructure()

        backupDefinitionBuilderWithFiles = _BackupDefinitionBuilder()\
            .withRoot(self.__testFileStructurePath)\
            .withIncludeFiles(os.listdir(self.__testFileStructurePath))

        for backupId in TEST_BACKUP_IDS:
            backupDefinition = backupDefinitionBuilderWithFiles\
                .withBackupId(backupId)\
                .build()
            self.__archiverProvider.backupFilesIncrementally(backupDefinition)

        # create also level 1 of one of the backups
        backupDefinition = backupDefinitionBuilderWithFiles\
            .withBackupId(TEST_BACKUP_IDS[1])\
            .build()
        self.__archiverProvider.backupFilesIncrementally(backupDefinition, level = 1)

        storedBackupIds = self.__archiverProvider.getStoredBackupIds()

        self.assertCountEqual(TEST_BACKUP_IDS, storedBackupIds)

    # }}} getStoredBackupIds() tests

# }}} CLASSES
