import json
import numpy as np


class Curriculum(object):
    def __init__(self, location):
        with open(location) as data_file:
            self.data = json.load(data_file)

    def get_lesson(self, progress):
        if progress < np.max(self.data['thresholds']):
            index = np.where(progress <= np.array(self.data['thresholds']))[0][0]
        else:
            index = self.data['thresholds'].index(self.data['thresholds'][-1])
        config = {}
        parameters = self.data["parameters"]
        for key in parameters:
            config[key] = parameters[key][index]
        return config
