import numpy as np
import gym
from gym import spaces


class MiniContinuousEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.pos = 0.
        self.was_right = False

        self.steps = 0

        self.goal_pos = [1., -1.]

        self.action_space = spaces.Box(
            low=-1., high=1., shape=(1,), dtype=np.float32
        )
        self.observation_space = spaces.Box(
            low=-10., high=10., shape=(1,), dtype=np.float32
        )

    def step(self, action):
        if isinstance(action, list):
            action = action[0]

        self.steps += 1

        force = min(max(action, -1.), 1.)
        self.pos += force ** 2 * np.sign(force)

        done = False
        reward = 0
        if self.pos >= self.goal_pos[0]:
            self.was_right = True
        if self.pos <= self.goal_pos[1] and self.was_right:
            reward = 100. - .08 * self.steps ** 1.2
            done = True

        if self.steps > 200:
            done = True

        # TODO Return global state self.was_right too. (POMDP)
        return self.pos, reward, done, {}

    def reset(self):
        self.pos = np.random.random_sample() * 2. - 1
        self.was_right = False
        self.steps = 0
        return self.pos

    def render(self, mode='human', close=False):
        pass
