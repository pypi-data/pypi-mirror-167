# test_backup_restarting.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2017 Róbert Čerňanský



""":class:`TestBackupRestarting`."""



__all__ = ["TestBackupRestarting"]



# {{{ INCLUDES

import unittest
import os
from datetime import datetime, timedelta

from AutoArchive._infrastructure.configuration import Options
from AutoArchive._application.archiving.archive_spec import ConfigConstants
from AutoArchive.tests import ComponentTestUtils
from AutoArchive._infrastructure.storage.tests import StorageTestUtils
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from AutoArchive._application.archiving.archive_spec.tests import ArchiveSpecTestUtils
from ...archiving_test_utils import ArchivingTestUtils

# }}} INCLUDES



# {{{ CLASSES

class TestBackupRestarting(unittest.TestCase):
    "Test of :meth:`._Archiving.makeBackup()` method for the backup level restarting."

    @classmethod
    def setUpClass(cls):
        ArchivingTestUtils._setUpClassArchivingComponent()



    @classmethod
    def tearDownClass(cls):
        ArchivingTestUtils._tearDownClassArchivingComponent()



    def setUp(self):
        self.__archiveSpecFilePath = None
        self.__irrelevantFilePath = None
        self.__storageState = {}

        ArchivingTestUtils._setUpArchivingComponent()

        self.__irrelevantFilePath = ComponentTestUtils.createIrrelevantFile()
        self.__archiveSpecFilePath = ArchiveSpecTestUtils.makeArchiveSpecFile()



    def tearDown(self):
        ComponentTestUtils.removeIrrelevantFile()

        ArchivingTestUtils._tearDownArchivingComponent()



    # {{{ makeBackup() tests for backup level restarting

    def test_makeBackupRestartAfterLevel(self):
        """Tests the makeBackup() method for restarting a level after a specific level was reached.

        Configures that the backup level shall be restarted after level 2.  Creates four incremental backups expecting
        that at fourth time the level will be restarted to 1.  Checks that the service method was called to create
        backup of level 1."""

        RESTART_AFTER_LEVEL = 2

        archiverMock = ArchiverTestUtils.createArchiverMock()

        options = {
            Options.RESTART_AFTER_LEVEL: RESTART_AFTER_LEVEL
        }

        # call the backup creation for RESTART_AFTER_LEVEL + 2 times so it should be restarted
        self.__createRestartableArchives(archiverMock, options, RESTART_AFTER_LEVEL + 2)

        # check that the last call of backupFilesIncrementally() was with backup level 1
        self.assertEqual(1, archiverMock.backupFilesIncrementally.call_args[0][2],
                         "The backup creation on the service was not called with expected backup level.")



    def test_makeBackupRestartAfterDays(self):
        """Tests the makeBackup() method for restarting a level after a specific number of days passed.

        Configures that the backup level shall be restarted after 3 days.  Creates a level 0, level 1 and level 2
        backups.  Modify value of last restart in the storage mock so that it is older than 3 days.  Calls the backup
        creation once more attempting to create the backup of level 3 but it should be restarted.  Checks that the
        service method was called to create backup of level 1."""

        RESTART_AFTER_AGE = 3

        NUMBER_OF_CREATED_LEVELS = 3

        STORAGE_LAST_RESTART = "archiving-last-restart"

        archiverMock = ArchiverTestUtils.createArchiverMock()

        options = {
            Options.RESTART_AFTER_LEVEL: 100, # has to be greater than NUMBER_OF_CREATED_LEVELS
            Options.RESTART_AFTER_AGE: RESTART_AFTER_AGE
        }

        # call the backup creation for NUMBER_OF_CREATED_LEVELS times
        self.__createRestartableArchives(archiverMock, options, NUMBER_OF_CREATED_LEVELS,
                                         archiveSpecFile = self.__archiveSpecFilePath)

        # decrease last restart date by RESTART_AFTER_AGE + 1 days

        # >beware that how the date of the last restart is stored is internal to the Archiving component so the
        # >following code may break without the interface change; well, not great but much better than to let this test
        # >to wait couple of days

        # >from the name of the archive specification file we get the realm
        realm = os.path.basename(self.__archiveSpecFilePath).replace(ConfigConstants.ARCHIVE_SPEC_EXT, "")

        # >get the last restart date, decrease it and store back
        lastRestartStr = self.__storageState[realm][StorageTestUtils.DEFAULT_SECTION][STORAGE_LAST_RESTART]
        lastRestart = datetime.strptime(lastRestartStr, "%Y-%m-%d").date()
        self.__storageState[realm][StorageTestUtils.DEFAULT_SECTION][STORAGE_LAST_RESTART] = \
            str(lastRestart - timedelta(RESTART_AFTER_AGE + 1))

        jointOptions = {
            Options.RESTARTING: True
        }
        jointOptions.update(options)

        # call the backup creation one more time with max. backup level set to NUMBER_OF_CREATED_LEVELS
        ArchivingTestUtils._createIncrementalBackup(archiverMock, jointOptions, NUMBER_OF_CREATED_LEVELS,
                                                    self.__storageState, self.__archiveSpecFilePath)

        # check that the last call of backupFilesIncrementally() was with backup level 1
        self.assertEqual(1, archiverMock.backupFilesIncrementally.call_args[0][2],
                         "The backup creation on the service was not called with expected backup level.")



    def test_makeBackupFullRestartAfterCount(self):
        """Tests the makeBackup() method for full level restarting after a specific number of restarts.

        Configures values for backup level restart and full backup level restart.  Creates number of backups so that
        the level shall be fully restarted.  Checks that the service method was called to create backup of level 0."""

        RESTART_AFTER_LEVEL = 1
        FULL_RESTART_AFTER_COUNT = 1

        archiverMock = ArchiverTestUtils.createArchiverMock()

        options = {
            Options.RESTART_AFTER_LEVEL: RESTART_AFTER_LEVEL,
            Options.FULL_RESTART_AFTER_COUNT: FULL_RESTART_AFTER_COUNT
        }

        # call the backup creation for number of times required to full restart; for the first time the level is
        # restarted after RESTART_AFTER_LEVEL + 1 backups are created; later on the level is restarted after each
        # backup creation (because the max. backup level is already higher than RESTART_AFTER_LEVEL), so we need to
        # make FULL_RESTART_AFTER_COUNT additional backups; finally yet one additional backup creation shall do the
        # _full_ restart
        self.__createRestartableArchives(archiverMock, options, RESTART_AFTER_LEVEL + FULL_RESTART_AFTER_COUNT + 2)

        # check that the last call of backupFilesIncrementally() was with backup level 0
        self.assertEqual(0, archiverMock.backupFilesIncrementally.call_args[0][2],
                         "The backup creation on the service was not called with expected backup level.")



    def test_makeBackupFullRestartAfterDays(self):
        """Tests the makeBackup() method for full restarting a level after a specific number of days passed.

        Configures that the backup level shall be fully restarted after 3 days.  Creates a level 0 and level 1
        archives.  Modify value of last full restart in the storage mock so that it is older than 3 days.  Removes all
        created backup files and creates a one more backup which should be level 0 due to full restarting.  Checks that
        the backup file of level 0 was created."""

        FULL_RESTART_AFTER_AGE = 3

        NUMBER_OF_CREATED_LEVELS = 3

        STORAGE_LAST_FULL_RESTART = "archiving-last-full-restart"

        archiverMock = ArchiverTestUtils.createArchiverMock()

        options = {
            Options.RESTART_AFTER_LEVEL: 100, # has to be greater than NUMBER_OF_CREATED_LEVELS
            Options.FULL_RESTART_AFTER_AGE: FULL_RESTART_AFTER_AGE
        }

        # call the backup creation for NUMBER_OF_CREATED_LEVELS times
        self.__createRestartableArchives(archiverMock, options, NUMBER_OF_CREATED_LEVELS,
                                         archiveSpecFile = self.__archiveSpecFilePath)

        # decrease last full restart date by FULL_RESTART_AFTER_AGE + 1 days

        # >beware that how the date of the last full restart is stored is internal to the Archiving component so the
        # >following code may break without the interface change; well, not great but much better than to let this test
        # >to wait couple of days

        # >from the name of the archive specification file we get the realm
        realm = os.path.basename(self.__archiveSpecFilePath).replace(ConfigConstants.ARCHIVE_SPEC_EXT, "")

        # >get the last full restart date, decrease it and store back
        lastRestartStr = self.__storageState[realm][StorageTestUtils.DEFAULT_SECTION][STORAGE_LAST_FULL_RESTART]
        lastRestart = datetime.strptime(lastRestartStr, "%Y-%m-%d").date()
        self.__storageState[realm][StorageTestUtils.DEFAULT_SECTION][STORAGE_LAST_FULL_RESTART] = \
            str(lastRestart - timedelta(FULL_RESTART_AFTER_AGE + 1))

        jointOptions = {
            Options.RESTARTING: True
        }
        jointOptions.update(options)

        # call the backup creation one more time with max. backup level set to NUMBER_OF_CREATED_LEVELS
        ArchivingTestUtils._createIncrementalBackup(archiverMock, jointOptions, NUMBER_OF_CREATED_LEVELS,
                                                    self.__storageState, self.__archiveSpecFilePath)

        # check that the last call of backupFilesIncrementally() was with backup level 0
        self.assertEqual(0, archiverMock.backupFilesIncrementally.call_args[0][2],
                         "The backup creation on the service was not called with expected backup level.")



    def test_makeBackupMaxRestartLevelSize_NotAllowed(self):
        """Tests the makeBackup() method for restarting to a higher level due to max. size reached.

        Configures that the backup level shall be restarted after level 2 and that the size of the target level can not
        exceed 60% of level 0 backup size.  Creates a level 0 backup then the level 1 backup with the service mock
        set up so that it creates (backup) file bigger than 60% of the level 0 (backup) file.  Finally, creates two
        more backups so that level is restarted.  Checks that the service method was called to create backup of level 2
        (which means that it was not allowed to restart to level 1)."""

        LEVEL0_SIZE = 10
        MAX_RESTART_LEVEL_SIZE = 60
        BACKUP_ID = "test backup"

        # create files which will represent backup files of particular levels
        # >create level 0 backup file of size LEVEL0_SIZE
        level0Backup = os.path.join(ComponentTestUtils.getComponentTestContext().workDir, BACKUP_ID + ".0")
        with open(level0Backup, "wb") as level0BackupStream:
            level0BackupStream.write(b"x" * LEVEL0_SIZE)

        # >create level 1 backup file which size is MAX_RESTART_LEVEL_SIZE + 15 percent of the level 0 size
        level1Backup = os.path.join(ComponentTestUtils.getComponentTestContext().workDir, BACKUP_ID + ".1")
        with open(level1Backup, "wb") as level1BackupStream:
            level1BackupStream.write(b"x" * round(LEVEL0_SIZE * ((MAX_RESTART_LEVEL_SIZE + 15) / 100)))

        archiverMock = ArchiverTestUtils.createArchiverMock()
        archiveSpecFilePath = ArchiveSpecTestUtils.makeArchiveSpecFile(name = BACKUP_ID)

        options = {
            Options.RESTARTING: True,
            Options.RESTART_AFTER_LEVEL: 2,
            Options.MAX_RESTART_LEVEL_SIZE: MAX_RESTART_LEVEL_SIZE
        }

        # call the backup creation for level 0
        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, 0, self.__storageState, archiveSpecFilePath)

        # call the backup creation for level 1
        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, 1, self.__storageState, archiveSpecFilePath)

        os.remove(level0Backup)
        os.remove(level1Backup)

        # call the backup creation for last two levels so it gets restarted
        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, 2, self.__storageState, archiveSpecFilePath)
        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, 3, self.__storageState, archiveSpecFilePath)

        # check that the last call of backupFilesIncrementally() was with backup level 2
        self.assertEqual(2, archiverMock.backupFilesIncrementally.call_args[0][2],
                         "The backup creation on the service was not called with expected backup level.")



    def test_makeBackupMaxRestartLevelSize_Allowed(self):
        """Tests the makeBackup() method for restarting not to a higher level.

        Configures that the backup level shall be restarted after level 2 and that the size of the target level can not
        exceed 60% of level 0 backup size.  Creates a level 0 backup then the level 1 backup with the service mock
        set up so that it creates (backup) file smaller than 60% of the level 0 (backup) file.  Finally, creates two
        more backups so that level is restarted.  Checks that the service method was called to create backup of level 1
        (which means that it was allowed to restart to level 1)."""

        LEVEL0_SIZE = 10
        MAX_RESTART_LEVEL_SIZE = 60
        BACKUP_ID = "test backup"

        # create files which will represent backup files of particular levels
        # >create level 0 backup file of size LEVEL0_SIZE
        level0Backup = os.path.join(ComponentTestUtils.getComponentTestContext().workDir, BACKUP_ID + ".0")
        with open(level0Backup, "wb") as level0BackupStream:
            level0BackupStream.write(b"x" * LEVEL0_SIZE)

        # >create level 1 backup file which size is MAX_RESTART_LEVEL_SIZE - 15 percent of the level 0 size
        level1Backup = os.path.join(ComponentTestUtils.getComponentTestContext().workDir, BACKUP_ID + ".1")
        with open(level1Backup, "wb") as level1BackupStream:
            level1BackupStream.write(b"x" * round(LEVEL0_SIZE * ((MAX_RESTART_LEVEL_SIZE - 15) / 100)))

        archiverMock = ArchiverTestUtils.createArchiverMock()
        archiveSpecFilePath = ArchiveSpecTestUtils.makeArchiveSpecFile(name = BACKUP_ID)

        options = {
            Options.RESTARTING: True,
            Options.RESTART_AFTER_LEVEL: 2,
            Options.MAX_RESTART_LEVEL_SIZE: MAX_RESTART_LEVEL_SIZE
        }

        # call the backup creation for level 0
        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, 0, self.__storageState, archiveSpecFilePath)

        # call the backup creation for level 1
        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, 1, self.__storageState, archiveSpecFilePath)

        os.remove(level0Backup)
        os.remove(level1Backup)

        # call the backup creation for last two levels so it gets restarted
        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, 2, self.__storageState, archiveSpecFilePath)
        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, 3, self.__storageState, archiveSpecFilePath)

        # check that the last call of backupFilesIncrementally() was with backup level 1
        self.assertEqual(1, archiverMock.backupFilesIncrementally.call_args[0][2],
                         "The backup creation on the service was not called with expected backup level.")

    # }}} makeBackup() tests for backup level restarting



    # {{{ helpers for makeBackup() tests for backup level restarting

    def __createRestartableArchives(self, archiverMock, options = None, levels = 1, archiveSpecFile = None):
        if options is None: options = {}

        jointOptions = {
            Options.RESTARTING: True
        }
        jointOptions.update(options)

        ArchivingTestUtils._createIncrementalBackups(archiverMock, jointOptions, levels, self.__storageState,
                                                     archiveSpecFile)

    # }}} helpers for makeBackup() tests for backup level restarting

# }}} CLASSES
