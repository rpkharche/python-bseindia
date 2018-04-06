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

import urllib.request

class LiveIndex:
	""" Class to fetch live value of BSE indices
	"""
	
	#Constructor 
	def __init__(self ):
		"""Constructor"""
		# Index codes for BSE indices
		self.BASE_URL = "https://www.bseindia.com/SensexView/SensexViewbackPage.aspx?flag=INDEX&indexcode="
		self.BSE_SENSEX = 16
		self.BSE_500 = 17
		self.BSE_100 = 22
		self.BSE_200 = 23
		self.BSE_CAPITAL_GOODS = 25
		self.BSE_CONSUMER_DURABLES = 27
		self.BSE_METAL = 35
		self.BSE_OIL_N_GAS = 37
		self.BSE_AUTO = 42
		self.BSE_PSU = 44
		self.BSE_TECK = 45
		self.BSE_DOLLEX_30 = 47
		self.BSE_DOLLEX_200 = 48
		self.BSE_BANKEX = 53
		self.BSE_DOLLEX_100 = 65
		self.BSE_REALTY = 67
		self.BSE_POWER = 69
		self.BSE_IPO = 72
		self.BSE_GREENEX = 75
		self.BSE_SME_IPO = 76
		self.BSE_CARBONEX = 77
		self.BSE_India_Infrastructure_Index = 79
		self.BSE_CPSE = 80
		self.BSE_MidCap = 81
		self.BSE_Fast_Moving_Consumer_Goods = 83
		self.BSE_Healthcare = 84
		self.BSE_Information_Technology = 85
		self.BSE_India_Manufacturing_Index = 86
		self.BSE_AllCap = 87
		self.BSE_Basic_Materials = 88
		self.BSE_Consumer_Discretionary_Goods_N_Services = 89
		self.BSE_Energy = 90
		self.BSE_Finance = 91
		self.BSE_Industrials = 92
		self.BSE_LargeCap = 93
		self.BSE_MidCap_Select_Index = 94
		self.BSE_SmallCap_Select_Index = 95
		self.BSE_Telecom = 96
		self.BSE_Utilities = 97
		self.BSE_SENSEX_50 = 98
		self.BSE_SENSEX_Next_50 = 99
		self.BSE_Bharat_22_Index = 100
		self.BSE_100_ESG_Index = 101
		self.BSE_150_MidCap_Index = 102
		self.BSE_250_SmallCap_Index = 103
		self.BSE_250_LargeMidCap_Index = 104
		self.BSE_400_MidSmallCap_Index = 105
		self.BSE_Dividend_Stability_Index = 106
		self.BSE_Enhanced_Value_Index = 107
		self.BSE_Low_Volatility_Index = 108
		self.BSE_Momentum_Index = 109
	def get_value_from_url(self,indexcode):
		"""Method for getting Index from combination of base URL and Index Code"""
		returnval = 0
		target_url = self.BASE_URL + str(indexcode); # Generate the Target URL #TODO PERF - join is faster than + on strings
		# Submit Request to BSE Server
		# SAMPLE Response - bseindia$#$BSE30@S&P_BSE_SENSEX@33608.59@33697.51@33501.37@33626.97@33596.80@30.17@0.09@06_Apr_2018_|_15:59_@2
		with urllib.request.urlopen(target_url) as f:
			tokens = f.read().decode("utf-8").split("@")
			returnval = tokens[5] # Live Value is at 6th position in string. 
		return returnval
	def get_bse_sensex(self):
		"""Method for getting S&P BSE SENSEX"""
		return self.get_value_from_url(self.BSE_SENSEX)
	def get_bse_sensex_50():
		"""Method for getting S&P BSE SENSEX 50"""
		return self.get_value_from_url(self.BSE_SENSEX_50)
	def get_bse_sensex_next_50():
		"""Method for getting S&P BSE SENSEX Next 50"""
		return self.get_value_from_url(self.BSE_SENSEX_Next_50)
	def get_bse_100():
		"""Method for getting S&P BSE 100"""
		return self.get_value_from_url(self.BSE_100)
	def get_bse_bharat_22():
		"""Method for getting S&P BSE Bharat 22 Index"""
		return self.get_value_from_url(self.BSE_Bharat_22_Index)
	def get_bse_midcap():
		"""Method for getting S&P BSE MidCap"""
		return self.get_value_from_url(self.BSE_MidCap)
	def get_bse_smallcap():
		"""Method for getting S&P BSE SmallCap"""
		return self.get_value_from_url(self.BSE_SmallCap)
	def get_bse_200():
		"""Method for getting S&P BSE 200"""
		return self.get_value_from_url(self.BSE_200)
	def get_bse_150_midcap():
		"""Method for getting S&P BSE 150 MidCap Index"""
		return self.get_value_from_url(self.BSE_150_MidCap_Index)
	def get_bse_250_smallcap():
		"""Method for getting S&P BSE 250 SmallCap Index"""
		return self.get_value_from_url(self.BSE_250_SmallCap_Index)
	def get_bse_250_largemidcap():
		"""Method for getting S&P BSE 250 LargeMidCap Index"""
		return self.get_value_from_url(self.BSE_250_LargeMidCap_Index)
	def get_bse_400_midsmallcap():
		"""Method for getting S&P BSE 400 MidSmallCap Index"""
		return self.get_value_from_url(self.BSE_400_MidSmallCap_Index)
	def get_bse_500():
		"""Method for getting S&P BSE 500"""
		return self.get_value_from_url(self.BSE_500)
	def get_bse_allcap():
		"""Method for getting S&P BSE AllCap"""
		return self.get_value_from_url(self.BSE_AllCap)
	def get_bse_largecap():
		"""Method for getting S&P BSE LargeCap"""
		return self.get_value_from_url(self.BSE_LargeCap)
	def get_bse_smallcapselect():
		"""Method for getting S&P BSE SmallCap Select Index"""
		return self.get_value_from_url(self.BSE_SmallCap_Select_Index)
	def get_bse_midcapselect():
		"""Method for getting S&P BSE MidCap Select Index"""
		return self.get_value_from_url(self.BSE_MidCap_Select_Index)
	def get_bse_basic_materials():
		"""Method for getting S&P BSE Basic Materials"""
		return self.get_value_from_url(self.BSE_Basic_Materials)
	def get_bse_consumer_discretionary_goods_and_services():
		"""Method for getting S&P BSE Consumer Discretionary Goods & Services"""
		return self.get_value_from_url(self.BSE_Consumer_Discretionary_Goods_N_Services)
	def get_bse_energy():
		"""Method for getting S&P BSE Energy"""
		return self.get_value_from_url(self.BSE_Energy)
	def get_bse_fast_moving_consumer_goods():
		"""Method for getting S&P BSE Fast Moving Consumer Goods"""
	def get_bse_finance():
		"""Method for getting S&P BSE Finance"""
		return self.get_value_from_url(self.BSE_Finance)
	def get_bse_healthcare():
		"""Method for getting S&P BSE Healthcare"""
		return self.get_value_from_url(self.BSE_Healthcare)
	def get_bse_industrials():
		"""Method for getting S&P BSE Industrials"""
		return self.get_value_from_url(self.BSE_Industrials)
	def get_bse_information_technology():
		"""Method for getting S&P BSE Information Technology"""
		return self.get_value_from_url(self.BSE_Information_Technology)
	def get_bse_telecom():
		"""Method for getting S&P BSE Telecom"""
		return self.get_value_from_url(self.BSE_Telecom)
	def get_bse_utilities():
		"""Method for getting S&P BSE Utilities"""
		return self.get_value_from_url(self.BSE_Utilities)
	def get_bse_auto():
		"""Method for getting S&P BSE AUTO"""
		return self.get_value_from_url(self.BSE_AUTO)
	def get_bse_bankex():
		"""Method for getting S&P BSE BANKEX"""
		return self.get_value_from_url(self.BSE_BANKEX)
	def get_bse_capital_goods():
		"""Method for getting S&P BSE CAPITAL GOODS"""
		return self.get_value_from_url(self.BSE_CAPITAL_GOODS)
	def get_bse_consumer_durables():
		"""Method for getting S&P BSE CONSUMER DURABLES"""
		return self.get_value_from_url(self.BSE_CONSUMER_DURABLES)
	def get_bse_metal():
		"""Method for getting S&P BSE METAL"""
		return self.get_value_from_url(self.BSE_METAL)
	def get_bse_oil_and_gas():
		"""Method for getting S&P BSE OIL & GAS"""
		return self.get_value_from_url(self.BSE_OIL_N_GAS)
	def get_bse_power():
		"""Method for getting S&P BSE POWER"""
		return self.get_value_from_url(self.BSE_POWER)
	def get_bse_realty():
		"""Method for getting S&P BSE REALTY"""
		return self.get_value_from_url(self.BSE_REALTY)
	def get_bse_teck():
		"""Method for getting S&P BSE TECK"""
		return self.get_value_from_url(self.BSE_TECK)
	
# Main Section for trial run	
if __name__== "__main__":
	bse_live = LiveIndex()
	print(bse_live.get_bse_sensex())
	
'''
return self.get_value_from_url(self.BSE_PSU)
return self.get_value_from_url(self.BSE_DOLLEX_30)
return self.get_value_from_url(self.BSE_DOLLEX_200)
return self.get_value_from_url(self.BSE_DOLLEX_100)
return self.get_value_from_url(self.BSE_IPO)
return self.get_value_from_url(self.BSE_GREENEX)
return self.get_value_from_url(self.BSE_SME_IPO)
return self.get_value_from_url(self.BSE_CARBONEX)
return self.get_value_from_url(self.BSE_India_Infrastructure_Index)
return self.get_value_from_url(self.BSE_CPSE)
return self.get_value_from_url(self.BSE_Fast_Moving_Consumer_Goods)
return self.get_value_from_url(self.BSE_India_Manufacturing_Index)
return self.get_value_from_url(self.BSE_100_ESG_Index)
return self.get_value_from_url(self.BSE_Dividend_Stability_Index)
return self.get_value_from_url(self.BSE_Enhanced_Value_Index)
return self.get_value_from_url(self.BSE_Low_Volatility_Index)
return self.get_value_from_url(self.BSE_Momentum_Index)'''