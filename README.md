This is a collection of small environments that aid in developing new Machine Learning methods.
They may also help in finding edge cases. If a method works on hard environments but not on simple ones, something may be wrong.

Currently there are two simple environments:
* `mini_discrete_env`: Start at position 0. Go to the right until position x. Then go to the left until position y. Reward is 100 for finishing minus a certain factor that takes into account the number of actions used. Returned observation is the current position and the global state (whether the agent has visited position x yet).
* `mini_continuous_env`: Same as `mini_discrete_env`, but with continuous action/observation space.

Example:

```
import gym
import mini_envs.discrete_envs.mini_discrete_env


env = gym.make('MiniDiscreteEnv-v0')
# The following lines are optional customizations.
env.goal_pos = [3, -3]  # In accordance to above description, first one is x, second one is y.
env.borders = [7, -7]  # Agent won't be able to go beyond borders.
env.max_steps = 100

obs, reward, done, _ = env.step(0)  # Go to the left.
obs, reward, done, _ = env.step(1)  # Go to the right.
```

Install:

`pip3 install -e .`, or:

`pip3 install git+git://github.com/instance01/gym-mini-envs.git`

