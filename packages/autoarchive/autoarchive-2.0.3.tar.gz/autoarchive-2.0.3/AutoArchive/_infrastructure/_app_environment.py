# _app_environment.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2022 Róbert Čerňanský



""":class:`AppEnvironment` class"""



__all__ = ["AppEnvironment"]



# {{{ CLASSES

class AppEnvironment:
    """Container class for various application-related information.

    :param executableName: Name of the startup script.
    :type executableName: ``str``
    :param commandLineOptions: Options passed on the command line.
    :type commandLineOptions: ``collections.abc.Mapping``
    :param arguments: Arguments passed on the command line.
    :type arguments: ``list<str>``"""

    def __init__(self, executableName, commandLineOptions, arguments):
        self.__executableName = executableName
        self.__commandLineOptions = commandLineOptions
        self.__arguments = arguments



    @property
    def executableName(self):
        """Name of the script that was used to start this application.

        :rtype: ``str``"""

        return self.__executableName



    @property
    def commandLineOptions(self):
        """Command line options.

        :rtype: ``collections.abc.Mapping``"""

        return self.__commandLineOptions



    @property
    def arguments(self):
        """Command line arguments.

        :rtype: ``list<str>``"""

        return self.__arguments

# }}} CLASSES
