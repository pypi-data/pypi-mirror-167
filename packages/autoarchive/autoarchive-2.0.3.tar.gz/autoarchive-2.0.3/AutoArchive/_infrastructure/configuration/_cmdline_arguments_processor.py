# _cmdline_arguments_processor.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2022 Róbert Čerňanský



""":class:`_CmdlineArgumentsProcessor` class."""



__all__ = ["_CmdlineArgumentsProcessor"]



# {{{ INCLUDES

from AutoArchive._infrastructure.utils import Utils
from . import OptionsUtils

# }}} INCLUDES



# {{{ CLASSES

class _CmdlineArgumentsProcessor:
    """Processes command-line arguments and populates :class:`.IConfiguration` instance.

    :param commandLineOptions: Command-line options and their values.
    :type commandLineOptions: ``collections.abc.Mapping``"""

    def __init__(self, commandLineOptions):
        self.__commandLineOptions = commandLineOptions



    def populateConfiguration(self, configuration):
        """Populates ``configuration`` with options specified on the command line.

        .. note:: Options that are not defined in the :class:`.Options` class are skipped; it is assumed that they are
           commands for command-line UI.

        :param configuration: Configuration that should be populated.
        :type configuration: :class:`._Configuration`"""

        for option in self.__commandLineOptions:
            value = self.__commandLineOptions[option]
            option = option.replace("_", "-")
            try:
                if OptionsUtils.isExistingOption(option):
                    configuration._addOrReplaceOption(option, str(value))
            except ValueError:
                Utils.fatalExit(
                    f"Wrong value \"{value}\" of the option \"{option}\" specified on the command line.")

# }}} CLASSES
