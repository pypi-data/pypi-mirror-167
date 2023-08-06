# test_configuration.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2022 Róbert Čerňanský



""":class:`TestConfiguration` class."""



__all__ = ["TestConfiguration"]



# {{{ INCLUDES

import unittest
import os
from argparse import ArgumentParser, SUPPRESS

from AutoArchive._infrastructure.configuration import Options
from AutoArchive.tests import ComponentTestUtils
from .configuration_test_utils import ConfigurationTestUtils

# }}} INCLUDES



# {{{ CLASSES

class TestConfiguration(unittest.TestCase):
    """Test of :class:`ConfigurationBase` public API."""

    # Each test should call __setUpConfiguration() method; if called with non-None configFileContent argument
    # then the test has to call __removeUserConfigFile() at the end of the its method.



    # Name of the user configuration file.
    __USER_CONFIG_FILE = "test_aa.conf"



    @classmethod
    def setUpClass(cls):
        ConfigurationTestUtils._setUpClassConfigurationComponent()



    @classmethod
    def tearDownClass(cls):
        ConfigurationTestUtils._tearDownClassConfigurationComponent()



    def setUp(self):

        # SMELL: Parser configuration here should be taken (not copied) from the code.  Because if, for example,
        # 'argument_default = SUPPRESS' would not be specified in the code then the program behaviour would
        # be incorrect.
        self.__parser = ArgumentParser(argument_default = SUPPRESS)



    def tearDown(self):
        ConfigurationTestUtils._tearDownConfigurationComponent()



    # {{{ __getitem__() tests

    def test_getItemBool(self):
        """Tests the __getitem__() method for a ``bool`` value.

        Sets a ``bool``\-type option through the command line and verifies that its retrieved value is ``True``."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        cmdline = [ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL)]
        configuration = self.__setUpConfiguration(cmdline)

        self.assertTrue(configuration[Options.INCREMENTAL])



    def test_getItemInt(self):
        """Tests the __getitem__() method for an ``int`` value.

        Sets an ``int``\-type option through the command line and verifies that its retrieved value is equal
        to the one that was set."""

        LEVEL = 99

        self.__parser.add_argument(ConfigurationTestUtils._makeCmdlineOption(Options.LEVEL), type = int)
        self.__parser.add_argument(ConfigurationTestUtils._makeCmdlineOption(Options.RESTART_AFTER_AGE), type = int)

        cmdline = [ConfigurationTestUtils._makeCmdlineOption(Options.LEVEL) + "=" + str(LEVEL)]
        configuration = self.__setUpConfiguration(cmdline)

        # test that the LEVEL option was set to LEVEL value
        self.assertEqual(configuration[Options.LEVEL], LEVEL)

        # test that the RESTART_AFTER_AGE option, which was not specified at all, was set to None
        self.assertIsNone(configuration[Options.RESTART_AFTER_AGE])



    def test_getItemStr(self):
        """Tests the __getitem__() method for a ``str`` value.

        Sets an ``str``\-type option through the command line and verifies that its retrieved value is equal to the
        one that was set."""

        DEST_DIR = "TEST_DEST_DIR"

        self.__parser.add_argument(ConfigurationTestUtils._makeCmdlineOption(Options.DEST_DIR))
        cmdline = [ConfigurationTestUtils._makeCmdlineOption(Options.DEST_DIR) + "=" + DEST_DIR]
        configuration = self.__setUpConfiguration(cmdline)

        # test that the DEST_DIR option was set to DEST_DIR value
        self.assertEqual(configuration[Options.DEST_DIR], DEST_DIR)



    def test_getItemBoolWithNegationForm(self):
        """Tests the __getitem__() method for ``bool``\-type option with *negation form*.

        Sets up parser with a ``bool``\-type option and its *negation form*.  Sets the option through the command
        line and verifies that its retrieved value is ``True``."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.NO_INCREMENTAL), action = "store_true")
        cmdline = [ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL)]
        configuration = self.__setUpConfiguration(cmdline)

        self.assertTrue(configuration[Options.INCREMENTAL])



    def test_getItemBoolWithForceForm(self):
        """Tests the __getitem__() method for ``bool``\-type option with *force form*.

        Sets up parser with a ``bool``\-type option and its *force form*.  Sets the option through the command line
        and verifies that its retrieved value is ``True``."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.FORCE_INCREMENTAL), action = "store_true")
        cmdline = [ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL)]
        configuration = self.__setUpConfiguration(cmdline)

        self.assertTrue(configuration[Options.INCREMENTAL])



    def test_getItemBoolIfNotPresent(self):
        """Tests the __getitem__() method for ``bool``\-type option not present on the command line.

        Does not set a ``bool``\-type option through the command line and verifies that its retrieved value is
        ``False``."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        cmdline = []
        configuration = self.__setUpConfiguration(cmdline)

        self.assertFalse(configuration[Options.INCREMENTAL])



    def test_getItemBoolWithNegationFormIfNotPresent(self):
        """Tests the __getitem__() method for ``bool``\-type option with *negation form* and not present.

        Sets up parser with a ``bool``\-type option and its *negation form*.  Does not set the option through
        the command line and verifies that its retrieved value is ``False``."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.NO_INCREMENTAL), action = "store_true")
        cmdline = []
        configuration = self.__setUpConfiguration(cmdline)

        self.assertFalse(configuration[Options.INCREMENTAL])



    def test_getItemBoolWithForceFormIfNotPresent(self):
        """Tests the __getitem__() method for ``bool``\-type option with *force form* and not present.

        Sets up parser with a ``bool``\-type option and its *force form*.  Does not set the option through the
        command line and verifies that its retrieved value is ``False``."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.FORCE_INCREMENTAL), action = "store_true")
        cmdline = []
        configuration = self.__setUpConfiguration(cmdline)

        self.assertFalse(configuration[Options.INCREMENTAL])



    def test_getItemNegationForm(self):
        """Tests the __getitem__() method for an option with negation form enabled.

        Sets an option in its *normal form* and its *negation form*, both through the command line.  Verifies that
        its retrieved value is ``False`` since the *negation form* has precedence over the *normal form*."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.NO_INCREMENTAL), action = "store_true")
        cmdline = [ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL),
                   ConfigurationTestUtils._makeCmdlineOption(Options.NO_INCREMENTAL)]
        configuration = self.__setUpConfiguration(cmdline)

        # test that the INCREMENTAL option was set to False
        self.assertFalse(configuration[Options.INCREMENTAL])



    def test_getItemForceForm(self):
        """Tests the __getitem__() method for an option with force form enabled.

        Sets an option in its *negation form* and its *force form*, both through the command line.  Verifies that
        its retrieved value is ``True`` since the *force form* has precedence over the *negation form*."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.NO_INCREMENTAL), action = "store_true")
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.FORCE_INCREMENTAL), action = "store_true")
        cmdline = [ConfigurationTestUtils._makeCmdlineOption(Options.NO_INCREMENTAL),
                   ConfigurationTestUtils._makeCmdlineOption(Options.FORCE_INCREMENTAL)]
        configuration = self.__setUpConfiguration(cmdline)

        # test that the INCREMENTAL option was forced to True
        self.assertTrue(configuration[Options.INCREMENTAL])



    def test_getItemBoolUserConfig(self):
        """Tests the __getitem__() method for a ``bool``\-type option initialized from the user configuration file.

        Sets a ``bool``\-type option through the user configuration file and verifies that its retrieved value is
        equal to the one that was set."""

        # setup command line arguments
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        cmdline = []

        # setup the user configuration file
        configFileContent = """\
[Archive]
incremental = true
"""
        configuration = self.__setUpConfiguration(cmdline, configFileContent)

        self.assertTrue(configuration[Options.INCREMENTAL])

        self.__removeUserConfigFile()



    def test_getItemIntUserConfig(self):
        """Tests the __getitem__() method for an ``int``\-type option initialized from the user configuration file.

        Sets an ``int``\-type option through the user configuration file and verifies that its retrieved value is
        equal to the one that was set."""

        FULL_RESTART_AFTER_AGE = 99

        # setup command line arguments
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.FULL_RESTART_AFTER_AGE), type = int)
        cmdline = []

        # setup the user configuration file
        configFileContent = str.format("""\
[Archive]
full-restart-after-age = {}
""", FULL_RESTART_AFTER_AGE)
        configuration = self.__setUpConfiguration(cmdline, configFileContent)

        # test that the FULL_RESTART_AFTER_AGE option was set to the command line value
        self.assertEqual(configuration[Options.FULL_RESTART_AFTER_AGE], FULL_RESTART_AFTER_AGE)

        self.__removeUserConfigFile()



    def test_getItemCmdlinePrecedence(self):
        """Tests the __getitem__() method for precedence of options specified on a command line.

        Sets an option through command line and through the user configuration file.  Verifies that its retrieved value
        is equal to the one that was set through the command line because command line values overrides configuration
        file values."""

        CMDLINE_FULL_RESTART_AFTER_AGE = 98
        CONFIG_FULL_RESTART_AFTER_AGE = 99

        # setup command line options
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.FULL_RESTART_AFTER_AGE), type = int)
        cmdline = [ConfigurationTestUtils._makeCmdlineOption(Options.FULL_RESTART_AFTER_AGE) + "=" +
                   str(CMDLINE_FULL_RESTART_AFTER_AGE)]

        # setup the user configuration file
        configFileContent = str.format("""\
[Archive]
full-restart-after-age = {}
""", CONFIG_FULL_RESTART_AFTER_AGE)
        configuration = self.__setUpConfiguration(cmdline, configFileContent)

        # test that the FULL_RESTART_AFTER_AGE option was set to the command line value
        self.assertEqual(configuration[Options.FULL_RESTART_AFTER_AGE], CMDLINE_FULL_RESTART_AFTER_AGE)

        self.__removeUserConfigFile()



    def test_getItemCmdlinePrecedenceForceForm(self):
        """Tests the __getitem__() method for precedence of an option specified on a command line and force in config.

        Sets an option through command line and its *force form* through the user configuration file.  Even the
        command line options overrides those from configuration file, the *force form* should win in cases like
        this because for parsers it is *not* the same option (e. g. one is ``--compression-level`` and the other is
        ``--force-compression-level``) so they do not override each other."""

        CMDLINE_COMPRESSION_LEVEL = 98
        CONFIG_FORCE_COMPRESSION_LEVEL = 99

        # setup command line options
        self.__parser.add_argument(ConfigurationTestUtils._makeCmdlineOption(Options.COMPRESSION_LEVEL), type = int)
        cmdline = [ConfigurationTestUtils._makeCmdlineOption(Options.COMPRESSION_LEVEL) + "=" +
                   str(CMDLINE_COMPRESSION_LEVEL)]

        # setup the user configuration file
        configFileContent = str.format("""\
[Archive]
force-compression-level = {}
""", CONFIG_FORCE_COMPRESSION_LEVEL)
        configuration = self.__setUpConfiguration(cmdline, configFileContent)

        # test that the COMPRESSION_LEVEL option was set to the force value from the configuration file
        self.assertEqual(configuration[Options.COMPRESSION_LEVEL], CONFIG_FORCE_COMPRESSION_LEVEL)

        self.__removeUserConfigFile()

    # }}} __getitem__() tests



    # {{{ getRawValue() tests

    def test_getRawValue(self):
        """Tests the getRawValue() method.

        Sets an option in its *negation form* and its *force form*, both through the command line.  Verifies that
        retrieved value for its *normal form* is ``None`` and for its *negation form* and its *force form* is
        ``True``."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.NO_INCREMENTAL), action = "store_true")
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.FORCE_INCREMENTAL), action = "store_true")
        cmdline = [ConfigurationTestUtils._makeCmdlineOption(Options.NO_INCREMENTAL),
                   ConfigurationTestUtils._makeCmdlineOption(Options.FORCE_INCREMENTAL)]
        configuration = self.__setUpConfiguration(cmdline)

        # test the raw values of all forms of the INCREMENTAL option
        self.assertIsNone(configuration.getRawValue(Options.INCREMENTAL))
        self.assertTrue(configuration.getRawValue(Options.NO_INCREMENTAL))
        self.assertTrue(configuration.getRawValue(Options.FORCE_INCREMENTAL))

    # }}} getRawValue() tests



    # {{{ isOptionPresent() tests

    def test_isOptionPresentBool(self):
        """Tests the isOptionPresent() method for a ``bool``\-type option.

        Sets a ``bool``\-type option through the command line and verifies that SUT returns ``True``."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        cmdline = [ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL)]
        configuration = self.__setUpConfiguration(cmdline)

        self.assertTrue(configuration.isOptionPresent(Options.INCREMENTAL))



    def test_isOptionPresentBoolIfNotPresent(self):
        """Tests the isOptionPresent() method for a ``bool``\-type option not present.

        Does not sets a ``bool``\-type option through the command line and verifies that SUT returns ``False``."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        cmdline = []
        configuration = self.__setUpConfiguration(cmdline)

        self.assertFalse(configuration.isOptionPresent(Options.INCREMENTAL))



    def test_isOptionPresentBoolUserConfig(self):
        """Tests the isOptionPresent() method for a ``bool``\-type option present in a configuration file.

        Sets a ``bool``\-type option through the user configuration file and verifies that the SUT
        returns ``True``."""

        # setup command line arguments
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.INCREMENTAL), action = "store_true")
        cmdline = []

        # setup the user configuration file
        configFileContent = """\
[Archive]
incremental = true
"""
        configuration = self.__setUpConfiguration(cmdline, configFileContent)

        self.assertTrue(configuration.isOptionPresent(Options.INCREMENTAL))

        self.__removeUserConfigFile()



    def test_isOptionPresentInt(self):
        """Tests the isOptionPresent() method for an ``int``\-type option.

        Sets an ``int``\-type option through the command line and verifies that SUT returns ``True``."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.FULL_RESTART_AFTER_AGE), type = int)
        cmdline = [ConfigurationTestUtils._makeCmdlineOption(Options.FULL_RESTART_AFTER_AGE) + "=99"]
        configuration = self.__setUpConfiguration(cmdline)

        self.assertTrue(configuration.isOptionPresent(Options.FULL_RESTART_AFTER_AGE))



    def test_isOptionPresentIntIfNotPresent(self):
        """Tests the isOptionPresent() method for an ``int``\-type option not present.

        Does not sets an ``int``\-type option through the command line and verifies that SUT returns ``False``."""

        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.FULL_RESTART_AFTER_AGE), type = int)
        cmdline = []
        configuration = self.__setUpConfiguration(cmdline)

        self.assertFalse(configuration.isOptionPresent(Options.FULL_RESTART_AFTER_AGE))



    def test_isOptionPresentIntUserConfig(self):
        """Tests the isOptionPresent() method for an ``int``\-type option present in a configuration file.

        Sets an ``int``\-type option through the user configuration file and verifies that the SUT returns
        ``True``."""

        # setup command line arguments
        self.__parser.add_argument(
            ConfigurationTestUtils._makeCmdlineOption(Options.FULL_RESTART_AFTER_AGE), type = int)
        cmdline = []

        # setup the user configuration file
        configFileContent = """\
[Archive]
full-restart-after-age = 99
"""
        configuration = self.__setUpConfiguration(cmdline, configFileContent)

        self.assertTrue(configuration.isOptionPresent(Options.FULL_RESTART_AFTER_AGE))

        self.__removeUserConfigFile()

    # }}} isOptionPresent() tests



    # {{{ helpers

    def __setUpConfiguration(self, cmdline, configFileContent = None):
        options = vars(self.__parser.parse_args(cmdline))
        configFilePath = self.__createUserConfigFile(configFileContent) if configFileContent else None

        return ConfigurationTestUtils._setUpConfigurationComponent(options, configFilePath)



    @classmethod
    def __createUserConfigFile(cls, content):
        configFilePath = os.path.join(ComponentTestUtils.getComponentTestContext().userConfigDir,
                                      cls.__USER_CONFIG_FILE)
        with open(configFilePath, "w") as configFile:
            configFile.write(content)
        return configFilePath



    @classmethod
    def __removeUserConfigFile(cls):
        os.remove(os.path.join(ComponentTestUtils.getComponentTestContext().userConfigDir, cls.__USER_CONFIG_FILE))

    # }}} helpers

# }}} CLASSES
