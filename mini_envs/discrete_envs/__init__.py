from gym.envs.registration import register

register(
    id='MiniDiscreteEnv-v0',
    entry_point='mini_envs.discrete_envs.mini_discrete_env:MiniDiscreteEnv',
)
