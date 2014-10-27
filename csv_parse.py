#!/usr/bin/env python
 
 
from pandas import read_csv
import matplotlib.pyplot as plt
#from pandas import DataFrame
import sys
import json
 
#LOG_FILE= 'stat_log.csv'
#file_name = 'metrics.json'
 
def read_csv_file(input_file):
    return read_csv(input_file)
 
def get_parameter_list(data):
    return list(data.columns.values)
 
def draw_graphics(data):
    pl = get_parameter_list(data)
    for param in pl[1 : -1]:
        data.plot(x = pl[0], y = param, title = param, figsize = (15,6))
        plt.savefig(param)
        plt.close()
 
def create_metrics_file(data, output_file_name):
    pl = get_parameter_list(data)
    param_values = data.describe()
    dict_param = {}
    for param in pl[1:-1]:
        dict_param[param] = {"min" : param_values.get_value('min', param), 
                    "avg" : param_values.get_value('mean', param),
                    "max" : param_values.get_value('max', param),
                    "median" : param_values.get_value('50%', param),
                    "std_dev" : param_values.get_value('std', param) }
    create_json_file(dict_param, output_file_name)
 
def create_json_file(dict_in, filename):
    with open(filename, 'w') as outfile:
        json.dump(dict_in, outfile, sort_keys=True, indent=4, separators=(',', ': '))
 
if __name__ == "__main__":
    if (len(sys.argv) != 3 ):
        print "Usage details: task.py <csv_log_file_name> <output_json_file_name>"
        sys.exit
    else:
        data_frame = read_csv_file(sys.argv[1])
        draw_graphics(data_frame)
        create_metrics_file(data_frame, sys.argv[2])
