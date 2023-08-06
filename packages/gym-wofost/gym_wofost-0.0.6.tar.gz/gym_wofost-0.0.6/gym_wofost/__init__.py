from gym.envs.registration import register

register(
    id="wofost-v0",
    entry_point="gym_wofost.envs:WofostEnv"
)
