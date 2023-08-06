# -- Importing dependencies :
import gym
from gym import spaces
import numpy as np
from gym_wofost.envs.models import Wofost  #
from gym_wofost.envs.actions import AgroActions
from gym_wofost.envs.reward import calculate_reward

# -- To add the external folders modules :
import sys

sys.path.append("..")

# -- Importing optional dependenciees :
import random
import time
from pprint import pprint


import shutup

shutup.please()


# -- To ignore deprecation warning
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

# -- Gym Registration depending on the version :
from gym import error, spaces, utils
from gym.utils import seeding


# -------------- normalize and denormalize irrigation action (0.0, 20.0) -------------------
def normalize_irrigation_action(action):
    """Normalize the action from [low, high] to [-1, 1]"""
    low, high = 0.0, 20.0
    return 2.0 * ((action - low) / (high - low)) - 1.0


def denormalize_irrigation_action(action):
    """Denormalize the action from [-1, 1] to [low, high]"""
    low, high = 0.0, 20.0
    return low + (0.5 * (action + 1.0) * (high - low))


# -------------------------------------------------------------------------------------------

# -------------- normalize and denormalize fertilization actions (0.0, 200.0) -------------------
def normalize_fertilization_action(action):
    """Normalize the action from [low, high] to [-1, 1]"""
    low, high = 0.0, 200.0
    return 2.0 * ((action - low) / (high - low)) - 1.0


def denormalize_fertilization_action(action):
    """Denormalize the action from [-1, 1] to [low, high]"""
    low, high = 0.0, 200.0
    return low + (0.5 * (action + 1.0) * (high - low))


# -------------------------------------------------------------------------------------------

# -------------- normalize and denormalize frequencies  (0, 223) -------------------
def normalize_ferquencies_action(action):
    """Normalize the action from [low, high] to [-1, 1]"""
    low, high = 0.0, 223.0
    return 2.0 * ((action - low) / (high - low)) - 1.0


def denormalize_frequencies_action(action):
    """Denormalize the action from [-1, 1] to [low, high]"""
    low, high = 0.0, 223.0
    return low + (0.5 * (action + 1.0) * (high - low))


# -------------------------------------------------------------------------------------------


class WofostEnv(gym.Env):
    """Custom Environment that follows gym interface"""

    metadata = {"render.modes": ["human"]}

    def __init__(
        self,
        years_count=2,
        Costs_dict={"Irrigation": 150, "N": 8, "P": 8.5, "K": 7, "Selling": 2.5},
        Discount_factors_dict={"Irrigation": 1, "N": 1, "P": 1, "K": 1},
        year=2019,
    ):
        """
        Initialization of the env : action and observation space

            *  observation space :
                    SUMMARY_OUTPUT_VARS = ["DVS","LAIMAX","TAGP", "TWSO", "TWLV", "TWST",
                            "TWRT", "CTRAT", "RD", "DOS", "DOE", "DOA",
                            "DOM", "DOH", "DOV"]
            * In recommendation system logic : we need yield as output not input

        """
        super(WofostEnv, self).__init__()

        self.info = {}

        self.year = year
        self.years_count = years_count
        self.years_count_max = years_count
        self.Costs_dict = Costs_dict
        self.Discount_factors_dict = Discount_factors_dict
        self.seed = 0

        # -- Obsrevation space :
        self.OUTPUT_VARS = [
            "DVS",
            "LAIMAX",
            "TAGP",
            "TWSO",
            "TWLV",
            "TWST",
            "TWRT",
            "CTRAT",
            "RD",
        ]

        # -- Mono-Action for now :
        self.n_actions = 6
        # -- Init the yield vector : state
        self.state = np.zeros(len(self.OUTPUT_VARS))

        # -- Init wofost and keep its parameters (for running wofost)
        params, wdp, config = Wofost.init_wofost()
        self.wofost_params = [params, wdp, config]

        # -- Irrigation amount :
        self.action_space = spaces.Box(
            low=np.array([-1, -1, -1, -1, -1, -1]),
            high=np.array([1, 1, 1, 1, 1, 1]),
            shape=(self.n_actions,),
            dtype="float64",
        )

        # -- yeild :
        self.observation_space = spaces.Box(
            low=0.0, high=np.inf, shape=self.state.shape, dtype="float64"
        )
        # -- avoid the problem with the monitor when the things are none :
        self.last_info = {}
        self.last_obs = None

    def set_args(
        self,
        args={
            "years_count": 2,
            "Costs_dict": {"Irrigation": 150, "N": 8, "P": 8.5, "K": 7, "Selling": 2.5},
            "Discount_factors_dict": {"Irrigation": 1, "N": 1, "P": 1, "K": 1},
            "year": 2019,
        },
    ):
        """
        Set the args
        """
        self.years_count_max = args["years_count"]
        for key, value in args.items():
            setattr(self, key, value)

    def step(self, action):
        """
        1. sample a year, and discount the years_count
        2. create action with the **action** irrigation amount, (fertilization_amount)
        # 3. run wofost and get the correspondent state variables (yield included),
        4. get the reward  (for now its the yield)
        """

        # -- sample a year with the full weather data :
        # year = self.sample_random_year()
        year = self.year
        print("years_count: ", self.years_count)

        self.years_count -= 1

        irrigation_action = denormalize_irrigation_action(action[0])
        N_amount = denormalize_fertilization_action(action[1])
        P_amount = denormalize_fertilization_action(action[2])
        K_amount = denormalize_fertilization_action(action[3])
        irrigation_freq = int(denormalize_frequencies_action(action[4]))
        fertilization_freq = int(denormalize_frequencies_action(action[5]))

        # de_action = action
        # print(
        #     f"----------- de action in step : -------------\n{[irrigation_action, N_amount, P_amount, K_amount, irrigation_freq, fertilization_freq]}\n"
        # )
        # Add a parameter here that specifies the irrigation amount : our solo action for now
        # print(type(de_action[0]))
        self.actions, _ = AgroActions().create_actions(
            [irrigation_freq],
            [fertilization_freq],
            irrigation_amount=irrigation_action,
            N_amount=N_amount,
            P_amount=P_amount,
            K_amount=K_amount,
            year=year,
        )

        # Run Wofost to obtain yield for each action : ** one action for now **
        # pprint(f"----------- action in run : {self.actions[0]} -------------\n")
        # pprint(f"----------- len actions : {len(self.actions)} -------------\n")

        self.state, Yield = Wofost.run_wofost(self.actions[0], *self.wofost_params)

        # -- Modification Date and Hour : 30.08.2022 : 4.03
        self.reward = calculate_reward(
            Yield,
            irrigation_action,
            N_amount,
            P_amount,
            K_amount,
            Costs_dict=self.Costs_dict,
            Discount_factors_dict=self.Discount_factors_dict,
        )

        # pprint(f"----------- state in run : {self.state} -------------\n")

        info = {}

        # -- Implement done logic : Important :
        if self.years_count == 0:
            done = True
        else:
            done = False

        return self.state, self.reward, done, self.info

    def reset(self):
        """
        1. Reset the state,
        2. Reset the Simulation length
        """
        # -- Reset the state :
        self.state = np.zeros(len(self.OUTPUT_VARS))
        # -- Reset the years count :
        self.years_count = self.years_count_max

        return self.state  # reward, done, info can't be included

    def render(self, mode="human", close=False):
        """
        Implement a visualization
        """
        pass

    def close(self):
        """
        Close the env
        """
        pass
