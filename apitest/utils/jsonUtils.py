#coding:utf-8
import json
import os
class JsonUtils:

	def __init__(self,file_path=None):
		self.file_path = file_path
		self.data = self.read_data()


	def read_data(self):
		'''
		读取json文件
		:return:
		'''
		with open(self.file_path, encoding="utf8") as fp:
			data = json.load(fp)
			return data


	def get_data(self,key, case_id):
		'''

		:param key:
		:param case_id: 测试用例 编号
		:return:
		'''

		test_case =  self.data[case_id - 1]
		return test_case[key]


#for test
if __name__ == '__main__':
	test_file_path = os.path.join( os.path.dirname(__file__) , os.pardir , "data" , "payment.json")
	ju  = JsonUtils(test_file_path)
	print(ju.get_data("test" ,1))

