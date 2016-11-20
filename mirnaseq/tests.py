#!/usr/bin/env python

"""
    mirnaseq unit tests
    Created September 2016
    Copyright (C) Damien Farrell
"""

from __future__ import absolute_import, print_function
import sys, os
import pandas as pd
import unittest
from . import base, analysis

class BasicTests(unittest.TestCase):
    """Basic tests for mirnaseq"""

    def setUp(self):
        self.df = None
        self.testdir = 'testing'
        if not os.path.exists(self.testdir):
            os.mkdir(self.testdir)
        return

    def test_tepitope(self):
        """Tepitope test"""

        df = self.df
        return


def run():
    unittest.main()

if __name__ == '__main__':
    unittest.main()