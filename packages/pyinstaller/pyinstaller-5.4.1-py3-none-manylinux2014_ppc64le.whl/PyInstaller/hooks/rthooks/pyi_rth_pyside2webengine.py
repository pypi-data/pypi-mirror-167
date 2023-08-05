#-----------------------------------------------------------------------------
# Copyright (c) 2015-2022, PyInstaller Development Team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: Apache-2.0
#-----------------------------------------------------------------------------

import os
import sys

if sys.platform == 'darwin':
    # If QtWebEngineProcess was collected from a framework-based Qt build, we need to set QTWEBENGINEPROCESS_PATH.
    # If not (a dylib-based build; Anaconda on macOS), it should be found automatically, same as on other OSes.
    process_path = os.path.normpath(
        os.path.join(
            sys._MEIPASS, 'PySide2', 'Qt', 'lib', 'QtWebEngineCore.framework', 'Helpers', 'QtWebEngineProcess.app',
            'Contents', 'MacOS', 'QtWebEngineProcess'
        )
    )
    if os.path.exists(process_path):
        os.environ['QTWEBENGINEPROCESS_PATH'] = process_path
