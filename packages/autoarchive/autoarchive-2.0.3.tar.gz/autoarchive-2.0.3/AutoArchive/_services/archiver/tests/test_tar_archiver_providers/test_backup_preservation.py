# test_backup_preservation.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2016 Róbert Čerňanský



""":class:`TestInternalTarBackupPreservation`, :class:`TestExternalTarBackupPreservation`."""



__all__ = ["TestInternalTarBackupPreservation", "TestExternalTarBackupPreservation"]



# {{{ INCLUDES

import unittest

import os
from abc import abstractmethod

from AutoArchive._services.archiver import BackupTypes
from AutoArchive._services.archiver._external_tar_archiver_provider import _ExternalTarArchiverProvider
from AutoArchive._services.archiver._internal_tar_archiver_provider import _InternalTarArchiverProvider
from AutoArchive._services.archiver._tar_archiver_provider_base import _BACKUP_TYPES_TO_EXTENSIONS
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from AutoArchive._services.archiver.tests.archiver_test_utils import _BackupDefinitionBuilder
from AutoArchive.tests import ComponentTestUtils

# }}} INCLUDES



# {{{ CLASSES

class _TestBackupPreservation(unittest.TestCase):
    """Base class for tests of tar archiver providers for backup preservation."""

    @classmethod
    def setUpClass(cls):
        ArchiverTestUtils._setUpClassArchiverComponent()



    @classmethod
    def tearDownClass(cls):
        ArchiverTestUtils._tearDownClassArchiverComponent()



    def setUp(self):
        self.archiverProvider_ = self.createTestSubject_()
        self.testFileStructurePath_ = ArchiverTestUtils._makeTestFileStructure()



    def tearDown(self):
        ArchiverTestUtils._removeTestFileStructure(self.testFileStructurePath_)



    @abstractmethod
    def createTestSubject_(self):
        """Creates an instance of tested archiver provider."""



    # {{{ doesBackupExist tests

    def test_doesBackupExist(self):
        """Tests basic case of backup existence.

        Creates a backup and asserts that it exists."""

        IRRELEVANT_BACKUP_TYPE = BackupTypes.TarGz

        backupDefinition = _BackupDefinitionBuilder()\
            .withBackupType(IRRELEVANT_BACKUP_TYPE)\
            .withRoot(self.testFileStructurePath_)\
            .withIncludeFiles(os.listdir(self.testFileStructurePath_))\
            .build()
        self.archiverProvider_.backupFiles(backupDefinition)

        # call the tested method
        result = self.archiverProvider_.doesBackupExist(backupDefinition)

        self.assertTrue(result, "The backup does not exist.")

    # }}} doesBackupExist tests



    # {{{ keepBackup tests

    def test_keepBackup(self):
        """Tests basic case of backup preservation.

        Creates a backup and preserves it under specified keep ID.  Asserts that the preserved backup exists and
        that the original backup does not exist."""

        TEST_KEEP_ID = "TEST_KEEP_ID"

        IRRELEVANT_BACKUP_TYPE = BackupTypes.TarBz2

        backupDefinition = _BackupDefinitionBuilder()\
            .withBackupType(IRRELEVANT_BACKUP_TYPE)\
            .withRoot(self.testFileStructurePath_)\
            .withIncludeFiles(os.listdir(self.testFileStructurePath_))\
            .build()
        backupFilePath = self.archiverProvider_.backupFiles(backupDefinition)

        # call the tested method
        self.archiverProvider_.keepBackup(backupDefinition, None, TEST_KEEP_ID)

        splitBackupFilePath = list(backupFilePath.partition(_BACKUP_TYPES_TO_EXTENSIONS[IRRELEVANT_BACKUP_TYPE]))
        splitBackupFilePath.insert(1, TEST_KEEP_ID + ".")
        keptBackupFilePath = str.join("", splitBackupFilePath)

        self.assertTrue(os.path.isfile(keptBackupFilePath), "The kept backup file does not exist.")
        self.assertFalse(os.path.exists(backupFilePath), "The original backup still exists.")

    # }}} keepBackup tests



class TestInternalTarBackupPreservation(_TestBackupPreservation):
    """Tests of internal tar archiver provider for backup preservation."""

    def createTestSubject_(self):
        return _InternalTarArchiverProvider(ComponentTestUtils.getComponentTestContext().workDir)



class TestExternalTarBackupPreservation(_TestBackupPreservation):
    """Tests of external tar archiver provider for backup preservation."""

    def createTestSubject_(self):
        return _ExternalTarArchiverProvider(ComponentTestUtils.getComponentTestContext().workDir)

# }}} CLASSES
