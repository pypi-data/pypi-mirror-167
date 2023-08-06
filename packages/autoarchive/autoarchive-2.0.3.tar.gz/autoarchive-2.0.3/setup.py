#!/usr/bin/env python

# setup.py
#
# Project: AutoArchive
# License: GNU GPLv3
#
# Copyright (C) 2003 - 2022 Róbert Čerňanský



"""The setup script for AutoArchive."""



# {{{ INCLUDES

import os, os.path, glob
from setuptools import setup
from setuptools.command.sdist import sdist

from AutoArchive._meta import *

# }}} INCLUDES



# {{{ CLASSES

class PreserveLinksSdist(sdist):

    def copy_file(self, src, dst, preserve_mode = 1, preserve_times = 1, link = None, level = 1):
        """Copy a file with preservation of symbolic links in mind.

        If ``src`` is symlink pointing to a relative destination, ``dst`` will be created as a symlink pointing to
        the same destination.  If ``dst`` is directory, symlink with the same name as ``src`` will be created in
        ``dst``.  If ``src`` if not symlink then base :meth:`copy_file()` method will be called."""

        copied = False

        # if src is relative symbolic link, create dst as symlink pointing to the same destination
        if os.path.islink(src):
            linkDestination = os.readlink(src)
            if not os.path.isabs(linkDestination):

                if os.path.isdir(dst):
                    dstFile = os.path.join(dst, os.path.basename(src))
                else:
                    dstFile = dst

                if not self.dry_run:
                    os.symlink(linkDestination, dstFile)
                copied = True

        # call base copy_file() method if symlink was not created
        if not copied:
            dstFile, copied = super().copy_file(src, dst, preserve_mode = preserve_mode,
                                                preserve_times = preserve_times, link = link, level = level)

        return dstFile, copied

# }}} CLASSES



# {{{ FUNCTIONS

def findDataFiles(destDir, srcDir):
    """Returns content of ``srcDir`` in a format required by ``data_files``."""

    dataFiles = []
    srcDirName = os.path.dirname(srcDir)
    for root, dirs, files in os.walk(srcDir):
        if files:
            dataFiles.append(
                (os.path.join(destDir, os.path.relpath(root, srcDirName)),
                 list(map(lambda f: os.path.join(root, f), files))))
    return dataFiles

# }}} FUNCTIONS



# {{{ MAIN PROGRAM

docDir = os.path.join("share/doc", _Meta.PACKAGE_NAME + "-" + _Meta.VERSION)

dataFiles = [
    (os.path.join("share", _Meta.PACKAGE_NAME), ["data/configuration/aa.conf.dist"]),
    ("share/man/man1", ["doc/user/man/aa.1", "doc/user/man/autoarchive.1"]),
    ("share/man/man5", ["doc/user/man/aa.conf.5",
                        "doc/user/man/aa_arch_spec.5"]),
    (docDir, ["README", "README.sk", "NEWS", "COPYING"]),
    (os.path.join(docDir, "examples"), glob.glob("doc/user/examples/*")),
    ("bin", ["bin/autoarchive"])
    ]

dataFiles.extend(findDataFiles(docDir, "doc/user/html"))

setup(
    name = _Meta.PACKAGE_NAME,
    version = _Meta.VERSION,
    description = _Meta.DESCRIPTION,
    long_description = """\
**AutoArchive** is a simple utility to help create backups more easily.  The
idea of the program is that all essential information for creating a single
backup---such as list of directories that should be archived, the archive name,
etc.---is stored in a single file -- the `archive specification file`.  It can
use ‘tar’ for creating archives, it has a command line interface and supports
incremental backups.""",
    author = "Róbert Čerňanský",
    author_email = "openhs@users.sourceforge.net",
    url = "https://autoarchive.sourceforge.io",
    download_url = str.format(
        "https://sourceforge.net/projects/autoarchive/files/autoarchive/{0}/autoarchive-{0}.tar.gz/download",
        _Meta.VERSION),
    license = "GNU GPLv3",
    keywords = "backup archive archiving compression tar",
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: System :: Archiving :: Compression",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities"
    ],
    packages = ["AutoArchive",
                "AutoArchive._infrastructure", "AutoArchive._infrastructure.configuration",
                "AutoArchive._infrastructure.service", "AutoArchive._infrastructure.storage",
                "AutoArchive._infrastructure.ui", "AutoArchive._infrastructure.utils",
                "AutoArchive._infrastructure.utils.interval",
                "AutoArchive._services", "AutoArchive._services.archiver",
                "AutoArchive._services.external_command_executor",
                "AutoArchive._application", "AutoArchive._application.archiving",
                "AutoArchive._application.archiving._archiver_manipulator",
                "AutoArchive._application.archiving.archive_spec",
                "AutoArchive._ui", "AutoArchive._ui.cmdline"],
    scripts = ["bin/aa"],
    data_files = dataFiles,

    cmdclass = {"sdist": PreserveLinksSdist},

    python_requires = ">=3.7"
)

# }}} MAIN PROGRAM
