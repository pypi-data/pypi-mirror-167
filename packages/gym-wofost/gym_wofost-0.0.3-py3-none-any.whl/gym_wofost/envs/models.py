# -- Importing dependencies :
import os.path
import math
from math import exp, log, sqrt
import csv
import warnings
from datetime import datetime
import random
import time
import numpy as np
from pprint import pprint

from pcse.fileinput import CABOFileReader
from pcse.db import NASAPowerWeatherDataProvider
from pcse.base import ParameterProvider
from pcse.engine import Engine

from gym_wofost.envs.actions import AgroActions


# -- Wofost simulator init :
class Wofost:
    @staticmethod
    def init_wofost():
        """
        Init wofost simulator
        """
        base_dir = os.path.dirname(__file__)
        data_dir = os.path.join(os.path.dirname(__file__), "default_data")
        crop_file_name = "crop.cab"
        soil_file_name = "soil.cab"
        site_file_name = "site.cab"
        config_file_name = "WLP_NPK.conf"

        soildata = CABOFileReader(data_dir + "/" + soil_file_name)
        sitedata = CABOFileReader(data_dir + "/" + site_file_name)
        cropdata = CABOFileReader(data_dir + "/" + crop_file_name)
        # config = os.path.join(data_dir, config_file_name)
        config = data_dir + "/" + "WLP_NPK.conf"

        params = ParameterProvider(cropdata, sitedata, soildata)
        latitude, longitude = 51.97, 5.67
        wdp = NASAPowerWeatherDataProvider(latitude, longitude)

        return params, wdp, config

    # -- Note : change this to daily basis
    @staticmethod
    def run_wofost(agromanagement, params, wdp, config):
        """Run wofost simulator, for a given agromanagement (growing season)

        Args:
            agromanagement (list): contains the actions template withing wofost format
            params (_type_): _description_
            wdp (_type_): _description_
            config (_type_): _description_

        Returns:
            the observations ndarray, reward (yield)
        """
        wofost = Engine(params, wdp, agromanagement, config)
        wofost.run_till_terminate()
        r = wofost.get_summary_output()
        for var_ in ["DOS", "DOE", "DOA", "DOM", "DOH", "DOV"]:
            del r[0][var_]
        return (
            np.array(list(r[0].values())),
            # r,
            r[0]["TWSO"],
        )
