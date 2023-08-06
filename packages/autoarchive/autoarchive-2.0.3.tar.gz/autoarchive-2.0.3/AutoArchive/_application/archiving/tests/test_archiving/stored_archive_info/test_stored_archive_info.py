# test_stored_archive_info.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2016 Róbert Čerňanský



""":class:`TestStoredArchiveInfo`."""



__all__ = ["TestStoredArchiveInfo"]



# {{{ INCLUDES

import unittest

import mock

from AutoArchive._infrastructure.configuration import Options
from AutoArchive._services.archiver import ArchiverFeatures
from AutoArchive._services.archiver._tar_archiver_provider_base import _TarArchiverProviderBase
from AutoArchive._application.archiving._command_executor import _CommandExecutor
from AutoArchive._application.archiving._archiving import _Archiving
from AutoArchive._ui.cmdline._cmdline_ui import CmdlineUi
from AutoArchive.tests import ComponentTestUtils
from AutoArchive._infrastructure.configuration.tests import ConfigurationTestUtils
from ...archiving_test_utils import ArchivingTestUtils

# }}} INCLUDES



# {{{ CLASSES

class TestStoredArchiveInfo(unittest.TestCase):
    "Test of :meth:`.IArchiving.getStoredArchiveInfo()` method."



    @classmethod
    def setUpClass(cls):
        ArchivingTestUtils._setUpClassArchivingComponent()



    @classmethod
    def tearDownClass(cls):
        ArchivingTestUtils._tearDownClassArchivingComponent()



    def setUp(self):
        self.__serviceAccessorMock = None
        self.__archiveSpecFilePath = None
        self.__archiving = None

        ArchivingTestUtils._setUpArchivingComponent()

        options = {
            Options.USER_CONFIG_DIR: ComponentTestUtils.getComponentTestContext().userConfigDir,
            Options.INCREMENTAL: True
        }
        configurationMock = ConfigurationTestUtils.createConfigurationMock(options)

        applicationContextMock = ArchivingTestUtils._setUpApplicationContextMock(configurationMock = configurationMock)
        self.__serviceAccessorMock = ArchivingTestUtils._setUpServiceAccessorMock()
        self.__archiving = _Archiving(mock.Mock(spec_set = CmdlineUi), applicationContextMock,
                                      self.__serviceAccessorMock, mock.Mock(spec_set = _CommandExecutor))



    def tearDown(self):
        ArchivingTestUtils._tearDownArchivingComponent()



    def test_getStoredArchiveInfo(self):
        """Tests the :meth:`IArchiving.getStoredArchiveInfo()` method.

        Sets up Archiver service mocks to return predefined values.  Calls the tested method and checks that
        :class:`_ArchiveInfo` instance is created; then checks a few basic properties that they have expected values."""

        TEST_STORED_BACKUP = "test stored backup"
        IRRELEVANT_BACKUP_LEVEL = 5

        # set up archiver service mocks
        archiverMock = mock.Mock(spec_set = _TarArchiverProviderBase)
        archiverMock.getMaxBackupLevel.return_value = IRRELEVANT_BACKUP_LEVEL
        archiverMock.getStoredBackupIds.return_value = {TEST_STORED_BACKUP}
        ArchivingTestUtils._setUpArchiverServices(self.__serviceAccessorMock, archiverMock,
                                                  supportedFeatures = frozenset({ArchiverFeatures.Incremental}))

        # call the tested method
        archiveInfo = self.__archiving.getStoredArchiveInfo(TEST_STORED_BACKUP)

        self.assertIsNotNone(archiveInfo)
        self.assertEqual(archiveInfo.name, TEST_STORED_BACKUP)
        self.assertTrue(archiveInfo.incremental)

        # path shall be ``None`` in case of stored info (and not ``None`` in case of configured info)
        self.assertIsNone(archiveInfo.path)



    def test_getStoredArchiveNames(self):
        """Tests the :meth:`IArchiving.getStoredArchiveNames()` method.

        Sets up archiver's service method for returning stored backup IDs to a predefined value.  Calls the tested
        method and checks that the same stored archive names as the predefined ones were returned."""

        TEST_STORED_BACKUPS = {"test stored backup 1", "test stored backup 2"}

        # set up archiver service mocks
        archiverMock = mock.Mock(spec_set = _TarArchiverProviderBase)
        archiverMock.getStoredBackupIds.return_value = TEST_STORED_BACKUPS
        ArchivingTestUtils._setUpArchiverServices(self.__serviceAccessorMock, archiverMock)

        # call the tested method
        archiveNames = self.__archiving.getStoredArchiveNames()

        self.assertCountEqual(TEST_STORED_BACKUPS, set(archiveNames))



    def test_purgeStoredArchiveData(self):
        """Tests the :meth:`IArchiving.purgeStoredArchiveData()` method.

        Sets up archiver's service method for returning stored backup IDs to a predefined value.  Calls the tested
        method to remove a particular backup.  Checks that the service method was called with an argument equal to
        the backup name that was requested for purge."""

        TEST_STORED_BACKUP_2 = "test stored backup 2"
        TEST_STORED_BACKUPS = ("test stored backup 1", TEST_STORED_BACKUP_2)

        # set up archiver service mocks
        archiverMock = mock.Mock(spec_set = _TarArchiverProviderBase)
        archiverMock.getStoredBackupIds.return_value = TEST_STORED_BACKUPS
        ArchivingTestUtils._setUpArchiverServices(self.__serviceAccessorMock, archiverMock)

        # call the tested method
        self.__archiving.purgeStoredArchiveData(TEST_STORED_BACKUP_2)

        archiverMock.purgeStoredBackupData.assert_called_with(TEST_STORED_BACKUP_2)

# }}} CLASSES
