"""
    gym-wofost package
    ----------------------------------
    This package contains the gym-wofost environment, which is a wrapper around the WOFOST simulator to be used in reinforcement learning.
"""

__author__ = "Noureddine Ech-chouky"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Noureddine Ech-chouky", "Mohammed Hmimmou", "Hemza Lahkim"]
__license__ = "None"
__version__ = "1.0.3"
__maintainer__ = "Noureddine Ech-chouky"
__email__ = "noureddine.echchouky@um5r.ac.ma"
__status__ = "Development"

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "1.0.4"
DESCRIPTION = (
    "gym_wofost : A crop growth simulation model turn into OpenAI Gym environment"
)
LONG_DESCRIPTION = "A standard gym environment, built on top of the PCSE library, for the python version of crop growth model WOFOST, to make it easy to train and test latest state of art Reinforcement Learning algorithms."

# Setting up
setup(
    name="gym_wofost",
    version=VERSION,
    author="AgriEdge (Noureddine Ech-chouky)",
    author_email="<noureddine.echchuky@um5r.ac.ma>",
    description=DESCRIPTION,
    package_data={
        "gym_wofost": [
            "default_data/*.cab",
            "default_data/*.yaml",
            "default_data/*.conf",
        ]
    },
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["gym", "PCSE==5.4.2", "shutup"],
    keywords=[
        "python",
        "Reinforcement learning",
        "gym environment",
        "pcse",
        "crop management",
        "precision agriculture",
        "wofost",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
