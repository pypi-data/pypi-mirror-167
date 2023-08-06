# test_execute_commands.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2017 Róbert Čerňanský



""":class:`TestExecuteCommands`."""



__all__ = ["TestExecuteCommands"]



# {{{ INCLUDES

import unittest
from mock import call

from AutoArchive._infrastructure.configuration import Options
from AutoArchive._services.external_command_executor import ExternalCommandExecutorServiceIdentification
from AutoArchive.tests import ComponentTestUtils
from AutoArchive._infrastructure.service.tests import ServiceTestUtils
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from AutoArchive._application.archiving.archive_spec.tests import ArchiveSpecTestUtils
from ...archiving_test_utils import ArchivingTestUtils


# }}} INCLUDES



# {{{ CLASSES

class TestExecuteCommands(unittest.TestCase):
    """Test of :meth:`._Archiving.makeBackup()` method for the commands execution.

    Before and after backup creation arbitrary commands can be executed.  This test configures such commands
    and checks whether they are executed."""

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



    def test_makeBackupExecuteCommandBeforeAndAfter(self):
        """Tests that defined commands are executed before and after backup creation.

        Configures a test command to be executed before backup creation and another command to be executed after
        the creation.  Creates backup and checks whether both command were executed."""

        BEFORE_COMMAND = "test before command"
        AFTER_COMMAND = "test_after_command"

        archiverMock = ArchiverTestUtils.createArchiverMock()
        serviceAccessorMock = ServiceTestUtils.createServiceAccessorMock({})

        options = {
            Options.COMMAND_BEFORE_BACKUP: str.format("\"{}\"", BEFORE_COMMAND),
            Options.COMMAND_AFTER_BACKUP: AFTER_COMMAND
        }
        ArchivingTestUtils._createBackup(archiverMock, options = options, serviceAccessorMock = serviceAccessorMock)

        externalCommandExecutorMock = serviceAccessorMock.getOrCreateService(
            ExternalCommandExecutorServiceIdentification, None)
        externalCommandExecutorMock.execute.assert_has_calls([call(BEFORE_COMMAND, None), call(AFTER_COMMAND, None)])
        self.assertEqual(2, externalCommandExecutorMock.execute.call_count,
                         "Unexpected number of external command executions.")



    def test_makeBackupExecuteCommandAfter(self):
        """Tests that defined command is executed after backup creation.

        Configures a test command to be executed after backup creation, creates backup and checks whether the
        command was executed."""

        AFTER_COMMAND = "test"
        AFTER_COMMAND_ARGUMENTS = ["arg1", "arg2 with spaces", "arg3"]

        archiverMock = ArchiverTestUtils.createArchiverMock()

        serviceAccessorMock = ServiceTestUtils.createServiceAccessorMock({})

        options = {
            Options.COMMAND_AFTER_BACKUP: str.format("{} {} \"{}\" {}", AFTER_COMMAND,
                                                              *AFTER_COMMAND_ARGUMENTS)
        }
        ArchivingTestUtils._createBackup(archiverMock, options = options, serviceAccessorMock = serviceAccessorMock)

        externalCommandExecutorMock = serviceAccessorMock.getOrCreateService(
            ExternalCommandExecutorServiceIdentification, None)
        externalCommandExecutorMock.execute.assert_called_once_with(AFTER_COMMAND, AFTER_COMMAND_ARGUMENTS)
