# -- Importing dependencies :
import datetime
import random
from copy import deepcopy
import yaml
from pprint import pprint


def return_apr_dict(action, irrigation_amount, N_amount, P_amount, K_amount):
    """
    return_apr_dict generates action dict, in pcse format

    :action (String) : given agriculture action (eg. irrigate or fertilize)

    :return (tuple of dicts): a : action description, b : action infos

    """
    a, b = None, None
    if action == "irrigate":
        a = {
            "event_signal": "irrigate",
            "name": "Irrigation application table",
            "comment": "All irrigation amounts in cm",
        }
        b = {"amount": irrigation_amount, "efficiency": 0.7}
    if action == "fertilize":
        a = {
            "event_signal": "apply_npk",
            "name": "Timed N/P/K application table",
            "comment": "All fertilizer amounts in kg/ha",
        }
        b = {
            "N_amount": N_amount,
            "P_amount": P_amount,
            "K_amount": K_amount,
            "N_recovery": 0.7,
            "P_recovery": 0.7,
            "K_recovery": 0.7,
        }
    return a, b


def generate_action_dict(
    action,
    periodicity,
    std,
    tot_days,
    seed,
    irrigation_amount,
    N_amount,
    P_amount,
    K_amount,
    cost=0,
):
    """
    generate_action_dict generates the action full dict with events_table, event_signal and comment name

    :action (String) :  eg. irrigate or fertilize
    :periodicity (int) : how much days the action will  apply periodically
    :std (datetime.date) : the starting date of the process
    :tot_days (int) : totale number of days
    :seed (int) : facilitate reproduction
    :cost (float) : the action cost [default : 0]

    :return (dict, float): dicton, tot_cost : wofost formatted action dict, process totale cost

    """

    # periodicity = tot_days

    random.seed(seed)
    dicton, b = return_apr_dict(action, irrigation_amount, N_amount, P_amount, K_amount)
    i = 0
    flag = 0
    tot_cost = 0
    while i <= tot_days:
        if periodicity > 0 and i % periodicity == 0:
            if "events_table" not in dicton:
                dicton["events_table"] = []
            dicton["events_table"].append({std + datetime.timedelta(i): b})
            flag = 1
            tot_cost += cost
        i += 1
    if flag == 1:
        return dicton, tot_cost
    else:
        return None, tot_cost


def gen_agromanager(
    base, dicton, costs, irrigation_amount, N_amount, P_amount, K_amount, seed=5676
):
    """
    gen_agromanager simply generates an agromanager

    :base (yaml config) : agro yaml configuration file
    :dicton (dict) :  periodicity dict  {'fertilize': 15, 'irrigate': 1}
    :dict_costs (float) : costs of actions  {'fertilize': 0, 'irrigate': 0}
    :seed (int) : facilitate reproduction

    :return (tuple):
        tot_costs (float) : the totale cost of the ations,
        aux (list of nasted dicts) : agro_mangaer infos and actions
    """

    aux = deepcopy(base)
    if len(aux) > 1 or len(aux[0]) > 1:
        raise ValueError("base should be a list of one element")
    sd = list(aux[0].keys())[0]
    aux[0][sd]["TimedEvents"] = []
    tot_days = (aux[0][sd]["CropCalendar"]["crop_end_date"] - sd).days
    total_cost = 0
    for action, periodicity in dicton.items():
        res, tot_cost_action = generate_action_dict(
            action,
            periodicity,
            sd,
            tot_days,
            seed,
            irrigation_amount,
            N_amount,
            P_amount,
            K_amount,
            cost=costs[action],
        )
        total_cost += tot_cost_action
        if res is not None:
            aux[0][sd]["TimedEvents"].append(res)
    return aux, total_cost


class AgroActions:
    """
    AgroActions manages all related to agromanagement and actions

    """

    def __init__(self):
        self.actions = None

    def create_actions(
        self,
        periods_irrigation,
        periods_fertilization,
        irrigation_amount,
        N_amount,
        P_amount,
        K_amount,
        year=2017,
    ):
        """
        gen_agromanager simply generates an agromanager

        :periods_irrigation (list) : [0, 1, 4, 7]
        :periods_fertilization (list) : [0, 15]
        :year (int) : correspondante year 2017

        :return (): actions
        """

        self.actions = []
        self.costs = []
        for p in periods_irrigation:
            for f in periods_fertilization:
                agro, cost = self.generate_agromanagement(
                    {"irrigate": p, "fertilize": f},
                    irrigation_amount=irrigation_amount,
                    N_amount=N_amount,
                    P_amount=P_amount,
                    K_amount=K_amount,
                    year=year,
                )
                self.actions.append(agro)
                self.costs.append(cost)
        return self.actions, self.costs

    def generate_agromanagement(
        self, dict_periodicity, irrigation_amount, N_amount, P_amount, K_amount, year
    ):
        """
        generate_agromanagement creates an agromanager

        :dict_periodicity () :
        :year (int) : the correspodante year

        :return ():
        """
        crop_name = "wheat"
        variety_name = "Winter_wheat_101"
        campaign_start_date = str(year) + "-01-01"
        emergence_date = str(year) + "-03-31"
        harvest_date = str(year) + "-08-11"
        max_duration = 300

        agro_yaml = f"""
                - {campaign_start_date}:
                    CropCalendar:
                        crop_name: {crop_name}
                        variety_name: {variety_name}
                        crop_start_date: {emergence_date}
                        crop_start_type: emergence
                        crop_end_date: {harvest_date}
                        crop_end_type: harvest
                        max_duration: {max_duration}
                    TimedEvents: null
                    StateEvents: null
                """

        agromanagement = yaml.safe_load(agro_yaml)
        dict_costs = {"irrigate": 0, "fertilize": 0}  # default : {0, 0}
        agromanagement, cost_advice = gen_agromanager(
            agromanagement,
            dict_periodicity,
            dict_costs,
            irrigation_amount,
            N_amount,
            P_amount,
            K_amount,
        )

        return agromanagement, cost_advice
