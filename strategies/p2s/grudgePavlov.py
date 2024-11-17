from agent import BaseAgent

# tit for tat
class p2(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        # SUCCESS: (coop, coop) or (def, coop)
        # DEFEAT:  (coop, def)  or (def, def)
        last_self_move = state["history"][itr-1][self.id]
        last_opp_move = state["history"][itr-1][op_id]
        
        if itr > 4:
            if (state["history"][itr-1][op_id] == -1 and state["history"][itr-2][op_id] == -1 and state["history"][itr-3][op_id] == -1 and state["history"][itr-4][op_id] == -1):
                return -1

        if itr == 1:
            return 1
        elif ((last_self_move == 1) and (last_opp_move == 1)) or ((last_self_move == -1) and (last_opp_move == 1)):
            return last_self_move
        elif ((last_self_move == 1) and (last_opp_move == -1)) or ((last_self_move == -1) and (last_opp_move == -1)):
            if last_self_move == 1:
                return 1
            else:
                return -1