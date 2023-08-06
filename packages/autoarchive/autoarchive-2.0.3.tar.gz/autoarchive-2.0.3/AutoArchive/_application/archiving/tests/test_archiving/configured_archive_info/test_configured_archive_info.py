# test_configured_archive_info.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2017 Róbert Čerňanský



""":class:`TestConfiguredArchiveInfo`."""



__all__ = ["TestConfiguredArchiveInfo"]



# {{{ INCLUDES

import unittest
import os

import mock

from AutoArchive._infrastructure.configuration import Options, ArchiverTypes
from AutoArchive._services.archiver import ArchiverFeatures
from AutoArchive._services.archiver._tar_archiver_provider_base import _TarArchiverProviderBase
from AutoArchive._application.archiving.archive_spec import ConfigConstants
from AutoArchive._application.archiving._command_executor import _CommandExecutor
from AutoArchive._application.archiving._archiving import _Archiving
from AutoArchive._ui.cmdline._cmdline_ui import CmdlineUi
from AutoArchive.tests import ComponentTestUtils
from AutoArchive._infrastructure.configuration.tests import ConfigurationTestUtils
from AutoArchive._application.archiving.archive_spec.tests import ArchiveSpecTestUtils
from ...archiving_test_utils import ArchivingTestUtils

# }}} INCLUDES



# {{{ CLASSES

class TestConfiguredArchiveInfo(unittest.TestCase):
    "Test of methods for getting info about configured archives."

    __ARCHIVE_NAME = "test archive name"



    @classmethod
    def setUpClass(cls):
        ArchivingTestUtils._setUpClassArchivingComponent()



    @classmethod
    def tearDownClass(cls):
        ArchivingTestUtils._tearDownClassArchivingComponent()



    def setUp(self):
        self.__serviceAccessorMock = None
        self.__archiving = None

        ArchivingTestUtils._setUpArchivingComponent()
        options = {Options.USER_CONFIG_DIR: ComponentTestUtils.getComponentTestContext().userConfigDir,
                   Options.ARCHIVE_SPECS_DIR: ComponentTestUtils.getComponentTestContext().archiveSpecsDir}
        configurationMock = ConfigurationTestUtils.createConfigurationMock(options)

        applicationContextMock = ArchivingTestUtils._setUpApplicationContextMock(configurationMock = configurationMock)
        self.__serviceAccessorMock = ArchivingTestUtils._setUpServiceAccessorMock()
        self.__archiving = _Archiving(mock.Mock(spec_set = CmdlineUi), applicationContextMock,
                                      self.__serviceAccessorMock, mock.Mock(spec_set = _CommandExecutor))



    def tearDown(self):
        ArchivingTestUtils._tearDownArchivingComponent()



    def test_getArchiveSpecs(self):
        """Tests the :meth:`_Archiving.getArchiveSpecs()` method.

        Creates some archive specification files and some other files in the archive specification directory.  Verifies
        that the returned sequence contains all the archive specification files and no other files."""

        def getSpecFilePath(fileName):
            return os.path.join(ComponentTestUtils.getComponentTestContext().archiveSpecsDir, fileName)



        specFiles = {"TEST_SPEC1" + ConfigConstants.ARCHIVE_SPEC_EXT,
                     "TEST_SPEC2" + ConfigConstants.ARCHIVE_SPEC_EXT}
        allFiles = specFiles | {"TEST_FILE1.test", "TEST_FILE2"}

        # create files in the archive specification directory
        for fileName in allFiles:
            os.mknod(getSpecFilePath(fileName))

        # test that archive specification files are returned
        self.assertCountEqual((f.path for f in self.__archiving.getArchiveSpecs()),
                              (getSpecFilePath(f) for f in specFiles))

        # clean up
        for fileName in allFiles:
            os.remove(getSpecFilePath(fileName))



    def test_filterValidSpecFiles(self):
        """Tests the :meth:`_Archiving.filterValidSpecFiles()` method.

        Creates two :term:`archive specification files <archive specification file>`, one with defined ``name``
        variable and the other without it.  It calls tested method with iterable of these two files and compares that
        the returned iterable contains a member that equals to the value of the specifies ``name`` variable and the
        member that equals to the file name of the second file."""

        archiveSpecFilesPaths = (ArchiveSpecTestUtils.makeArchiveSpecFile(name = self.__ARCHIVE_NAME),
                                 ArchiveSpecTestUtils.makeArchiveSpecFile())

        archiveNames = self.__archiving.filterValidSpecFiles(archiveSpecFilesPaths)

        self.assertCountEqual(
            (self.__ARCHIVE_NAME,
             os.path.basename(archiveSpecFilesPaths[1]).replace(ConfigConstants.ARCHIVE_SPEC_EXT, "")),
            archiveNames)



    def test_getArchiveInfo(self):
        """Tests the :meth:`_Archiving.getArchiveInfo()` method.

        Creates an :term:`archive specification file` with some defined variables.  Also sets up Archiver service mocks
        to return predefined values.  Calls the tested method and checks that :class:`_ArchiveInfo` instance is
        created; then checks a few basic properties that they have expected values."""

        PATH = os.curdir
        ARCHIVER = ArchiverTypes.TarXz
        DEST_DIR = '"test dest dir"'
        MAX_BACKUP_LEVEL = 3

        # set up archive specification file and archiver service mocks
        archiveSpecFilePath = ArchiveSpecTestUtils.makeArchiveSpecFile(
            name = self.__ARCHIVE_NAME, path = PATH, archiver = ARCHIVER, destDir = DEST_DIR)
        archiverMock = mock.Mock(spec_set = _TarArchiverProviderBase)
        archiverMock.getMaxBackupLevel.return_value = MAX_BACKUP_LEVEL
        ArchivingTestUtils._setUpArchiverServices(self.__serviceAccessorMock, archiverMock,
                                                  supportedFeatures = frozenset({ArchiverFeatures.Incremental}))

        # call the tested method
        archiveInfo = self.__archiving.getArchiveInfo(archiveSpecFilePath)

        self.assertIsNotNone(archiveInfo)
        self.assertEqual(self.__ARCHIVE_NAME, archiveInfo.name)
        self.assertEqual(PATH, archiveInfo.path)
        self.assertEqual(ARCHIVER, archiveInfo.archiverType)
        self.assertEqual(DEST_DIR, archiveInfo.destDir)
        self.assertFalse(archiveInfo.incremental)
        self.assertEqual(MAX_BACKUP_LEVEL - 1, archiveInfo.backupLevel)
        self.assertFalse(archiveInfo.restarting)
        self.assertIsNone(archiveInfo.lastRestart)

# }}} CLASSES
