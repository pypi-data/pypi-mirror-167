# test_backup_types.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2021 Róbert Čerňanský



""":class:`TestInternalTarBackupTypes`, :class:`TestExternalTarBackupTypes`."""



__all__ = ["TestInternalTarBackupTypes", "TestExternalTarBackupTypes"]



# {{{ INCLUDES

import unittest

import os
from abc import abstractmethod

from AutoArchive._services.archiver import BackupTypes
from AutoArchive._services.archiver._external_tar_archiver_provider import _ExternalTarArchiverProvider
from AutoArchive._services.archiver._internal_tar_archiver_provider import _InternalTarArchiverProvider
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from AutoArchive._services.archiver.tests.archiver_test_utils import _BackupDefinitionBuilder
from AutoArchive.tests import ComponentTestUtils

# }}} INCLUDES



# {{{ CLASSES

class _TestBackupTypes(unittest.TestCase):
    """Base class for tests of tar archiver providers for different archive types."""

    @classmethod
    def setUpClass(cls):
        ArchiverTestUtils._setUpClassArchiverComponent()



    @classmethod
    def tearDownClass(cls):
        ArchiverTestUtils._tearDownClassArchiverComponent()



    def setUp(self):
        self.archiverProvider_ = None
        self.testFileStructurePath_ = None

        self.archiverProvider_ = self.createTestSubject_()
        self.testFileStructurePath_ = ArchiverTestUtils._makeTestFileStructure()



    def tearDown(self):
        ArchiverTestUtils._removeTestFileStructure(self.testFileStructurePath_)



    @abstractmethod
    def createTestSubject_(self):
        """Creates an instance of tested archiver provider."""



    # {{{ supported backup types and features tests

    def test_SupportedBackupTypes(self):
        """Tests the supportedBackupTypes property.

        Asserts that the tested archiver service provider supports at least one backup type."""

        self.assertGreater(len(self.archiverProvider_.supportedBackupTypes), 0)



    def test_getSupportedFeatures(self):
        """Tests the getSupportedFeatures() method.

        Asserts that the tested archiver service provider does not return ``None`` as the iterable of features."""

        self.assertIsNotNone(self.archiverProvider_.getSupportedFeatures())



    def test_getSupportedFeaturesForBackupType(self):
        """Tests the getSupportedFeatures() method for all supported backup types.

        Gets all supported features then asserts that for each supported backup type, supported features for the given
        type is a subset of all supported features."""

        allSupportedFeatures = self.archiverProvider_.getSupportedFeatures()
        for backupType in self.archiverProvider_.supportedBackupTypes:
            self.assertTrue(self.archiverProvider_.getSupportedFeatures(backupType) <= allSupportedFeatures)

    # }}} supported backup types and features tests



    # {{{ backup creation tests for backup types

    def test_BackupCreationOfTypeTar(self):
        """Tests the creation of "tar" backup."""

        self.createAndCheckBackupType_(BackupTypes.Tar, b"ustar\x00", 257)



    def test_BackupCreationOfTypeTarGz(self):
        """Tests the creation of "tar.gz" backup."""

        self.createAndCheckBackupType_(BackupTypes.TarGz, b"\x1f\x8b")



    def test_BackupCreationOfTypeTarBz2(self):
        """Tests the creation of "tar.bz2" backup."""

        self.createAndCheckBackupType_(BackupTypes.TarBz2, b"BZh")



    def createAndCheckBackupType_(self, backupType, magicBytes, magicOffset = 0):
        """Tests the creation of a backup of passed type.

        Creates the backup of specified type and asserts that the corresponding backup file exists and the magic bytes
        matches."""

        backupDefinition = _BackupDefinitionBuilder()\
            .withBackupType(backupType)\
            .withRoot(self.testFileStructurePath_)\
            .withIncludeFiles(os.listdir(self.testFileStructurePath_))\
            .build()
        backupFilePath = self.archiverProvider_.backupFiles(backupDefinition)

        self.assertTrue(os.path.isfile(backupFilePath), "The backup file does not exists.")
        with open(backupFilePath ,"rb") as archiveStream:
            readMagicBytes = \
                archiveStream.read(magicOffset + len(magicBytes))[magicOffset:(magicOffset + len(magicBytes))]
            self.assertEqual(magicBytes, readMagicBytes, str.format("The created backup is not of type \"{}\".",
                                                                    str(backupType)))

    # }}} backup creation tests for backup types



class TestInternalTarBackupTypes(_TestBackupTypes):
    """Tests of internal tar archiver provider for different archive types."""

    def createTestSubject_(self):
        return _InternalTarArchiverProvider(ComponentTestUtils.getComponentTestContext().workDir)



class TestExternalTarBackupTypes(_TestBackupTypes):
    """Tests of external tar archiver provider for different archive types."""

    def createTestSubject_(self):
        return _ExternalTarArchiverProvider(ComponentTestUtils.getComponentTestContext().workDir)



    # {{{ backup creation tests for backup types

    def test_BackupCreationOfTypeTarXz(self):
        """Tests the creation of "tar.xz" backup."""

        self.createAndCheckBackupType_(BackupTypes.TarXz, b"\xFD7zXZ\x00")



    def test_BackupCreationOfTypeTarZst(self):
        """Tests the creation of "tar.xz" backup."""

        self.createAndCheckBackupType_(BackupTypes.TarZst, b"(\xB5/\xFD")

    # }}} backup creation tests for backup types



    # {{{ backup creation tests for compression level

    def test_BackupCreationCompressionStrengthTarGz(self):
        """Tests the effect of compression strength for "tar.gz" backup type."""

        self.__testCompressionStrength(BackupTypes.TarGz)



    def test_BackupCreationCompressionStrengthTarBz2(self):
        """Tests the effect of compression strength for "tar.bz2" backup type."""

        # create significantly big test file structure
        ArchiverTestUtils._removeTestFileStructure(self.testFileStructurePath_)
        self.testFileStructurePath_ = ArchiverTestUtils._makeTestFileStructure(200)

        self.__testCompressionStrength(BackupTypes.TarBz2)



    def test_BackupCreationCompressionStrengthTarXz(self):
        """Tests the effect of compression strength for "tar.xz" backup type."""

        self.__testCompressionStrength(BackupTypes.TarXz)



    def test_BackupCreationCompressionStrengthTarZst(self):
        """Tests the effect of compression strength for "tar.zst" backup type."""

        self.__testCompressionStrength(BackupTypes.TarZst)



    def __testCompressionStrength(self, backupType):
        """Tests the effect of compression strength for passed archive type.

        Creates a backup with lowest compression strength and then with highest.  Asserts tha the size of the backup
        with highest strength is smaller than the other."""

        backupDefinition = _BackupDefinitionBuilder()\
            .withBackupType(backupType)\
            .withRoot(self.testFileStructurePath_)\
            .withIncludeFiles(os.listdir(self.testFileStructurePath_))\
            .build()

        backupFilePath = self.archiverProvider_.backupFiles(backupDefinition, 0)
        sizeOfStrength0 = os.path.getsize(backupFilePath)
        backupFilePath = self.archiverProvider_.backupFiles(backupDefinition, 9)
        sizeOfStrength9 = os.path.getsize(backupFilePath)

        self.assertLess(sizeOfStrength9, sizeOfStrength0,
                        "The backup file created with stronger compression strength " +
                        "has not smaller size than the one created with weaker strength.")

    # }}} backup creation tests for compression level

# }}} CLASSES
