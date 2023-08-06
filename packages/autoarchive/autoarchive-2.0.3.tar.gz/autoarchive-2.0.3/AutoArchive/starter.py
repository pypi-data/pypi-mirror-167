# starter.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2022 Róbert Čerňanský



"""Initializes the application and starts it."""



__all__ = ["Starter"]



# {{{ INCLUDES

from abc import ABCMeta, abstractmethod
import os
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter, SUPPRESS

from ._meta import _Meta
from AutoArchive._infrastructure.utils import Constants, Utils
from AutoArchive._infrastructure._app_environment import AppEnvironment
from AutoArchive._infrastructure.service._service_accessor import ServiceAccessor
from AutoArchive._infrastructure._application_context import ApplicationContext
from AutoArchive._infrastructure.configuration._configuration_factory import ConfigurationFactory
from AutoArchive._infrastructure.configuration import Options, OptionsUtils, ArchiverTypes
from AutoArchive._infrastructure.storage._file_storage import FileStorage
from AutoArchive._services.archiver._archiver_service_component import ArchiverServiceComponent
from AutoArchive._services.external_command_executor._external_command_executor_service_component import \
    ExternalCommandExecutorServiceComponent
from AutoArchive._application.archiving import ArchivingApplication
from AutoArchive._ui.cmdline._user_action_executor import UserActionExecutor
from AutoArchive._ui.cmdline._cmdline_ui import CmdlineUi
from AutoArchive._ui.cmdline._cmdline_commands import CmdlineCommands

# }}} INCLUDES



# {{{ CONSTANTS

#: Tuple of service components
_SERVICE_COMPONENTS = (ExternalCommandExecutorServiceComponent, ArchiverServiceComponent)

# }}} CONSTANTS



# {{{ CLASSES

class Starter(metaclass = ABCMeta):
    "Fires up the show."

    @abstractmethod
    def __init__(self):
        pass



    @classmethod
    def start(cls, programArgs = sys.argv):
        "Initializes and starts the program."

        try:
            options, arguments = cls.__parseArguments(programArgs[1:])
            appEnvironment = AppEnvironment(os.path.basename(programArgs[0]), options, arguments)
            configuration = ConfigurationFactory.makeConfiguration(appEnvironment)
            storage = FileStorage(configuration)

            applicationContext = ApplicationContext(appEnvironment, configuration, storage)
            serviceAccessor = ServiceAccessor()
            serviceComponents = cls.__createServiceComponents(applicationContext, serviceAccessor)

            cmdlineUi = CmdlineUi(appEnvironment, configuration)

            archivingApplication = ArchivingApplication(cmdlineUi, applicationContext, serviceAccessor)

            return 0 if UserActionExecutor(cmdlineUi, applicationContext, archivingApplication).execute() else 1
        except KeyboardInterrupt:
            print("\nAborted by user.")
            return 1
        except Exception as ex:
            import traceback
            if Constants.DEBUG:
                print(traceback.print_exc())
            else:
                Utils.printError(str.format("Exception occurred: {}.", traceback.format_exception_only(type(ex), ex)))
            return 1



    @staticmethod
    def __createServiceComponents(applicationContext, serviceAccessor):
        serviceComponents = []
        for serviceComponentClass in _SERVICE_COMPONENTS:
            serviceComponents.append(serviceComponentClass(applicationContext, serviceAccessor))
        return serviceComponents



    @classmethod
    def __parseArguments(cls, programArgs):
        "Parses command line arguments."

        # define usage and version strings
        usage = "%(prog)s [options] [command] [AA_SPEC ...]"
        description = _Meta.DESCRIPTION
        version = """\
%(prog)s version {version}

{copyright}

{license}
    """.format(version = _Meta.VERSION, copyright = _Meta.COPYRIGHT, license = _Meta.LICENSE)

        # create parser and add the options
        # we use RawDescriptionHelpFormatter to preserve format of 'version' text
        parser = ArgumentParser(usage = usage, description = description, add_help = False,
                                formatter_class = RawDescriptionHelpFormatter, argument_default = SUPPRESS)

        parser.add_argument("aaSpecs",
                            metavar = "AA_SPEC",
                            nargs = "*",
                            help = str.format(
                                "Archive specification.  It determines the archive specification file that shall be " +
                                "processed.  If AA_SPEC contains the \".aa\" extension then it is taken as the path " +
                                "to an archive specification file.  Otherwise, if specified without the extension, " +
                                "the corresponding .aa file is searched in the archive specifications directory " +
                                "(see option --{}).)", Options.ARCHIVE_SPECS_DIR))

        # {{{ commands

        commandsGroup = parser.add_argument_group(
            "Commands",
            "Commands for program's operations.  The default operation is the backup " +
            "creation if no command is specified.")

        commandsGroup.add_argument(cls.__makeCmdlineOption(CmdlineCommands.LIST),
                                   action = "store_true",
                                   help = "Show all configured or orphaned archives.")

        commandsGroup.add_argument(cls.__makeCmdlineOption(CmdlineCommands.PURGE),
                                   action = "store_true",
                                   help = "Purge stored data for an orphaned archive.")

        commandsGroup.add_argument("--version",
                                   action = "version",
                                   version = version,
                                   help = "Show program's version number and exit.")

        commandsGroup.add_argument("-h", "--help", action = "help", help = "Show this help message and exit.")

        # }}} commands

        # {{{ archiving related options

        archivingGroup = parser.add_argument_group("Archiving options")

        archiverChoices = [OptionsUtils.archiverTypeToStr(arch) for arch in ArchiverTypes]
        archivingGroup.add_argument("-a", cls.__makeCmdlineOption(Options.ARCHIVER),
                                    metavar = "ARCHIVER",
                                    choices = archiverChoices,
                                    help = str.format("Specify archiver type.  Supported types are: {choices} " +
                                                      "(default: targz).",  choices = archiverChoices))

        compressionLevelChoices = [str(level) for level in range(0, 10)]
        archivingGroup.add_argument("-c", cls.__makeCmdlineOption(Options.COMPRESSION_LEVEL),
                                    choices = compressionLevelChoices,
                                    metavar = "NUM",
                                    help = str.format(
                                        "Compression strength level.  If not specified, default " +
                                        "behaviour of underlying compression program will be used.  " +
                                        "Valid range is from {rangeFrom} to {rangeTo}.",
                                        rangeFrom = compressionLevelChoices[0], rangeTo = compressionLevelChoices[-1]))

        archivingGroup.add_argument("-d", cls.__makeCmdlineOption(Options.DEST_DIR),
                                    metavar = "DIR_PATH",
                                    help = "Directory where the backup will be created (default: <current directory>).")

        archivingGroup.add_argument(cls.__makeCmdlineOption(Options.OVERWRITE_AT_START),
                                    action = "store_true",
                                    help = "If enabled, backups are overwritten at the start of creation.  If " +
                                           "disabled (default), backups are overwritten at the end of creation.  " +
                                           "Enabling this option can be useful with big backups and low free space " +
                                           "on the backup volume.")

        # }}} archiving related options

        # {{{ incremental archiving related options

        incrementalGroup = parser.add_argument_group("Incremental archiving options")

        incrementalGroup.add_argument("-i", cls.__makeCmdlineOption(Options.INCREMENTAL),
                                      action = "store_true",
                                      help = "Perform incremental backup.")

        incrementalGroup.add_argument("-l", cls.__makeCmdlineOption(Options.LEVEL),
                                      type = int,
                                      help = "Specify the backup level which should be created.  All information " +
                                             "about higher levels---if any exists---will be erased.  If not " +
                                             "present, the next level in a row will be created.")

        incrementalGroup.add_argument(cls.__makeCmdlineOption(Options.RESTARTING),
                                      action = "store_true",
                                      help = "Turns on backup level restarting.  See other '*restart-*' options to " +
                                             "configure the restarting behaviour.")

        incrementalGroup.add_argument(cls.__makeCmdlineOption(Options.RESTART_AFTER_LEVEL),
                                      type = int,
                                      metavar = "LEVEL",
                                      help = str.format("Maximal backup level.  If reached, it will be restarted " +
                                                        "back to a lower level (which is typically level 1 but it " +
                                                        "depends on '--{}') (default: 10).",
                                                        Options.MAX_RESTART_LEVEL_SIZE))

        incrementalGroup.add_argument(cls.__makeCmdlineOption(Options.RESTART_AFTER_AGE),
                                      type = int,
                                      metavar = "DAYS",
                                      help = str.format("Number of days after which the backup level is restarted.  " +
                                                        "Similarly to '--{}' it will be restarted to level 1 or " +
                                                        "higher.", Options.RESTART_AFTER_LEVEL))

        incrementalGroup.add_argument(cls.__makeCmdlineOption(Options.FULL_RESTART_AFTER_COUNT),
                                      type = int,
                                      metavar = "COUNT",
                                      help = "Number of backup level restarts after which the level is restarted to 0.")

        incrementalGroup.add_argument(cls.__makeCmdlineOption(Options.FULL_RESTART_AFTER_AGE),
                                      type = int,
                                      metavar = "DAYS",
                                      help = "Number of days after which the backup level is restarted to 0.")

        incrementalGroup.add_argument(cls.__makeCmdlineOption(Options.MAX_RESTART_LEVEL_SIZE),
                                      type = int,
                                      metavar = "PERCENTAGE",
                                      help = "Maximal percentage size of a backup (of level > 0) to which level is " +
                                             "allowed restart to.  The size is percentage of size of the level 0 " +
                                             "backup file.  If a backup of particular level has its size bigger " +
                                             "than defined percentage, restart to that level will not be allowed.")

        incrementalGroup.add_argument(cls.__makeCmdlineOption(Options.REMOVE_OBSOLETE_BACKUPS),
                                      action = "store_true",
                                      help = "Turn on removing backups of levels that are no longer valid due to " +
                                             "the backup level restart.  All backups of the backup level higher " +
                                             "than the one currently being created will be removed.")

        # }}} incremental archiving related options

        # {{{ options related to old backups keeping

        keepingGroup = parser.add_argument_group("Options for keeping old backups")

        keepingGroup.add_argument("-k", cls.__makeCmdlineOption(Options.KEEP_OLD_BACKUPS),
                                  action = "store_true",
                                  help = str.format("Turn on backup keeping.  When a backup is about to be " +
                                                    "overwritten, it is renamed instead.  If '--{}' is enabled it " +
                                                    "applies to all corresponding increments.  The new name is " +
                                                    "created by inserting a keeping ID in front of backup file(s) " +
                                                    "extension.  The keeping ID is a string from interval 'aa', " +
                                                    "'ab', ..., 'zy', 'zz' where 'aa' represents most recent kept " +
                                                    "backup.", Options.INCREMENTAL))

        keepingGroup.add_argument(cls.__makeCmdlineOption(Options.NUMBER_OF_OLD_BACKUPS),
                                  type = int,
                                  metavar = "NUM",
                                  help = str.format("Number of old backups to keep when '--{}' is enabled " +
                                                    "(default: 1).", Options.KEEP_OLD_BACKUPS))

        # }}} options related to old backups keeping

        # {{{ command execution options

        commandExecutionGroup = parser.add_argument_group("Command execution options")

        commandExecutionGroup.add_argument(cls.__makeCmdlineOption(Options.COMMAND_BEFORE_ALL_BACKUPS),
                                           type = str,
                                           metavar = "COMMAND_BEFORE_ALL",
                                           help = "Arbitrary command that will be executed before backup creation " +
                                                  "for the set of selected archives.")

        commandExecutionGroup.add_argument(cls.__makeCmdlineOption(Options.COMMAND_AFTER_ALL_BACKUPS),
                                           metavar = "COMMAND_AFTER_ALL",
                                           help = "Arbitrary command that will be executed after backup creation " +
                                                  "for the set of selected archives.")

        commandExecutionGroup.add_argument(cls.__makeCmdlineOption(Options.COMMAND_BEFORE_BACKUP),
                                           metavar = "COMMAND_BEFORE",
                                           help = "Arbitrary command to execute prior to each backup creation.")

        commandExecutionGroup.add_argument(cls.__makeCmdlineOption(Options.COMMAND_AFTER_BACKUP),
                                           metavar = "COMMAND_AFTER",
                                           help = "Arbitrary command to execute after each backup creation.")

        # }}} command execution options

        # {{{ general options

        generalGroup = parser.add_argument_group("General options")

        generalGroup.add_argument("-v", cls.__makeCmdlineOption(Options.VERBOSE),
                                  action = "count",
                                  help = "Turn on verbose output.")

        generalGroup.add_argument("-q", cls.__makeCmdlineOption(Options.QUIET),
                                  action = "store_true",
                                  help = str.format("Turn on quiet output.  Only errors will be shown.  If --{quiet} " +
                                                    "is turned on at the same level as --{verbose} (e. g. both are " +
                                                    "specified on the command line) then --{quiet} has higher " +
                                                    "priority than --{verbose}.", quiet = Options.QUIET,
                                                    verbose = Options.VERBOSE))

        generalGroup.add_argument(cls.__makeCmdlineOption(Options.ALL),
                                  action = "store_true",
                                  help = str.format("Operate on all configured archives. See also --{}.",
                                                    Options.ARCHIVE_SPECS_DIR))

        generalGroup.add_argument(cls.__makeCmdlineOption(Options.ARCHIVE_SPECS_DIR),
                                  metavar = "DIR_PATH",
                                  help = "Directory where archive specification files will be searched for (default: " +
                                         "~/.config/aa/archive_specs).")

        generalGroup.add_argument(cls.__makeCmdlineOption(Options.USER_CONFIG_FILE),
                                  metavar = "FILE_PATH",
                                  help = "Alternate user configuration file (default: ~/.config/aa/aa.conf).")

        generalGroup.add_argument(cls.__makeCmdlineOption(Options.USER_CONFIG_DIR),
                                  metavar = "DIR_PATH",
                                  help = "Alternate user configuration directory (default: ~/.config/aa).")

        # }}} general options

        # {{{ force options

        forceGroup = parser.add_argument_group("Force options", "Options to override standard options defined in " +
                                               "archive specification files.")

        forceGroup.add_argument(cls.__makeCmdlineOption(Options.FORCE_ARCHIVER),
                                choices = archiverChoices,
                                metavar = "ARCHIVER",
                                help = str.format(
                                    "Force archiver type.  See --{archiver} option for supported types.",
                                    archiver = Options.ARCHIVER))

        forceGroup.add_argument(cls.__makeCmdlineOption(Options.FORCE_INCREMENTAL),
                                action = "store_true",
                                help = "Force incremental backup.")

        forceGroup.add_argument(cls.__makeCmdlineOption(Options.FORCE_RESTARTING),
                                action = "store_true",
                                help = "Force backup level restarting.")

        forceGroup.add_argument(cls.__makeCmdlineOption(Options.FORCE_COMPRESSION_LEVEL),
                                choices = compressionLevelChoices,
                                metavar = "NUM",
                                help = "Force compression strength level.")

        forceGroup.add_argument(cls.__makeCmdlineOption(Options.FORCE_DEST_DIR),
                                metavar = "DIR_PATH",
                                help = "Force the directory where the backup will be created.")

        forceGroup.add_argument(cls.__makeCmdlineOption(Options.FORCE_COMMAND_BEFORE_BACKUP),
                                metavar = "COMMAND_BEFORE",
                                help = "Force configuration of the command to execute prior to each backup creation.")

        forceGroup.add_argument(cls.__makeCmdlineOption(Options.FORCE_COMMAND_AFTER_BACKUP),
                                metavar = "COMMAND_AFTER",
                                help = "Force configuration of the command to execute after each backup creation.")

        forceGroup.add_argument(cls.__makeCmdlineOption(Options.FORCE_OVERWRITE_AT_START),
                                action = "store_true",
                                help = "Force backup overwriting behavior.")

        # }}} force options

        # {{{ negation options

        negationGroup = parser.add_argument_group("Negation options", "Negative variants of standard boolean options.")

        negationGroup.add_argument(cls.__makeCmdlineOption(Options.NO_INCREMENTAL),
                                   action = "store_true",
                                   help = "Disable incremental backup.")

        negationGroup.add_argument(cls.__makeCmdlineOption(Options.NO_RESTARTING),
                                   action = "store_true",
                                   help = "Turn off backup level restarting.")

        negationGroup.add_argument(cls.__makeCmdlineOption(Options.NO_REMOVE_OBSOLETE_BACKUPS),
                                   action = "store_true",
                                   help = "Turn off obsolete backups removing.")

        negationGroup.add_argument(cls.__makeCmdlineOption(Options.NO_KEEP_OLD_BACKUPS),
                                   action = "store_true",
                                   help = "Turn off backup keeping.")

        negationGroup.add_argument(cls.__makeCmdlineOption(Options.NO_ALL),
                                   action = "store_true",
                                   help = "Do not operate on all configured archive specification files.")

        negationGroup.add_argument(cls.__makeCmdlineOption(Options.NO_OVERWRITE_AT_START),
                                   action = "store_true",
                                   help = "Do not overwrite backup at the start of creation. Overwrite after the new " +
                                          "backup is created.")

        # }}} negation options

        args = parser.parse_args(programArgs)
        options = vars(args)
        arguments = options["aaSpecs"] if "aaSpecs" in options else []
        return options, arguments



    @staticmethod
    def __makeCmdlineOption(option):
        return "--" + str(option)

# }}} CLASSES
