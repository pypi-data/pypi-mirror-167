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


# -- Read Cabo file :
def read_cabo_file(cabo_file_path: str) -> CABOFileReader:
    """Read the cabofile and return it as a CABOFileReader object

    ---------------------------------------------------------------------
    :param cabo_file_path: The path to the cabo file
    :type cabo_file_path: str

    ---------------------------------------------------------------------
    :return: The cabofile as a CABOFileReader object
    :rtype: CABOFileReader
    """
    return CABOFileReader(cabo_file_path)


# -- Check if the file path is valid :
def check_file_path(file_path: str) -> bool:
    """Check if the file path is valid

    ---------------------------------------------------------------------
    :param file_path: The path to the file
    :type file_path: str

    ---------------------------------------------------------------------
    :return: True if the file path is valid, False otherwise
    :rtype: bool
    """
    if os.path.isfile(file_path):
        return True
    else:
        raise ValueError("The file path is not valid, default will be used instead")
        return False


# -- Check if the crop file is provided, if not the default one is used :
def check_cabo_file(param_name: str, kwargs: dict) -> CABOFileReader:
    """Check if the crop file is provided, if not the default one is used

    ---------------------------------------------------------------------
    :param param_name: The name of the parameter to check (eg. "crop", "site" or "soil")
    :type param_name: str
    :param kwargs: The dictionary of parameters
    :type kwargs: dict

    ---------------------------------------------------------------------
    :return: The cabo file as a CABOFileReader object
    :rtype: CABOFileReader
    """
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(os.path.dirname(__file__), "..", "default_data")

    if f"{param_name}_file_path" not in kwargs or (
        f"{param_name}_file_path" in kwargs
        and not check_file_path(kwargs[f"{param_name}_file_path"])
    ):
        para_file_path = os.path.join(data_dir, f"{param_name}.cab")
        para_data = read_cabo_file(para_file_path)
    else:
        para_file_path = kwargs["crop_file_path"]
        para_data = read_cabo_file(para_file_path)

    return para_data


# -- Check if the config file path is provided, if not the default one is used :
def check_config_file(kwargs: dict) -> str:
    """Check if the config file path is provided, if not the default one is used

    ---------------------------------------------------------------------
    :param kwargs: The dictionary of parameters
    :type kwargs: dict

    ---------------------------------------------------------------------
    :return: The path to the config file
    :rtype: str
    """
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(os.path.dirname(__file__), "..", "default_data")

    if "config_file_path" not in kwargs or (
        f"config_file_path" in kwargs
        and not check_file_path(kwargs["config_file_path"])
    ):
        config_file_path = os.path.join(data_dir, "WLP_NpPK.conf")
    else:
        config_file_path = kwargs["config_file_path"]

    return config_file_path


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

        # -- Cabo files list :
        cabo_files = ["crop", "soil", "site"]
        data_ = []
        for file in enumerate(cabo_files):
            data_.append(check_cabo_file(file, kwargs))
        data_zip = zip(cabo_files, data_)

        # -- replace the wlp_npk config file, with the one provided by the user :
        config = check_config_file(kwargs)

        # -- Init the ParameterProvider : with crop, soil and site parameters
        params = ParameterProvider(
            data_zip["crop"], data_zip["soil"], data_zip["site"], config
        )

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
