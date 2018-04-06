#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Ravindra Kharche
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" BSE Corporates test
Unit tests for fetching bse corporates data.
"""
__author__ = "rpkharche@gmail.com(Ravindra Kharche)"
__copyright__ = "Copyright 2018, python-bseindia"
__license__ = "MIT"
__status__ = "Production"

import unittest

class TestCorporate(unittest.TestCase):
		# Write a common method  for csv validate that provides true/false that asserts tests
	def validate_csv(self):#,filename):
		"""function for validating csv file"""
		# put the code for download csv validation 
		#   self.assertEqual(
        #    read_data(self.data)[0],
        #    ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points']
        #    )
#		if(valid csv):
#			return True
#		else:
		return False

	"""Tests for BSE corporates data"""
	def test_get_listed_securities(self):
		"""Unit test for downloading listed securities in BSE"""
		self.assertTrue(self.validate_csv());
	def test_get_suspended_securities(self):
		"""Unit test for downloading suspended securities in BSE"""
		self.assertTrue(self.validate_csv());
	def test_get_delisted_securities(self):
		"""Unit test for downloading delisted securities in BSE"""
		self.assertTrue(self.validate_csv());

if __name__ == '__main__':
    unittest.main()