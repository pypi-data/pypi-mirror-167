# test_keep_old_backups.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2017 Róbert Čerňanský



""":class:`TestKeepOldBackups`."""



__all__ = ["TestKeepOldBackups"]



# {{{ INCLUDES

import unittest

from AutoArchive._infrastructure.configuration import Options
from AutoArchive._services.archiver.tests.archiver_test_utils import ArchiverTestUtils
from ...archiving_test_utils import ArchivingTestUtils

# }}} INCLUDES



# {{{ CLASSES

class TestKeepOldBackups(unittest.TestCase):
    "Test of :meth:`._Archiving.makeBackup()` method for the keeping of old backups."

    # standard keeping IDs enumeration
    __KEEPING_IDS = (None, "aa", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj")



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



    # {{{ makeBackup() tests for old backup keeping

    def test_makeBackupKeepOldBackup(self):
        """Tests the basic use case of backup keeping.

        Creates a backup and checks that the original one was kept."""

        # setup service so that single backup is exists, none is kept
        EXISTING_BACKUPS_KEEPING_IDS = (None,)

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True
        }

        ArchivingTestUtils._createBackup(archiverMock, options)

        self.assertTrue(archiverMock.keepBackup.called)
        self.assertEqual(EXISTING_BACKUPS_KEEPING_IDS[0], archiverMock.keepBackup.call_args[0][1],
                         "Backup with wrong keeping ID was kept.")
        self.assertEqual(self.__KEEPING_IDS[1], archiverMock.keepBackup.call_args[0][2],
                         "Backup was kept under wrong keeping ID.")



    def test_makeBackupKeepOldBackupNumberOfOldBackups(self):
        """Tests the backup keeping with defined number of kept backups.

        Sets up the archiver service so that it returns 5 existing backups (one normal and four kept).  Configuration
        option for number of old backup to be kept is set to 2.  Then creates a backup and asserts that second
        kept backup is removed and that the rest of the backups is kept correctly."""

        # setup service so that defined backups are kept
        EXISTING_BACKUPS_KEEPING_IDS = self.__KEEPING_IDS[:5]

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: 2
        }

        ArchivingTestUtils._createBackup(archiverMock, options)

        # check that removal of only the last backup is called
        self.assertEqual(1, archiverMock.removeBackup.call_count, "None or more than one backup was removed.")
        self.assertEqual(EXISTING_BACKUPS_KEEPING_IDS[options[Options.NUMBER_OF_OLD_BACKUPS]],
                         archiverMock.removeBackup.call_args[0][1], "The last kept backup was not removed.")

        for keepingIdNum in range(options[Options.NUMBER_OF_OLD_BACKUPS] - 1, -1, -1):
            keepBackupArgs = \
                archiverMock.keepBackup.call_args_list[options[Options.NUMBER_OF_OLD_BACKUPS] - 1 - keepingIdNum][0]
            self.assertEqual(EXISTING_BACKUPS_KEEPING_IDS[keepingIdNum], keepBackupArgs[1],
                             "Backup with wrong keeping ID was kept.")
            self.assertEqual(self.__KEEPING_IDS[keepingIdNum + 1], keepBackupArgs[2],
                             "Backup was kept under wrong keeping ID.")



    def test_makeBackupKeepOldBackupNumberOfOldBackupsWithKeepingIdHoles(self):
        """Tests the backup keeping with defined number of kept backups which are not continuous.

        Sets up the archiver service so that it returns several kept backups with some missing ones.  Configuration
        option for number of old backup to be kept is set to 6.  Then creates a backup and asserts that second
        kept backup is removed and that the rest of the backups is kept correctly."""

        # setup service so that defined backups are kept
        EXISTING_BACKUPS_KEEPING_IDS = self.__KEEPING_IDS[:3] + self.__KEEPING_IDS[5:7]

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: 6
        }

        ArchivingTestUtils._createBackup(archiverMock, options)

        self.assertEqual(3, archiverMock.keepBackup.call_count, "Wrong number of backup's increments was kept.")
        self.__assertKeptBackup(archiverMock, None, "aa")
        self.__assertKeptBackup(archiverMock, "aa", "ab")
        self.__assertKeptBackup(archiverMock, "ab", "ac")
        self.assertFalse(archiverMock.removeBackup.called, "Some backups were removed.")



    def test_makeBackupKeepOldBackupNumberOfOldBackupsRemoveObsolete(self):
        """Tests the backup keeping with defined number of kept backups and removing obsolete backups.

        Sets up the archiver service so that it returns 6 existing backups (one normal and five kept).  Configuration
        option for number of old backup to be kept is set to 3 and removing obsolete backups is enabled.  Then
        creates a backup and asserts that all kept obsolete backups are removed and that the rest of the backups
        is kept correctly."""

        # setup service so that defined backups are kept
        EXISTING_BACKUPS_KEEPING_IDS = (None, "aa", "ab", "ac", "ad", "af")

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.REMOVE_OBSOLETE_BACKUPS: True,
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: 3
        }

        # call the tested method
        ArchivingTestUtils._createBackup(archiverMock, options)

        # check that all obsolete kept backups were removed
        self.assertEqual(len(EXISTING_BACKUPS_KEEPING_IDS) - options[Options.NUMBER_OF_OLD_BACKUPS],
                         archiverMock.removeBackup.call_count, "Wrong number of backups were removed.")
        self.assertEqual(EXISTING_BACKUPS_KEEPING_IDS[options[Options.NUMBER_OF_OLD_BACKUPS]],
                         archiverMock.removeBackup.call_args_list[0][0][1],
                         "Wrong backup was removed.") # not obsolete but still removed - ok
        self.assertEqual(EXISTING_BACKUPS_KEEPING_IDS[options[Options.NUMBER_OF_OLD_BACKUPS] + 1],
                         archiverMock.removeBackup.call_args_list[1][0][1], "Wrong obsolete backup was removed.")
        self.assertEqual(EXISTING_BACKUPS_KEEPING_IDS[options[Options.NUMBER_OF_OLD_BACKUPS] + 2],
                         archiverMock.removeBackup.call_args_list[2][0][1], "Wrong obsolete backup was removed.")

        # check that keep of the original backup is called as third call
        self.assertEqual(EXISTING_BACKUPS_KEEPING_IDS[0], archiverMock.keepBackup.call_args_list[2][0][1],
                         "Backup with wrong keeping ID was kept.")
        self.assertEqual("aa", archiverMock.keepBackup.call_args_list[2][0][2],
                         "Backup was kept under wrong keeping ID.")



    def test_makeBackupKeepOldBackupMaxNumberOfOldBackups(self):
        """Tests the maximum allowed number of old backups.

        Sets up the archiver service so that it returns more existing backups than allowed.  Configuration option
        for number of old backup to be kept also exceed the same limit.  Then creates a backup and asserts that
        last allowed backup ("zz") is removed."""

        def intToKeepingId(number):
            BASE = 26
            NUMERALS = [chr(nmr) for nmr in range(ord("a"), ord("z") + 1)]
            firstDigit = NUMERALS[number // BASE]
            secondDigit = NUMERALS[number % BASE]
            return firstDigit + secondDigit



        # setup service so that maximal number of old backups are kept
        EXISTING_BACKUPS_KEEPING_IDS = [None] + [intToKeepingId(keepingIdNumber) for keepingIdNumber in range(0, 676)]

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: len(EXISTING_BACKUPS_KEEPING_IDS) + 5
        }

        ArchivingTestUtils._createBackup(archiverMock, options)

        # check that removal of only the last allowed backup is called
        self.assertEqual(1, archiverMock.removeBackup.call_count, "None or more than one backup was removed.")
        self.assertEqual("zz", archiverMock.removeBackup.call_args[0][1],
                         "The last allowed kept backup was not removed.")



    def test_makeBackupKeepOldBackupZeroOldBackups(self):
        """Tests the backup keeping when zero old backups is configured.

        Sets up the archiver service so that it returns some existing backups.  Configuration option for number of
        old backup to be kept is set to 0.  Then creates a backup and asserts that no backup was removed nor
        kept."""

        # setup service so that some old backups are kept
        EXISTING_BACKUPS_KEEPING_IDS = self.__KEEPING_IDS[:3]

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: 0
        }

        ArchivingTestUtils._createBackup(archiverMock, options)

        # check that no backup is removed nor kept
        self.assertFalse(archiverMock.removeBackup.called, "Some backups were removed.")
        self.assertFalse(archiverMock.keepBackup.called, "Some backups were kept.")



    def test_makeBackupKeepOldBackupRemoveObsoleteWithKeepingIdHoles(self):
        """Tests the backup keeping for removal of obsolete backups with non continuous kept backups.

        Sets up the archiver service so that it returns several kept backups with some missing ones.  Configuration
        option for number of old backup to be kept is set to 6.  Then creates a backup and asserts that no backups are
        removed."""

        # setup service so that defined backups are kept
        EXISTING_BACKUPS_KEEPING_IDS = self.__KEEPING_IDS[:3] + self.__KEEPING_IDS[5:9]

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: 6
        }

        ArchivingTestUtils._createBackup(archiverMock, options)

        self.assertFalse(archiverMock.removeBackup.called, "Some backups were removed.")

    # }}} makeBackup() tests for old backup keeping



    # {{{ helpers for makeBackup() tests for old backup keeping

    @staticmethod
    def __createAndSetupArchiverMock(existingBackupsKeepingIds):
        archiverMock = ArchiverTestUtils.createArchiverMock()
        archiverMock.doesBackupExist.side_effect = lambda bd, level = None, keepingId = None: \
            keepingId in existingBackupsKeepingIds
        return archiverMock



    def __assertKeptBackup(self, archiverMock, keepingId, newKeepingId, msg = None):
        keptCalledCorrectly = False
        for keepBackupArgs in archiverMock.keepBackup.call_args_list:
            keepBackupPositionalArgs = keepBackupArgs[0]

            if keepBackupPositionalArgs[1] == keepingId and \
                            keepBackupPositionalArgs[2] == newKeepingId:
                keptCalledCorrectly = True
                break

        self.assertTrue(keptCalledCorrectly, msg or str.format(
            "Backup was not kept correctly: keepingId {}, newKeepingId {}.",
            keepingId, newKeepingId))

    # }}} helpers for makeBackup() tests for old backup keeping

# }}} CLASSES
