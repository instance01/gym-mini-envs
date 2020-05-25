from gym.envs.registration import register

register(
    id='MiniContinuousEnv-v0',
    entry_point='mini_envs.continuous_envs.mini_continuous_env:MiniContinuousEnv',
)
