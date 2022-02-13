"""classic Acrobot simulator
"""

import gym

class AcrobotWithoutVelocity(gym.Env):
    def __post_init__(self):
        self.env = gym.make('Acrobot-v1')

    def __getattr__(self, *args):
        return self.env.__getattr__(*args)

    def step_only_angles(self):
        """return only sin&cos of theta1&theta2
        """
        observation, reward, terminal, info = self.env.step(a)
        yield observation[:4], reward, terminal, info
        self.env.reset()
