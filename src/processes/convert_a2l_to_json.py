import os.path

from src.common.a2ltools import read_a2l_static_values, read_a2l_variables
from src.common.json import write_json_file


class ConvertA2lToJson:
    def run(self, a2l_file, json_file):
        static_values = read_a2l_static_values(a2l_file)
        dynamic_values = read_a2l_variables(a2l_file)
        allvalues = {**static_values, **dynamic_values}
        write_json_file(json_file, allvalues)
