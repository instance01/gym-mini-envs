import numpy as np
import gym
from gym import spaces


class MiniDiscreteEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # State
        self.pos = 0
        self.was_right = False
        self.steps = 0

        # Environment
        self.max_steps = 50
        self.borders = [5, -5]
        self.goal_pos = [2, -2]
        self.actions = [0, 1]

        # Compat
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(
            low=self.borders[1],
            high=self.borders[0],
            shape=(2,),
            dtype=np.float32
        )

    def _ensure_action_valid(self, action):
        if isinstance(action, list):
            return np.argmax(action)
        if action == 0:
            return -1
        return action

    def step(self, action):
        action = self._ensure_action_valid(action)

        self.steps += 1
        self.pos += action
        # TODO Use np.clip
        self.pos = min(max(self.pos, self.borders[1]), self.borders[0])

        done = False
        reward = 0
        if self.pos >= self.goal_pos[0]:
            self.was_right = True
        if self.pos <= self.goal_pos[1] and self.was_right:
            reward = 100. - .1 * self.steps ** 1.2
            done = True

        if self.steps > self.max_steps:
            done = True

        # POMDP !! Return whole state for now.
        # Later consider returning a history of self.pos.
        return [self.pos, self.was_right], reward, done, {}

    def reset(self):
        self.pos = 0
        self.was_right = False
        self.steps = 0
        return [self.pos, False]

    def render(self, mode='human', close=False):
        print(self.pos)
