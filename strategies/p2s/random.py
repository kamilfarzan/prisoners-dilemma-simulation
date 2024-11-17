from agent import BaseAgent
import random

# 50-50 chance
class p2(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        if random.randint(0,100)>50:
            return 1
        else:
            return -1
        