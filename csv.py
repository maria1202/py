from pandas import read_csv
import matplotlib.pyplot as plt
from pandas import DataFrame
import json

log_file = 'stat_log.csv'


def read_csv_file(input_file):
	return read_csv(log_file)

def get_parameter_list(data):
	return list(data.columns.values)

def draw_graphics(input_file):
	data = read_csv_file(input_file)
	pl = get_parameter_list(data)
	for param in pl[1 : -1]:
		data.plot(x = pl[0], y = param, title = param, color = 'blue', figsize = (15,6))
		plt.savefig('graph_' + param)
		plt.close()

def create_metrics_file(input_file):
	data = read_csv_file(input_file)
	pl = get_parameter_list(data)
	param_values = data.describe()
	dict_param = {}
	for param in pl[1 : -1]:
		dict_param[param] = {"min" : param_values.get_value('min', param), 
					"avg" : param_values.get_value('mean', param),
					"max" : param_values.get_value('max', param),
					"median" : param_values.get_value('50%', param),
					"std_dev" : param_values.get_value('std', param) }
	create_json_file(dict_param, 'metrics.json')

def create_json_file(dict_in, filename):
	with open(filename, 'w') as outfile:
		json.dump(dict_in, outfile, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == "__main__":
	draw_graphics(log_file)
	create_metrics_file(log_file)