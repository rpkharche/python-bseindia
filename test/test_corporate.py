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
	def get_file_type(self,filename):
		"""function for getting file type - support xml,csv,txt"""
		with open(filename, 'rb') as fh:
			try:
				xml.sax.parse(fh, xml.sax.ContentHandler()) # try xml parsing 
				fh.close()
				return 'xml'
			except: # SAX' exceptions are not public
				pass
			fh.close()
		with open(filename, 'r') as fh:
			try:
				commacount=0
				count=0
				for line in csv.reader(fh): # try csv parsing 
					if count==0:
						commacount = len(str(line).split(","))
						if commacount>1:
							pass
						else:
							raise csv.Error
					else:
						if commacount == len(str(line).split(",")): # All bse csv are having same number of columns in output
							pass
						else:
							raise csv.Error
					count+=1
				fh.close()
				return 'csv'
			except csv.Error  as e:
				pass
		fh.close()
		return 'txt' # We are not checking for other formats as we dont need them now. 
	"""Tests for BSE corporates data"""
	def test_download_listed_securities(self):
		"""Unit test for downloading listed securities in BSE"""
		#TODO write the code to download the file 
		listed_securities_file=''
		self.assertEqual(self.get_file_type(listed_securities_file), 'csv')
		
	def test_download_suspended_securities(self):
		"""Unit test for downloading suspended securities in BSE"""
		#TODO write the code to download the file 
		suspended_securities_file=''
		self.assertEqual(self.get_file_type(suspended_securities_file), 'csv')
		
	def test_download_delisted_securities(self):
		"""Unit test for downloading delisted securities in BSE"""
		#TODO write the code to download the file 
		delisted_securities_file=''
		self.assertEqual(self.get_file_type(delisted_securities_file), 'csv')

if __name__ == '__main__':
    unittest.main()