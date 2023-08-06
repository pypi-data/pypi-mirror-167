import os

from pandas import DataFrame

from client.ml.unitls import get_notebook, get_environment
from client.sdk.watchmen.sdk import load_dataset_by_name, push_notebook_to_watchmen, call_indicator_data_api, \
	load_indicator_by_id, load_achievement_by_id


class WatchmenClient(object):
	def __init__(self, token,host):
		if token:
			self.token = token
		else:
			self.token = os.environ.get('TOKEN')
		self.host = host

	def load_dataset(self, name, dataframe_type="pandas"):
		return load_dataset_by_name(self.token,self.host, name, dataframe_type)

	def load_achievement(self, achievement_id):
		return load_achievement_by_id(self.token,self.host, achievement_id)

	def load_indicator(self, indicator_id):
		return load_indicator_by_id(self.token,self.host, indicator_id)

	def load_indicator_value(self, indicator_id, aggregate_arithmetic, filters):
		payload = {
			"current": {
				"aggregateArithmetic": aggregate_arithmetic,
				"indicatorId": indicator_id,
				"criteria": filters,
				"name": "",
				"variableName": "v2"
			}
		}
		result = call_indicator_data_api(self.token, self.host,payload)
		return result

	def load_summary_data(self):

		## use template report api
		pass

	def register_notebook(self, storage_type="file"):
		notebook = get_notebook(storage_type)
		notebook.environment = get_environment()
		response = push_notebook_to_watchmen(notebook, self.token,self.host)
		if response.status_code == 200:
			print("push notebook successfully")
		return notebook

	def save_topic_dataset(self, topic_name: str, dataset: DataFrame):
		pass

	def register_model(self):
		pass
