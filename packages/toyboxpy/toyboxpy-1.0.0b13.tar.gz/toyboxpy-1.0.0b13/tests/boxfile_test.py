# SPDX-FileCopyrightText: 2022-present toybox.py Contributors
#
# SPDX-License-Identifier: MIT

import unittest
import sys
import os

# -- We need to import for our parent folder here.
sys.path.append(os.path.join(sys.path[0], '..'))

from toybox.boxfile import Boxfile       # noqa: E402


class TestBoxfile(unittest.TestCase):
    """Unit tests for the Boxfile class."""

    def test_constructor(self):
        boxfile = Boxfile('tests/data/boxfile_old')
        self.assertEqual(len(boxfile.dependencies), 1)
        self.assertEqual(str(boxfile.dependencies[0]), 'github.com/DidierMalenfant/pdbase@(>=1.0.0 <2.0.0)')
        self.assertEqual(boxfile.maybeInstalledVersionAsStringForDependency(boxfile.dependencies[0]), None)
        self.assertEqual(boxfile.maybeLuaImportFile(), None)

        boxfile = Boxfile('tests/data/boxfile_current')
        self.assertEqual(len(boxfile.dependencies), 1)
        self.assertEqual(str(boxfile.dependencies[0]), 'github.com/DidierMalenfant/pdbase@(>=1.0.0 <2.0.0)')
        self.assertEqual(boxfile.maybeInstalledVersionAsStringForDependency(boxfile.dependencies[0]), '1.2.3')
        self.assertEqual(boxfile.maybeLuaImportFile(), 'source/main.lua')

        with self.assertRaises(SyntaxError) as context:
            Boxfile('tests/data/boxfile_future')

        self.assertEqual(str(context.exception), 'Incorrect format for Boxfile \'tests/data/boxfile_future/Boxfile\'.\nMaybe you need to upgrade toybox?')

        with self.assertRaises(SyntaxError) as context:
            Boxfile('tests/data/boxfile_invalid')

        self.assertEqual(str(context.exception), 'Malformed JSON in Boxfile \'tests/data/boxfile_invalid/Boxfile\'.\nExpecting \',\' delimiter: line 3 column 5 (char 40).')


if __name__ == '__main__':
    unittest.main()
