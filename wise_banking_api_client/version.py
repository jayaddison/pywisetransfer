# icalendar_compatibility
# Copyright (C) 2025  Nicco Kunzmann
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see
# <https://www.gnu.org/licenses/>.
try:
    from ._version import __version__, __version_tuple__, version, version_tuple
except ModuleNotFoundError:
    __version__ = version = "0.0dev0"
    __version_tuple__ = version_tuple = (0, 0, "dev0")
import sys
from importlib.metadata import version as get_version

cli_version = f"""{__version__}

Components:
"""
modules = [
    "recurring-ical-events",
    "icalendar",
    "python-dateutil",
    "pytz",
    "click",
    "tzdata",
    "x-wr-timezone",
]
modules.sort()
for module in modules:
    try:
        cli_version += f"{module}: {get_version(module)}\n"
    except ModuleNotFoundError:  # noqa: PERF203
        cli_version += f"{module}: not installed\n"

cli_version += f"""
Python: {sys.version}"""

__all__ = [
    "__version__",
    "__version_tuple__",
    "cli_version",
    "version",
    "version_tuple",
]
