# test_content.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2016 Róbert Čerňanský



""":class:`TestInternalTarContent`, :class:`TestExternalTarContent`."""



__all__ = ["TestInternalTarContent", "TestExternalTarContent"]



# {{{ INCLUDES

import unittest
from mock import Mock

import os
from abc import abstractmethod

from AutoArchive._services.archiver import BackupSubOperations, BackupOperationErrors
from AutoArchive._services.archiver._external_tar_archiver_provider import _ExternalTarArchiverProvider
from AutoArchive._services.archiver._internal_tar_archiver_provider import _InternalTarArchiverProvider
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from AutoArchive._services.archiver.tests.archiver_test_utils import _BackupDefinitionBuilder
from AutoArchive.tests import ComponentTestUtils

# }}} INCLUDES



# {{{ CLASSES

class _TestContent(unittest.TestCase):
    """Base class for tests of tar archiver providers for archive content."""

    # Attention! Tests included in this class and derived classes has to fulfill following requirements:
    # - Create a test file structure and store the path to it to self.testFileStructurePath_ variable.
    # - Initialize the self.extractPath_ variable with a path to the extracted backup.



    @classmethod
    def setUpClass(cls):
        ArchiverTestUtils._setUpClassArchiverComponent()



    @classmethod
    def tearDownClass(cls):
        ArchiverTestUtils._tearDownClassArchiverComponent()



    def setUp(self):
        self.archiverProvider_ = None
        self.testFileStructurePath_ = None
        self.extractPath_ = None

        self.archiverProvider_ = self.createTestSubject_()



    def tearDown(self):
        ArchiverTestUtils._removeExtractedBackup(self.extractPath_)
        if os.path.isfile(ComponentTestUtils.irrelevantValidFilePath):
            os.remove(ComponentTestUtils.irrelevantValidFilePath)
        ArchiverTestUtils._removeTestFileStructure(self.testFileStructurePath_)



    @abstractmethod
    def createTestSubject_(self):
        """Creates an instance of tested archiver provider."""



    # {{{ backup creation tests for archive content

    def test_BackupCreationContent(self):
        """Tests the creation of a backup and its content.

        Creates a backup and extracts it.  Asserts that the backup content is identical to the archived file
        structure."""

        self.testFileStructurePath_ = ArchiverTestUtils._makeTestFileStructure()

        backupDefinition = _BackupDefinitionBuilder()\
            .withRoot(self.testFileStructurePath_)\
            .withIncludeFiles(os.listdir(self.testFileStructurePath_))\
            .build()
        backupFilePath = self.archiverProvider_.backupFiles(backupDefinition)

        self.extractPath_ = ArchiverTestUtils._extractBackup(backupFilePath)
        self.assertTrue(ArchiverTestUtils._compareDirs(self.testFileStructurePath_, self.extractPath_))



    def test_BackupCreationContentLinks(self):
        """Tests the creation of a backup and its content with file structure containing symlinks.

        Creates a backup and extracts it.  Asserts that the backup content is identical to the archived file
        structure."""

        self.testFileStructurePath_ = ArchiverTestUtils._makeTestFileStructure(links = True)

        backupDefinition = _BackupDefinitionBuilder()\
            .withRoot(self.testFileStructurePath_)\
            .withIncludeFiles(os.listdir(self.testFileStructurePath_))\
            .build()
        backupFilePath = self.archiverProvider_.backupFiles(backupDefinition)

        self.extractPath_ = ArchiverTestUtils._extractBackup(backupFilePath)
        self.assertTrue(ArchiverTestUtils._compareDirs(self.testFileStructurePath_, self.extractPath_))



    def test_BackupCreationContentExclude(self):
        """Tests the creation of a backup and its content with some file excluded.

        Creates a backup and extracts it.  Asserts that the backup content is identical to the archived file
        structure."""

        EXCLUDE_FILES = frozenset({str.format(ArchiverTestUtils._DIR_NAME, index = 1),
                                   os.path.join(str.format(ArchiverTestUtils._DIR_NAME, index = 0),
                                                str.format(ArchiverTestUtils._FILE_NAME, index = 0))})

        self.testFileStructurePath_ = ArchiverTestUtils._makeTestFileStructure()

        backupDefinition = _BackupDefinitionBuilder()\
            .withRoot(self.testFileStructurePath_)\
            .withIncludeFiles(os.listdir(self.testFileStructurePath_))\
            .withExcludeFiles(EXCLUDE_FILES)\
            .build()
        backupFilePath = self.archiverProvider_.backupFiles(backupDefinition)

        self.extractPath_ = ArchiverTestUtils._extractBackup(backupFilePath)

        # make a set of files that were archived but exclude the content of directories in EXCLUDE_FILES; beware that
        # the algorithm below works only for top-level directories in EXCLUDE_FILES
        originalFiles = set()
        for root, dirs, files in os.walk(self.testFileStructurePath_):
            relativeRoot = os.path.relpath(root, self.testFileStructurePath_)
            if ((os.path.dirname(relativeRoot) and os.path.dirname(relativeRoot) not in EXCLUDE_FILES) or
                not os.path.dirname(relativeRoot)):
                originalFiles.add(relativeRoot)
            if relativeRoot not in EXCLUDE_FILES and \
               ((os.path.dirname(relativeRoot) and os.path.dirname(relativeRoot) not in EXCLUDE_FILES) or
                not os.path.dirname(relativeRoot)):
                originalFiles.update({os.path.join(relativeRoot, f) for f in files})

        # make a set of files that the archive contains
        extractedFiles = set()
        for root, dirs, files in os.walk(self.extractPath_):
            relativeRoot = os.path.relpath(root, self.extractPath_)
            extractedFiles.add(relativeRoot)
            extractedFiles.update({os.path.join(relativeRoot, f) for f in files})

        excluded = originalFiles - extractedFiles
        self.assertEqual(EXCLUDE_FILES, excluded)



    def test_BackupCreationContentSocket(self):
        """Tests the creation of a backup and its content with file structure containing a socket.

        Creates a backup and extracts it.  Asserts that the backup content does not contains the socket."""

        self.testFileStructurePath_ = ArchiverTestUtils._makeTestFileStructure(socket = True)

        backupDefinition = _BackupDefinitionBuilder()\
            .withRoot(self.testFileStructurePath_)\
            .withIncludeFiles(os.listdir(self.testFileStructurePath_))\
            .build()
        backupFilePath = self.archiverProvider_.backupFiles(backupDefinition)

        # check that the backup does not contains the socket
        self.extractPath_ = ArchiverTestUtils._extractBackup(backupFilePath)
        sockets = set(os.listdir(self.testFileStructurePath_)) - set(os.listdir(self.extractPath_))
        self.assertEqual(sockets, {ArchiverTestUtils._SOCKET_NAME})



    def test_PermissionDeniedContent(self):
        """Tests the content of the backup with some unreadable filesystem objects.

        Creates a backup and extracts it.  Asserts that the backup content does not contains filesystem objects which
        were not readable."""

        self.testFileStructurePath_ = ArchiverTestUtils._makeTestFileStructure(denied = True, links = True)

        backupDefinition = _BackupDefinitionBuilder()\
            .withRoot(self.testFileStructurePath_)\
            .withIncludeFiles(os.listdir(self.testFileStructurePath_))\
            .build()
        backupFilePath = self.archiverProvider_.backupFiles(backupDefinition)

        # check that the backup does not contain the unreadable file and directory
        self.extractPath_ = ArchiverTestUtils._extractBackup(backupFilePath)
        denied = set(os.listdir(self.testFileStructurePath_)) - set(os.listdir(self.extractPath_))
        self.assertEqual(denied, {ArchiverTestUtils._DENIED_FILE_NAME, ArchiverTestUtils._DENIED_DIR_NAME})

    # }}} backup creation tests for archive content



    # {{{ backup creation tests for events propagation

    def test_PermissionDeniedPropagation(self):
        """Tests the propagation of permission denied error during backup creation.

        Creates a backup of file structure containing non-readable objects.  Asserts that during creation the
        corresponding event was fired for each unreadable object."""

        self.testFileStructurePath_ = ArchiverTestUtils._makeTestFileStructure(denied = True, links = True)
        onBackupOperationErrorMock = Mock()
        self.archiverProvider_.backupOperationError += onBackupOperationErrorMock

        backupDefinition = _BackupDefinitionBuilder()\
            .withRoot(self.testFileStructurePath_)\
            .withIncludeFiles(os.listdir(self.testFileStructurePath_))\
            .build()
        self.archiverProvider_.backupFiles(backupDefinition)

        self.assertEqual([((BackupSubOperations.Open, BackupOperationErrors.PermissionDenied,
                            ArchiverTestUtils._DENIED_DIR_NAME), {}),
                          ((BackupSubOperations.Open, BackupOperationErrors.PermissionDenied,
                            ArchiverTestUtils._DENIED_FILE_NAME), {})],
            onBackupOperationErrorMock.call_args_list)



    def test_BackupCreationSocketIgnoredPropagation(self):
        """Tests the propagation of socket ignored error during backup creation.

        Creates a backup of file structure containing a socket.  Asserts that during creation the corresponding event
        was fired for the socket."""

        self.testFileStructurePath_ = ArchiverTestUtils._makeTestFileStructure(socket = True)

        onBackupOperationErrorMock = Mock()
        self.archiverProvider_.backupOperationError += onBackupOperationErrorMock

        backupDefinition = _BackupDefinitionBuilder()\
            .withRoot(self.testFileStructurePath_)\
            .withIncludeFiles(os.listdir(self.testFileStructurePath_))\
            .build()
        self.archiverProvider_.backupFiles(backupDefinition)

        onBackupOperationErrorMock.assert_called_once_with(
            BackupSubOperations.Open, BackupOperationErrors.SocketIgnored, ArchiverTestUtils._SOCKET_NAME)



    def test_BackupCreationFileAddPropagation(self):
        """Tests the propagation of adding a filesystem object during backup creation.

        Creates a backup.  Asserts that the corresponding event was fired for each valid filesystem object."""

        self.testFileStructurePath_ = ArchiverTestUtils._makeTestFileStructure(
            socket = True, denied = True, links = True)

        onFileAddMock = Mock()
        self.archiverProvider_.fileAdd += onFileAddMock

        backupDefinition = _BackupDefinitionBuilder()\
            .withRoot(self.testFileStructurePath_)\
            .withIncludeFiles(os.listdir(self.testFileStructurePath_))\
            .build()
        self.archiverProvider_.backupFiles(backupDefinition)

        self.assertEqual(19, onFileAddMock.call_count)

    # }}} backup creation tests for events propagation



class TestInternalTarContent(_TestContent):
    """Tests of internal tar archiver provider for archive content."""

    def createTestSubject_(self):
        return _InternalTarArchiverProvider(ComponentTestUtils.getComponentTestContext().workDir)



class TestExternalTarContent(_TestContent):
    """Tests of external tar archiver provider for archive content."""

    def createTestSubject_(self):
        return _ExternalTarArchiverProvider(ComponentTestUtils.getComponentTestContext().workDir)

# }}} CLASSES
