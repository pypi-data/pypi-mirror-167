#-----------------------------------------------------------------------------
# Copyright (c) 2013-2022, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------

from PyInstaller.utils.hooks.qt import add_qt5_dependencies, get_qt_qml_files, pyqt5_library_info

hiddenimports, binaries, datas = add_qt5_dependencies(__file__)
qml_binaries, qml_datas = get_qt_qml_files(pyqt5_library_info)
binaries += qml_binaries
datas += qml_datas
