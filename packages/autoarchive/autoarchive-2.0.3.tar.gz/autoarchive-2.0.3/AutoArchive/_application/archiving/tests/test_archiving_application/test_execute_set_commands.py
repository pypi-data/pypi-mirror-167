# test_execute_set_commands.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2017 Róbert Čerňanský



""":class:`TestExecuteSetCommands`."""



__all__ = ["TestExecuteSetCommands"]



# {{{ INCLUDES

import unittest

from mock import Mock, call

from AutoArchive._infrastructure.py_additions import event
from AutoArchive._infrastructure.configuration import Options
from AutoArchive._services.external_command_executor import ExternalCommandExecutorServiceIdentification
from AutoArchive._services.archiver import ArchiverFeatures
from AutoArchive._ui.cmdline._cmdline_ui import CmdlineUi
from AutoArchive._application.archiving import ArchivingApplication
from AutoArchive._application.archiving.archive_spec import ArchiveSpecInfo
from AutoArchive.tests import ComponentTestUtils
from AutoArchive._infrastructure.configuration.tests import ConfigurationTestUtils
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from AutoArchive._application.archiving.archive_spec.tests import ArchiveSpecTestUtils
from AutoArchive._application.archiving.tests.archiving_test_utils import ArchivingTestUtils

# }}} INCLUDES



# {{{ CLASSES

class TestExecuteSetCommands(unittest.TestCase):
    """Test of :meth:`.ArchivingApplication.executeCreateAction()` method for the set commands execution.

    Before and after creation of all selected backups arbitrary commands can be executed.  This test configures such
    commands and checks whether they are executed."""

    @classmethod
    def setUpClass(cls):
        ArchivingTestUtils._setUpClassArchivingComponent()
        cls.__defaultOptions = {Options.ARCHIVE_SPECS_DIR: ComponentTestUtils.getComponentTestContext().archiveSpecsDir}



    @classmethod
    def tearDownClass(cls):
        ArchivingTestUtils._tearDownClassArchivingComponent()



    def setUp(self):
        ArchivingTestUtils._setUpArchivingComponent()
        self.__serviceAccessorMock = ArchivingTestUtils._setUpServiceAccessorMock()
        self.__componentUiMock = Mock(spec_set = CmdlineUi)

        self.__componentUiMock.messageShown = self.__messageShownEventMock
        ArchivingTestUtils._setUpArchiverServices(self.__serviceAccessorMock, ArchiverTestUtils.createArchiverMock(),
                                                  supportedFeatures = frozenset({ArchiverFeatures.Incremental}))



    def tearDown(self):
        ArchivingTestUtils._tearDownArchivingComponent()



    def test_createActionExecuteSetCommandBeforeAndAfter(self):
        """Tests that defined commands are executed before and after creation of all selected archives.

        Sets up two archive specs for backup execution.  Configures a test command to be executed before creation
        of all backups and another command to be executed after the creation.  Creates all two configured backups and
        checks whether both commands were executed."""

        BEFORE_COMMAND = "test before command"
        AFTER_COMMAND = "test_after_command"

        options = {
            Options.COMMAND_BEFORE_ALL_BACKUPS: str.format("\"{}\"", BEFORE_COMMAND),
            Options.COMMAND_AFTER_ALL_BACKUPS: AFTER_COMMAND
        }

        selectedArchiveSpecs = (ArchiveSpecInfo("any name 1", ArchiveSpecTestUtils.makeArchiveSpecFile()),
                                ArchiveSpecInfo("any name 2", ArchiveSpecTestUtils.makeArchiveSpecFile()))

        jointOptions = self.__defaultOptions.copy()
        jointOptions.update(options)
        configurationMock = ConfigurationTestUtils.createConfigurationMock(jointOptions)
        applicationContextMock = ArchivingTestUtils._setUpApplicationContextMock(configurationMock = configurationMock)
        archivingApplication = ArchivingApplication(self.__componentUiMock, applicationContextMock,
                                                    self.__serviceAccessorMock)

        archivingApplication.executeCreateAction(selectedArchiveSpecs)

        externalCommandExecutorMock = self.__serviceAccessorMock.getOrCreateService(
            ExternalCommandExecutorServiceIdentification, None)
        externalCommandExecutorMock.execute.assert_has_calls([call(BEFORE_COMMAND, None), call(AFTER_COMMAND, None)])
        self.assertEqual(2, externalCommandExecutorMock.execute.call_count,
                         "Unexpected number of external command executions.")



    @event
    def __messageShownEventMock(messageKind):
        pass

# }}} CLASSES
