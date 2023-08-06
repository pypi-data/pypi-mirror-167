# test_show_final_error.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2017 Róbert Čerňanský



""":class:`TestShowFinalError`."""



__all__ = ["TestShowFinalError"]



# {{{ INCLUDES

import unittest
import itertools
import re

import mock

from AutoArchive._ui.cmdline._cmdline_ui import CmdlineUi
from AutoArchive._services.archiver.tests import ArchiverTestUtils
from ...archiving_test_utils import ArchivingTestUtils

# }}} INCLUDES



# {{{ CLASSES

class TestShowFinalError(unittest.TestCase):
    """Test of :meth:`._Archiving.makeBackup()` method for showing final error message."""

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



    # {{{ makeBackup() tests for show final error

    def test_makeBackupShowFinalError(self):
        """Tests the makeBackup() method for showing final error message for failed backup creation.

        Sets up the archiver service so it simulates an error upon backup creation.  Checks that the final verbose
        message saying that an error occurred was shown."""

        archiverMock = ArchiverTestUtils.createArchiverMock()
        componentUiMock = mock.Mock(spec_set = CmdlineUi)

        ArchivingTestUtils._createBackup(archiverMock, errorOccur = True, componentUiMock = componentUiMock)

        errorCallsArgs = (methodCall[1]
                          for methodCall in componentUiMock.method_calls
                          if methodCall[0] == "showVerbose")
        creationFailedCallsArgs = itertools.dropwhile(
            lambda callArg: re.search("error\(s\) occurred during", callArg[0], re.IGNORECASE) is None, errorCallsArgs)

        # we expect that the "creation failed" message will be shown
        self.assertIsNotNone(next(creationFailedCallsArgs, None),
                             "The error message \"error(s) occurred\" was not shown.")

    # }}} makeBackup() tests for show final error
