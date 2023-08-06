# test_keep_old_incremental_backups.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2017 Róbert Čerňanský



""":class:`TestKeepOldIncrementalBackups`."""



__all__ = ["TestKeepOldIncrementalBackups"]



# {{{ INCLUDES

import unittest
import collections

from AutoArchive._infrastructure.configuration import Options
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from ...archiving_test_utils import ArchivingTestUtils

# }}} INCLUDES



# {{{ CLASSES

class TestKeepOldIncrementalBackups(unittest.TestCase):
    "Test of :meth:`._Archiving.makeBackup()` method for the keeping of old incremental backups."

    # standard keeping IDs enumeration
    __KEEPING_IDS = (None, "aa", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj")

    __KeepingIdIncrements = collections.namedtuple("KeepingIdIncrements", "keepingId, numberOfIncrements")



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



    # {{{ makeBackup() tests for old incremental backup keeping

    def test_makeBackupKeepOldIncrementalBackup(self):
        """Tests the basic use case of incremental backup keeping.

        Creates an incremental backup of level 1 and checks that the corresponding increments from the original one
        were kept and none was removed."""

        BACKUP_LEVEL = 1

        # setup service so that a single backup with three backup increments exists, none is kept
        EXISTING_BACKUPS_KEEPING_IDS = {0: (None,), 1: (None,), 2: (None,)}

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.LEVEL: BACKUP_LEVEL
        }

        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, maxBackupLevel = 999)

        self.assertEqual(2, archiverMock.keepBackup.call_count, "Wrong number of backup's increments was kept.")
        self.__assertKeptBackup(archiverMock, None, "aa", 1)
        self.__assertKeptBackup(archiverMock, None, "aa", 2)
        self.assertFalse(archiverMock.removeBackupIncrements.called, "Some backup increments were removed.")



    def test_makeBackupKeepOldIncrementalBackupRemoveOldest(self):
        """Tests the incremental backup keeping where oldest kept backups have to be removed.

        Sets up the archiver service so that it returns following existing backups (providing that backup ID is
        'test' and type tar which is irrelevant to the test):

          test.tar,    test.1.tar,    test.2.tar,
          test.aa.tar, test.1.aa.tar, test.2.aa.tar,
                       test.1.ab.tar, test.2.ab.tar,
                       test.1.ac.tar, test.2.ac.tar,
                       test.1.ad.tar, test.2.ad.tar

        Also sets configuration option for number of old backup to be kept to 2.  Then creates a backup of level 1 and
        checks that backup increments with keeping ID "ab" are removed starting from level 1.  Also checks that backup
        increments of level 1 and 2 with keeping ID "aa" are kept with keeping ID "ab".  Finally checks that
        original (not kept) backup increments of level 1 and 2 are kept with keeping ID "aa"."""

        OLD_BACKUPS = 2
        BACKUP_LEVEL = 1

        EXISTING_BACKUPS_KEEPING_IDS = {0: self.__KEEPING_IDS[:2],
                                        1: self.__KEEPING_IDS[:5],
                                        2: self.__KEEPING_IDS[:5]}

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: OLD_BACKUPS,
            Options.LEVEL: BACKUP_LEVEL
        }

        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, maxBackupLevel = 999)

        self.assertEqual(5, archiverMock.keepBackup.call_count, "Wrong number of backup's increments was kept.")
        self.__assertKeptBackup(archiverMock, None, "aa", 1)
        self.__assertKeptBackup(archiverMock, None, "aa", 2)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 0)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 1)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 2)
        self.assertEqual(1, archiverMock.removeBackupIncrements.call_count, "No or more than one backup was removed.")
        self.__assertRemovedIncrements(archiverMock, 1, "ab")



    def test_makeBackupKeepOldIncrementalBackupReplaceLevel0(self):
        """Tests the incremental backup keeping when replacing the level 0.

        Sets up the archiver service so that it returns single level 0 increment and no kept increment for that level.
        Also some kept increments.  Configuration option for number of old backup to be kept sets to 4.  Then creates
        a backup of level 0 and checks that backups were kept correctly and no increments were removed."""

        OLD_BACKUPS = 4
        BACKUP_LEVEL = 0

        # setup service so that defined number in each of three backup's increments exists
        EXISTING_BACKUPS_KEEPING_IDS = {0: self.__KEEPING_IDS[:1],
                                        1: self.__KEEPING_IDS[1:2],
                                        2: self.__KEEPING_IDS[1:3]}

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: OLD_BACKUPS,
            Options.LEVEL: BACKUP_LEVEL
        }

        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, maxBackupLevel = 999)

        self.assertEqual(4, archiverMock.keepBackup.call_count, "Wrong number of backup's increments was kept.")
        self.__assertKeptBackup(archiverMock, None, "aa", 0)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 1)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 2)
        self.__assertKeptBackup(archiverMock, "ab", "ac", 2)
        self.assertFalse(archiverMock.removeBackupIncrements.called, "Some backup increments were removed.")



    def test_makeBackupKeepOldIncrementalBackupNoReplaceLevel1(self):
        """Tests the incremental backup keeping when creating a level 1 backup not replacing any.

        Sets up the archiver service so that it returns single level 0 increment and no kept increment for that level.
        Also some kept increments, more than the set number of old backups.  Configuration option for number of old
        backup to be kept sets to 1.  Then creates a backup of level 1 and checks that no backups were kept and no
        increments were removed."""

        OLD_BACKUPS = 1
        BACKUP_LEVEL = 1

        EXISTING_BACKUPS_KEEPING_IDS = {0: self.__KEEPING_IDS[:1],
                                        1: self.__KEEPING_IDS[1:2],
                                        2: self.__KEEPING_IDS[1:3]}

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: OLD_BACKUPS,
            Options.LEVEL: BACKUP_LEVEL
        }

        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, maxBackupLevel = 999)

        self.assertFalse(archiverMock.removeBackupIncrements.called, "Some backup increments were removed.")
        self.assertFalse(archiverMock.keepBackup.called, "Some backup increments were kept.")



    def test_makeBackupKeepOldIncrementalBackupReplaceLevel0WithKeptLevel0(self):
        """Tests the incremental backup keeping when replacing the level 0 when kept level 0 exists.

        Sets up the archiver service so that it returns single level 0 increment and single kept increment for that
        level.  Also some kept increments.  Configuration option for number of old backup to be kept sets to 3.  Then
        creates a backup of level 0 and checks that backups were kept and removed correctly."""

        OLD_BACKUPS = 3
        BACKUP_LEVEL = 0

        EXISTING_BACKUPS_KEEPING_IDS = {0: self.__KEEPING_IDS[:2],
                                        1: self.__KEEPING_IDS[2:3],
                                        2: self.__KEEPING_IDS[2:4]}

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: OLD_BACKUPS,
            Options.LEVEL: BACKUP_LEVEL
        }

        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, maxBackupLevel = 999)

        self.assertEqual(4, archiverMock.keepBackup.call_count, "Wrong number of backup's increments was kept.")
        self.__assertKeptBackup(archiverMock, None, "aa", 0)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 0)
        self.__assertKeptBackup(archiverMock, "ab", "ac", 1)
        self.__assertKeptBackup(archiverMock, "ab", "ac", 2)
        self.assertEqual(1, archiverMock.removeBackupIncrements.call_count, "No or more than one backup was removed.")
        self.__assertRemovedIncrements(archiverMock, 2, "ac")



    def test_makeBackupKeepOldIncrementalBackupWithMissingKeptLevels(self):
        """Tests the incremental backup keeping where kept backup are missing in some levels.

        Sets up the archiver service so that it returns various number of existing increments for different backup
        levels while level 2 is missing some kept backup.  Also sets configuration option for number of old backup to
        be kept to 5.  Then creates a backup of level 1 and checks that backups were kept and removed
        correctly."""

        OLD_BACKUPS = 5
        BACKUP_LEVEL = 1

        EXISTING_BACKUPS_KEEPING_IDS = {0: self.__KEEPING_IDS[:3],
                                        1: self.__KEEPING_IDS[:5],
                                        2: self.__KEEPING_IDS[:2],
                                        3: self.__KEEPING_IDS[:6]}

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: OLD_BACKUPS,
            Options.LEVEL: BACKUP_LEVEL
        }

        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, maxBackupLevel = 999)

        self.assertEqual(11, archiverMock.keepBackup.call_count, "Wrong number of backup's increments was kept.")
        self.__assertKeptBackup(archiverMock, None, "aa", 1)
        self.__assertKeptBackup(archiverMock, None, "aa", 2)
        self.__assertKeptBackup(archiverMock, None, "aa", 3)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 0)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 1)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 2)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 3) # SMELL: FileExists exception would have been thrown here
        self.__assertKeptBackup(archiverMock, "ab", "ac", 0)
        self.__assertKeptBackup(archiverMock, "ab", "ac", 1)
        self.__assertKeptBackup(archiverMock, "ac", "ad", 1)
        self.__assertKeptBackup(archiverMock, "ad", "ae", 1)
        self.assertEqual(1, archiverMock.removeBackupIncrements.call_count, "No or more than one backup was removed.")
        self.__assertRemovedIncrements(archiverMock, 3, "ae")



    def test_makeBackupKeepOldIncrementalBackupWithKeepingIdHoles(self):
        """Tests the incremental backup keeping where kept backup are not continuous.

        Sets up the archiver service so that it returns various number of existing increments for different backup
        levels while some of them does not contains continuous sequence.  Also sets configuration option for number of
        old backup to be kept to 5.  Then creates a backup of level 1 and checks that backups were kept and removed
        correctly."""

        OLD_BACKUPS = 5
        BACKUP_LEVEL = 1

        EXISTING_BACKUPS_KEEPING_IDS = {0: self.__KEEPING_IDS[:3],
                                        1: self.__KEEPING_IDS[:5],
                                        2: self.__KEEPING_IDS[:2] + (self.__KEEPING_IDS[4:9]),
                                        3: self.__KEEPING_IDS[:6]}

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: OLD_BACKUPS,
            Options.LEVEL: BACKUP_LEVEL
        }

        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, maxBackupLevel = 999)

        self.assertEqual(13, archiverMock.keepBackup.call_count, "Wrong number of backup's increments was kept.")
        self.__assertKeptBackup(archiverMock, None, "aa", 1)
        self.__assertKeptBackup(archiverMock, None, "aa", 2)
        self.__assertKeptBackup(archiverMock, None, "aa", 3)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 0)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 1)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 2)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 3) # SMELL: FileExists exception would have been thrown here
        self.__assertKeptBackup(archiverMock, "ab", "ac", 0)
        self.__assertKeptBackup(archiverMock, "ab", "ac", 1)
        self.__assertKeptBackup(archiverMock, "ac", "ad", 1)
        self.__assertKeptBackup(archiverMock, "ad", "ae", 1)
        self.__assertKeptBackup(archiverMock, "ad", "ae", 2)
        self.__assertKeptBackup(archiverMock, "ad", "ae", 3)
        self.assertEqual(1, archiverMock.removeBackupIncrements.call_count, "No or more than one backup was removed.")
        self.__assertRemovedIncrements(archiverMock, 2, "ae")



    def test_makeBackupKeepOldIncrementalBackupWithLevelHoles(self):
        """Tests the incremental backup keeping where backup levels are not continuous.

        Sets up the archiver service so that it returns various number of existing increments for different backup
        levels while level 2 is missing.  Also sets configuration option for number of old backup to be kept to 3.
        Then creates a backup of level 1 and checks that backups were kept and removed correctly."""

        OLD_BACKUPS = 3
        BACKUP_LEVEL = 1

        EXISTING_BACKUPS_KEEPING_IDS = {0: self.__KEEPING_IDS[:3],
                                        1: self.__KEEPING_IDS[:5],
                                        3: self.__KEEPING_IDS[:5]}

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: OLD_BACKUPS,
            Options.LEVEL: BACKUP_LEVEL
        }

        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, maxBackupLevel = 999)

        self.assertEqual(5, archiverMock.keepBackup.call_count, "Wrong number of backup's increments was kept.")
        self.__assertKeptBackup(archiverMock, None, "aa", 1)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 0)
        self.__assertKeptBackup(archiverMock, "aa", "ab", 1)
        self.__assertKeptBackup(archiverMock, "ab", "ac", 0)
        self.__assertKeptBackup(archiverMock, "ab", "ac", 1)
        self.assertEqual(1, archiverMock.removeBackupIncrements.call_count, "No or more than one backup was removed.")
        self.__assertRemovedIncrements(archiverMock, 1, "ac")



    def test_makeBackupKeepOldIncrementalBackupRemoveObsolete(self):
        """Tests the incremental backup keeping where obsolete kept backups have to be removed.

        Sets up the archiver service so that it returns various number of existing increments for different backup
        levels.  Also sets configuration option for number of old backup to be kept to 2.  Then creates a backup
        of level 1 and checks that correct number of obsolete backup increments were removed.  Also checks that
        correct backup increments were removed (as for the starting backup level and keeping ID)."""

        OLD_BACKUPS = 3

        EXISTING_BACKUPS_KEEPING_IDS = {0: self.__KEEPING_IDS[:2],
                                        1: self.__KEEPING_IDS[:4],
                                        2: self.__KEEPING_IDS[:5]}

        ANY_EXISTING_BACKUP_LEVEL = 1

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.REMOVE_OBSOLETE_BACKUPS: True,
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: OLD_BACKUPS,
            Options.LEVEL: ANY_EXISTING_BACKUP_LEVEL
        }

        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, maxBackupLevel = 999)

        self.assertEqual(1, archiverMock.removeBackupIncrements.call_count - 2,
                         "Wrong number of obsolete kept backups were removed.")
        self.__assertRemovedIncrements(archiverMock, 2, "ad")



    def test_makeBackupKeepOldIncrementalBackupZeroOldBackups(self):
        """Tests the incremental backup keeping when zero old backups is configured.

        Sets up the archiver service so that it returns some existing backups.  Configuration option for number of
        old backup to be kept is set to 0.  Then creates a backup and asserts that no backup was removed nor
        kept."""

        OLD_BACKUPS = 0
        BACKUP_LEVEL = 1

        EXISTING_BACKUPS_KEEPING_IDS = {0: self.__KEEPING_IDS[:2],
                                        1: self.__KEEPING_IDS[:3],
                                        2: self.__KEEPING_IDS[:3]}

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: OLD_BACKUPS,
            Options.LEVEL: BACKUP_LEVEL
        }

        ArchivingTestUtils._createBackup(archiverMock, options)

        # check that no backup is removed nor kept
        self.assertFalse(archiverMock.removeBackupIncrements.called, "Some backups were removed.")
        self.assertFalse(archiverMock.keepBackup.called, "Some backups were kept.")



    def test_makeBackupKeepOldIncrementalBackupRemoveObsoleteWithKeepingIdHoles(self):
        """Tests the incremental backup keeping for removal where kept backup are not continuous.

        Sets up the archiver service so that it returns various number of existing increments for different backup
        levels while some of them does not contains continuous sequence.  Also sets configuration option for number of
        old backup to be kept to 4.  Then creates a backup of level 1 and checks that correct number of obsolete backup
        increments were removed.  Also checks that correct backup increments were removed."""

        OLD_BACKUPS = 4

        EXISTING_BACKUPS_KEEPING_IDS = {0: self.__KEEPING_IDS[:1],
                                        1: self.__KEEPING_IDS[:6] + (self.__KEEPING_IDS[8:11]),
                                        2: self.__KEEPING_IDS[:10]}

        ANY_EXISTING_BACKUP_LEVEL = 2

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.REMOVE_OBSOLETE_BACKUPS: True,
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: OLD_BACKUPS,
            Options.LEVEL: ANY_EXISTING_BACKUP_LEVEL
        }

        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, maxBackupLevel = 999)

        self.assertEqual(6, archiverMock.removeBackupIncrements.call_count - 2,
                         "Wrong number of obsolete kept backups were removed.")
        self.__assertRemovedIncrements(archiverMock, 1, "ae")
        self.__assertRemovedIncrements(archiverMock, 2, "af")
        self.__assertRemovedIncrements(archiverMock, 2, "ag")
        self.__assertRemovedIncrements(archiverMock, 1, "ah")
        self.__assertRemovedIncrements(archiverMock, 1, "ai")
        self.__assertRemovedIncrements(archiverMock, 1, "aj")



    def test_makeBackupKeepOldIncrementalBackupRemoveObsoleteWithMissingKeptLevels(self):
        """Tests the incremental backup keeping for removal where kept backup are missing in some levels.

        Sets up the archiver service so that it returns various number of existing increments for different backup
        levels while level 2 is missing some kept backup.  Also sets configuration option for number of old backup to
        be kept to 5.  Then creates a backup of level 1 and checks that correct backup increments were removed."""

        OLD_BACKUPS = 5

        EXISTING_BACKUPS_KEEPING_IDS = {0: self.__KEEPING_IDS[:3],
                                        1: self.__KEEPING_IDS[:5],
                                        2: self.__KEEPING_IDS[:2],
                                        3: self.__KEEPING_IDS[:7]}

        ANY_EXISTING_BACKUP_LEVEL = 3

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.REMOVE_OBSOLETE_BACKUPS: True,
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: OLD_BACKUPS,
            Options.LEVEL: ANY_EXISTING_BACKUP_LEVEL
        }

        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, maxBackupLevel = 999)

        # SMELL: Even though level 3 "ac"+ backups are obsolete (or better say "rogue") because no level 2 "ac"
        # exists, they are not removed.
        self.assertEqual(1, archiverMock.removeBackupIncrements.call_count - 2,
                         "Wrong number of obsolete kept backups were removed.")
        self.__assertRemovedIncrements(archiverMock, 3, "ae")



    def test_makeBackupKeepOldIncrementalBackupRemoveObsoleteWithLevelHoles(self):
        """Tests the incremental backup keeping for removal where backup levels are not continuous.

        Sets up the archiver service so that it returns various number of existing increments for different backup
        levels while level 2 is missing.  Also sets configuration option for number of old backup to be kept to 3.
        Then creates a backup of level 1 and checks that correct backup increments were removed."""

        OLD_BACKUPS = 3
        BACKUP_LEVEL = 1

        EXISTING_BACKUPS_KEEPING_IDS = {0: self.__KEEPING_IDS[:3],
                                        1: self.__KEEPING_IDS[:5],
                                        3: self.__KEEPING_IDS[:5]}

        archiverMock = self.__createAndSetupArchiverMock(EXISTING_BACKUPS_KEEPING_IDS)

        options = {
            Options.REMOVE_OBSOLETE_BACKUPS: True,
            Options.KEEP_OLD_BACKUPS: True,
            Options.NUMBER_OF_OLD_BACKUPS: OLD_BACKUPS,
            Options.LEVEL: BACKUP_LEVEL
        }

        ArchivingTestUtils._createIncrementalBackup(archiverMock, options, maxBackupLevel = 999)

        self.assertEqual(1, archiverMock.removeBackupIncrements.call_count - 2,
                         "Wrong number of obsolete kept backups were removed.")
        self.__assertRemovedIncrements(archiverMock, 1, "ad")

    # }}} makeBackup() tests for old incremental backup keeping



    # {{{ helpers for makeBackup() tests for old incremental backup keeping

    @staticmethod
    def __createAndSetupArchiverMock(existingBackupsKeepingIds):
        archiverMock = ArchiverTestUtils.createArchiverMock()
        archiverMock.doesBackupExist.side_effect = lambda bd, level = 0, keepingId = None: \
            keepingId in existingBackupsKeepingIds[level] if level in existingBackupsKeepingIds else False
        archiverMock.doesAnyBackupLevelExist.side_effect = lambda bd, fromLevel, keepingId = None: \
            True in (keepingId in existingBackupsKeepingIds[lvl] \
                     for lvl in existingBackupsKeepingIds if lvl >= fromLevel)
        return archiverMock



    def __assertRemovedIncrements(self, archiverMock, fromLevel, keepingId = None, msg = None):
        removedIncrementsCorrectly = False
        for removeBackupIncrementsArgs in archiverMock.removeBackupIncrements.call_args_list:
            removeBackupIncrementsPositionalArgs = removeBackupIncrementsArgs[0]

            thirdArgumentSpecified = len(removeBackupIncrementsPositionalArgs) > 2
            if (not thirdArgumentSpecified and
                    (removeBackupIncrementsPositionalArgs[1] == fromLevel and keepingId is None)) or \
                    (thirdArgumentSpecified and
                         (removeBackupIncrementsPositionalArgs[1] == fromLevel and
                                  removeBackupIncrementsPositionalArgs[2] == keepingId)):
                removedIncrementsCorrectly = True
                break

        self.assertTrue(removedIncrementsCorrectly, msg or str.format(
            "Backup was not removed correctly: fromLevel {}, keepingId {}.", fromLevel, keepingId))



    def __assertKeptBackup(self, archiverMock, keepingId, newKeepingId, level, msg = None):
        keptCalledCorrectly = False
        for keepBackupArgs in archiverMock.keepBackup.call_args_list:
            keepBackupPositionalArgs = keepBackupArgs[0]

            if keepBackupPositionalArgs[1] == keepingId and \
                            keepBackupPositionalArgs[2] == newKeepingId and \
                            keepBackupPositionalArgs[3] == level:
                keptCalledCorrectly = True
                break

        self.assertTrue(keptCalledCorrectly, msg or str.format(
            "Backup was not kept correctly: keepingId {}, newKeepingId {}, level {}.",
            keepingId, newKeepingId, level))

    # }}} helpers for makeBackup() tests for old incremental backup keeping

# }}} CLASSES
