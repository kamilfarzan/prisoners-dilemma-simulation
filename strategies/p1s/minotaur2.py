from agent import BaseAgent
import random


class p1(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        #ImperfectForgivingTFT
        #pavlov
        #forgivingTFT

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        last_self_move = state["history"][itr-1][self.id]
        last_opp_move = state["history"][itr-1][op_id]
        if itr <= 65:
            if itr == 1 or itr ==2:
                return 1
            elif random.randint(0,100)<99:
                if state["history"][itr-1][op_id]==-1 and state["history"][itr-2][op_id]==-1:
                    return -1
                return 1
            else:
                if state["history"][itr - 1][op_id] == 1:
                    return -1
                else:
                    return 1
        elif itr > 65 and itr <= 130:
            if ((last_self_move == 1) and (last_opp_move == 1)) or ((last_self_move == -1) and (last_opp_move == 1)):
                return last_self_move
            elif ((last_self_move == 1) and (last_opp_move == -1)) or ((last_self_move == -1) and (last_opp_move == -1)):
                if last_self_move == 1:
                    return -1
                else:
                    return 1
        else:
            if state["history"][itr-1][op_id]==-1 and state["history"][itr-2][op_id]==-1:
                return -1
            return 1