from agent import BaseAgent

# tit for tat
class p2(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        if itr == 1:
            return -1
        if itr == 2:
            if state["history"][1][op_id] == -1:
                return 1
            if state["history"][1][op_id] == 1:
                return -1
        if itr==3:
            return 1
        if itr == 4:
            return -1
        if state["history"][1][op_id] == -1 and state["history"][2][op_id]==-1 and state["history"][3][op_id] == -1 and state["history"][4][op_id]==-1:
            return -1
        elif state["history"][1][op_id] == 1 and state["history"][2][op_id]==1 and state["history"][3][op_id] == 1 and state["history"][4][op_id]==1:
            return -1
        elif state["history"][1][op_id] == 1 and state["history"][2][op_id] == 1 and state["history"][3][op_id] == 1 and state["history"][4][op_id] == -1:
            if state["current_iter"] % 2 == 0:
                return -1
            else:
                return 1
        else:
            return 1