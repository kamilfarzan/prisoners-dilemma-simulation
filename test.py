import math
import random
COOP = 1
DEFECT = -1
is_err1 = False
is_err2 = False
move_queue = [0, 0]
streak = 0
history = {}
iteration = 1
rounds = 100
time_limit = 1
error = 0.1
payoff_matrx = [
    [3, 0],
    [5, 1],
    [1, 1]
]
score = [0, 0, 0]


error = 0.05
is_err1 = random.random() < error
is_err2 = random.random() < error

if move_queue[0] == COOP and move_queue[1] == COOP:
    streak += 1
elif move_queue[0] == DEFECT and move_queue[1] == COOP:
    streak = math.ceil(streak / 2) if (is_err1 or is_err2) else 0
elif move_queue[0] == COOP and move_queue[1] == DEFECT:
    streak = math.ceil(streak / 2) if (is_err1 or is_err2) else 0
else:
    streak = math.ceil(streak / 2) if (is_err1 and is_err2) else 0