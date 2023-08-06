# test_archive_types.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2021 Róbert Čerňanský



""":class:`TestArchiveTypes`."""



__all__ = ["TestArchiveTypes"]



# {{{ INCLUDES

import unittest

from AutoArchive._infrastructure.configuration import ArchiverTypes
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from ...archiving_test_utils import ArchivingTestUtils

# }}} INCLUDES



# {{{ CLASSES

class TestArchiveTypes(unittest.TestCase):
    """Test of :meth:`._Archiving.makeBackup()` method for SPI usage for all supported archiver types."""

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



    # {{{ makeBackup() tests for archive types

    def test_makeBackupTar(self):
        "Tests the makeBackup() method with Tar archive type."

        self.__testMakeBackup(ArchiverTypes.Tar)



    def test_makeBackupTarGz(self):
        "Tests the makeBackup() method with TarGz archive type."

        self.__testMakeBackup(ArchiverTypes.TarGz)



    def test_makeBackupTarBz2(self):
        "Tests the makeBackup() method with TarBz2 archive type."

        self.__testMakeBackup(ArchiverTypes.TarBz2)



    def test_makeBackupTarXz(self):
        "Tests the makeBackup() method with TarXz archive type."

        self.__testMakeBackup(ArchiverTypes.TarXz)



    def test_makeBackupTarZst(self):
        "Tests the makeBackup() method with TarZst archive type."

        self.__testMakeBackup(ArchiverTypes.TarZst)



    def test_makeBackupTarInternal(self):
        "Tests the makeBackup() method with TarInternal archive type."

        self.__testMakeBackup(ArchiverTypes.TarInternal)



    def test_makeBackupTarGzInternal(self):
        "Tests the makeBackup() method with TarGzInternal archive type."

        self.__testMakeBackup(ArchiverTypes.TarGzInternal)



    def test_makeBackupTarBz2Internal(self):
        "Tests the makeBackup() method with TarBz2Internal archive type."

        self.__testMakeBackup(ArchiverTypes.TarBz2Internal)

    # }}} makeBackup() tests for archive types



    # {{{ helpers for makeBackup() tests for archiver type

    def __testMakeBackup(self, archiver):
        """Tests the makeBackup() method with specified archive type."""

        archiverMock = ArchiverTestUtils.createArchiverMock()

        ArchivingTestUtils._createBackup(archiverMock, archiverType = archiver)

        self.assertTrue(archiverMock.backupFiles.called)
        self.assertEqual(ArchivingTestUtils._ARCHIVER_TYPE_TO_BACKUP_TYPE_MAP[archiver],
                         archiverMock.backupFiles.call_args[0][0].backupType)

    # }}} helpers for makeBackup() tests for archiver type

# }}} CLASSES
