from random import random, choice
from typing import List
class Environment:
    """An environment that assigns a random reward regardless of an agent's actions
    """
    def __init__(self):
        self.steps_left = 10 # internal state
    def get_observation(self) -> List[float]:
        return [0.0, 0.0, 0.0]
    def get_actions(self) -> List[int]:
        return [0, 1]
    def is_done(self) -> bool:
        return self.steps_left == 0
    def action(self, action: int) -> float:
        if self.is_done():
            raise Exception('Game is over')
        self.steps_left -= 1
        return random()

class Agent:
    """An agent that receives a random reward regardless of their actions
    """
    def __init__(self):
        self.total_reward = 0.0
    def step(self, env:Environment):
        current_observation = env.get_observation()
        actions = env.get_actions()
        reward = env.action(choice(actions))
        self.total_reward += reward

if __name__ == '__main__':
    env = Environment()
    agent = Agent()
    while not env.is_done():
        agent.step(env)
    print('Total reward got: %.4f' % agent.total_reward)

