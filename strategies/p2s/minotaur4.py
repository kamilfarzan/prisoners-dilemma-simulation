from agent import BaseAgent
import random

# tit for tat
class p2(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        #forgivingTFT
        #pavlov
        #random
        #grim

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        last_self_move = state["history"][itr-1][self.id]
        last_opp_move = state["history"][itr-1][op_id]
        if itr <= 50:
            if state["history"][itr-1][op_id]==-1 and state["history"][itr-2][op_id]==-1:
                return -1
            return 1
        elif itr > 50 and itr <= 100:
            if ((last_self_move == 1) and (last_opp_move == 1)) or ((last_self_move == -1) and (last_opp_move == 1)):
                return last_self_move
            elif ((last_self_move == 1) and (last_opp_move == -1)) or ((last_self_move == -1) and (last_opp_move == -1)):
                if last_self_move == 1:
                    return -1
                else:
                    return 1
        elif itr>100 and itr<150:
            if random.randint(0,100) > 50:
                return 1
            else:
                return -1
        elif itr>150:
            if (state["history"][itr - 1][op_id] == -1) or (state["history"][itr - 1][self.id] == -1):
                return -1
            return 1