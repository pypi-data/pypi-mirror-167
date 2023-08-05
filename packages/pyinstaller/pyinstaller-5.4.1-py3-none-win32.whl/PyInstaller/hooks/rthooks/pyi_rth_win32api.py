#-----------------------------------------------------------------------------
# Copyright (c) 2013-2022, PyInstaller Development Team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: Apache-2.0
#-----------------------------------------------------------------------------

# Starting with Python 3.8, win32api failed with "ImportError: DLL load failed while importing win32clipboard: The
# specified module could not be found." This seems to be caused by pywintypes.dll not being found in various situations.
# See https://github.com/mhammond/pywin32/pull/1430 and
# https://github.com/mhammond/pywin32/commit/71afa71e11e6631be611ca5cb57cda526
# As a work-around, import pywintypes prior to win32api.

# Unfortunately, __import_pywin32_system_module__ from pywintype module assumes that in a frozen application, the
# pythoncom3X.dll and pywintypes3X.dll that are normally found in site-packages/pywin32_system32, are located
# directly in the sys.path, without bothering to check first if they are actually available in the standard location.
# This obviously runs afoul of our attempts at preserving the directory layout and placing them in the pywin32_system32
# sub-directory instead of the top-level application directory. So as a work-around, add the sub-directory to sys.path
# to keep pywintypes happy...
import sys
import os

pywin32_system32_path = os.path.join(sys._MEIPASS, 'pywin32_system32')
if os.path.isdir(pywin32_system32_path) and pywin32_system32_path not in sys.path:
    sys.path.append(pywin32_system32_path)
del pywin32_system32_path

import pywintypes  # noqa: F401, E402
