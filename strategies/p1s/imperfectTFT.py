from agent import BaseAgent
import random

# Imperfect tit for tat
class p1(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        if itr == 1:
            return 1
        elif random.randint(0,100)<99:
            return state["history"][itr - 1][op_id]
        else:
            if state["history"][itr - 1][op_id] == 1:
                return -1
            else:
                return 1