"""
    gym-wofost package
    ----------------------------------
    This package contains the gym-wofost environment, which is a wrapper around the WOFOST simulator to be used in reinforcement learning.
"""

__author__ = "Noureddine Ech-chouky"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Noureddine Ech-chouky", "Mohammed Hmimmou", "Hemza Lahkim"]
__license__ = "None"
__version__ = "0.0.8"
__maintainer__ = "Noureddine Ech-chouky"
__email__ = "noureddine.echchouky@um5r.ac.ma"
__status__ = "Development"

# -- Importing general purpose dependencies :
import os
import csv
import warnings
from datetime import datetime
import random
from typing import List, Tuple, Dict, Union, Optional
import time
import numpy as np
from pprint import pprint
import warnings

# -- Importing PCSE dependencies :
from pcse.fileinput import CABOFileReader
from pcse.db import NASAPowerWeatherDataProvider
from pcse.base import ParameterProvider
from pcse.engine import Engine

# -- Importing local dependencies :
from gym_wofost.envs.actions import AgroActions


# -- Wofost simulator init :
class Wofost:
    @staticmethod
    def init_wofost(latitude: float = 51.97, longitude: float = 5.67, **kwargs):
        """Init wofost simulator, by loading the crop,soil and site parameters, also initializing the weather data provider

        ---------------------------------------------------------------------
        :param latitude: latitude of the site(range from -90 to 90)
        :type latitude: int
        :param longitude: longitude of the site(range from -180 to 180)
        :type longitude: int

        ---------------------------------------------------------------------
        :return params : crop,soil and site parameters
        :rtype params : pcse.base.ParameterProvider
        """

        # -- Check if the latitude and longitude are in the correct range :
        if latitude < -90 or latitude > 90:
            warnings.warn(
                "The latitude is not in the correct range, it should be between -90 and 90, the default value is used instead"
            )
        else:
            latitude = latitude
        if longitude < -180 or longitude > 180:
            warnings.warn(
                "The longitude is not in the correct range, it should be between -180 and 180, the default value is used instead"
            )
        else:
            longitude = longitude

        base_dir = os.path.dirname(__file__)
        data_dir = os.path.join(os.path.dirname(__file__), "..", "default_data")

        # -- Loading the crop,soil and site parameters :

        # -- Check if the crop file is provided, if not the default one is used :
        if "crop_file_path" in kwargs:
            crop_file_path = kwargs["crop_file_path"]
            if not os.path.isfile(crop_file_path):
                raise ValueError(
                    "The crop file path is not correct, default will be used instead"
                )
                crop_file_name = "crop.cab"
                cropdata = CABOFileReader(data_dir + "/" + crop_file_name)
            else:
                cropdata = CABOFileReader(crop_file_path)

        # -- Check if the soil file is given, if not the default one will be used :
        if "soil_file_path" in kwargs:
            soil_file_path = kwargs["soil_file_path"]
            if not os.path.isfile(soil_file_path):
                raise ValueError(
                    "The soil file path is not correct, default will be used instead"
                )
                soil_file_name = "soil.cab"
                soildata = CABOFileReader(data_dir + "/" + soil_file_name)
            else:
                soildata = CABOFileReader(soil_file_path)

        # -- Check if the site file is given, if not the default one will be used :
        if "site_file_path" in kwargs:
            site_file_path = kwargs["site_file_path"]
            if not os.path.isfile(site_file_path):
                raise ValueError(
                    "The site file path is not correct, default will be used instead"
                )
                site_file_name = "site.cab"
                sitedata = CABOFileReader(data_dir + "/" + site_file_name)
            else:
                site_data = CABOFileReader(site_file_path)

        # -- replace the wlp_npk config file, with the one provided by the user :
        if "WLP_NPK_file_path" in kwargs:
            WLP_file_path = kwargs["WLP_file_path"]
            if not os.path.isfile(WLP_file_path):
                raise ValueError(
                    "The WLP file path is not correct, default will be used instead"
                )
                config_file_name = "WLP_NPK.cab"
                config = os.path.join(data_dir, config_file_name)
            else:
                config = WLP_file_path

        # -- Init the ParameterProvider : with crop, soil and site parameters
        params = ParameterProvider(cropdata, sitedata, soildata)

        # -- Init the weather data provider :
        wdp = NASAPowerWeatherDataProvider(latitude, longitude)
        return params, wdp, config

    @staticmethod
    def run_wofost(agromanagement, params, wdp, config) -> Tuple[np.array, float]:
        """Run wofost simulator, for a given agromanagement (growing season)

        ---------------------------------------------------------------------
        :param agromanagement : contains the actions template withing wofost format
        :param params : contains the crop,soil and site parameters
        :param wdp : weather data provider
        :param config : wofost configuration file

        ---------------------------------------------------------------------
        :return obs : the observations ndarray
        :return yield : the correspond (yield)
        """
        # -- Init wofost engine : with the given parameters
        wofost = Engine(params, wdp, agromanagement, config)
        # -- Run wofost engine : for the given agromanagement, for growing season
        wofost.run_till_terminate()
        # -- Get the observations : from the wofost engine, summary of the growing season simulation
        r = wofost.get_summary_output()
        # -- Removing variables that are not needed : (neither none or dates)
        for var_ in ["DOS", "DOE", "DOA", "DOM", "DOH", "DOV"]:
            del r[0][var_]
        return (
            # -- Converting the dict to ndarray : (to be used as observations)
            np.array(list(r[0].values())),
            # -- Yield is the last variable in the observations array :
            r[0]["TWSO"],
        )
