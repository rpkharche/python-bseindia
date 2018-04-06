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

""" BSE Indices test
unit tests for getting various indices from BSE like S&P Sensex, S&P BSE SENSEX 50, etc. 
"""
__author__ = "rpkharche@gmail.com(Ravindra Kharche)"
__copyright__ = "Copyright 2018, python-bseindia"
__license__ = "MIT"
__status__ = "Production"

import unittest
import sys 
sys.path.append('.') #pytest mandate
from bselive.Index import LiveIndex
bse_live = LiveIndex()
class TestIndex(unittest.TestCase):
	"""Tests for getting BSE indexes"""
	def test_get_bse_sensex(self):
		"""Unit test for getting S&P BSE SENSEX"""
		index_val = bse_live.get_bse_sensex()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_sensex_50(self):
		"""Unit test for getting S&P BSE SENSEX 50"""
		index_val = bse_live.get_bse_sensex_50()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_sensex_next_50(self):
		"""Unit test for getting S&P BSE SENSEX Next 50"""
		index_val = bse_live.get_bse_sensex_next_50()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_100(self):
		"""Unit test for getting S&P BSE 100"""
		index_val = bse_live.get_bse_100()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_bharat_22(self):
		"""Unit test for getting S&P BSE Bharat 22 Index"""
		index_val = bse_live.get_bse_bharat_22()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_midcap(self):
		"""Unit test for getting S&P BSE MidCap"""
		index_val = bse_live.get_bse_midcap()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_smallcap(self):
		"""Unit test for getting S&P BSE SmallCap"""
		index_val = bse_live.get_bse_smallcap()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_200(self):
		"""Unit test for getting S&P BSE 200"""
		index_val = bse_live.get_bse_200()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_150_midcap(self):
		"""Unit test for getting S&P BSE 150 MidCap Index"""
		index_val = bse_live.get_bse_150_midcap()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_250_smallcap(self):
		"""Unit test for getting S&P BSE 250 SmallCap Index"""
		index_val = bse_live.get_bse_250_smallcap()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_250_largemidcap(self):
		"""Unit test for getting S&P BSE 250 LargeMidCap Index"""
		index_val = bse_live.get_bse_250_largemidcap()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_400_midsmallcap(self):
		"""Unit test for getting S&P BSE 400 MidSmallCap Index"""
		index_val = bse_live.get_bse_400_midsmallcap()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_500(self):
		"""Unit test for getting S&P BSE 500"""
		index_val = bse_live.get_bse_500()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_allcap(self):
		"""Unit test for getting S&P BSE AllCap"""
		index_val = bse_live.get_bse_allcap()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_largecap(self):
		"""Unit test for getting S&P BSE LargeCap"""
		index_val = bse_live.get_bse_largecap()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_smallcapselect(self):
		"""Unit test for getting S&P BSE SmallCap Select Index"""
		index_val = bse_live.get_bse_smallcapselect()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_midcapselect(self):
		"""Unit test for getting S&P BSE MidCap Select Index"""
		index_val = bse_live.get_bse_midcapselect()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_basic_materials(self):
		"""Unit test for getting S&P BSE Basic Materials"""
		index_val = bse_live.get_bse_basic_materials()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_consumer_discretionary_goods_and_services(self):
		"""Unit test for getting S&P BSE Consumer Discretionary Goods & Services"""
		index_val = bse_live.get_bse_consumer_discretionary_goods_and_services()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_energy(self):
		"""Unit test for getting S&P BSE Energy"""
		index_val = bse_live.get_bse_energy()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_fast_moving_consumer_goods(self):
		"""Unit test for getting S&P BSE Fast Moving Consumer Goods"""
		index_val = bse_live.get_bse_fast_moving_consumer_goods()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_finance(self):
		"""Unit test for getting S&P BSE Finance"""
		index_val = bse_live.get_bse_finance()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_healthcare(self):
		"""Unit test for getting S&P BSE Healthcare"""
		index_val = bse_live.get_bse_healthcare()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_industrials(self):
		"""Unit test for getting S&P BSE Industrials"""
		index_val = bse_live.get_bse_industrials()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_information_technology(self):
		"""Unit test for getting S&P BSE Information Technology"""
		index_val = bse_live.get_bse_information_technology()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_telecom(self):
		"""Unit test for getting S&P BSE Telecom"""
		index_val = bse_live.get_bse_telecom()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_utilities(self):
		"""Unit test for getting S&P BSE Utilities"""
		index_val = bse_live.get_bse_utilities()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_auto(self):
		"""Unit test for getting S&P BSE AUTO"""
		index_val = bse_live.get_bse_auto()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_bankex(self):
		"""Unit test for getting S&P BSE BANKEX"""
		index_val = bse_live.get_bse_bankex()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_capital_goods(self):
		"""Unit test for getting S&P BSE CAPITAL GOODS"""
		index_val = bse_live.get_bse_capital_goods()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_consumer_durables(self):
		"""Unit test for getting S&P BSE CONSUMER DURABLES"""
		index_val = bse_live.get_bse_consumer_durables()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_metal(self):
		"""Unit test for getting S&P BSE METAL"""
		index_val = bse_live.get_bse_metal()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_oil_and_gas(self):
		"""Unit test for getting S&P BSE OIL & GAS"""
		index_val = bse_live.get_bse_oil_and_gas()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_power(self):
		"""Unit test for getting S&P BSE POWER"""
		index_val = bse_live.get_bse_power()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_realty(self):
		"""Unit test for getting S&P BSE REALTY"""
		index_val = bse_live.get_bse_realty()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
	def test_get_bse_teck(self):
		"""Unit test for getting S&P BSE TECK"""
		index_val = bse_live.get_bse_teck()
		self.assertTrue(index_val>0)
		self.assertTrue(isinstance(index_val,float))
