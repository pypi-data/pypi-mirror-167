import numpy as np
import pandas as pd
import re

def set_library(txtfile):
	try:
		with open(txtfile, 'r', encoding='euc-kr') as file:
			text_list = file.readlines()
	except:
		with open(txtfile, 'r', encoding='utf-8') as file:
			text_list = file.readlines()

	# 금융규제운영규정 판다스 시리즈로 사전 구축
	srs = pd.Series(text_list, name='sentence')

	srs = srs.map(lambda x: x.replace('\n',''))
	mapping = srs.map(lambda x: False if x == '' else True)
	srs = srs[mapping]
	srs.reset_index(drop=True, inplace=True)

	return srs

def get_sentence_kw(srs, kw):

	def find_kw(pool, kw):
		if kw in pool:
			dummy = re.findall(kw, pool)
			result = ','.join(dummy)
			return result
		else:
			return None

	sec_col = srs.apply(find_kw, kw=kw)
	srs_df = pd.concat([srs, sec_col], axis=1)
	srs_df.columns = ['sentence', 'keyword']
	# print(srs_df.isnull().sum())
	srs_df.dropna(inplace=True)

	return srs_df

def get_csv(df, csv_name):
	df.to_csv(csv_name, index=False)