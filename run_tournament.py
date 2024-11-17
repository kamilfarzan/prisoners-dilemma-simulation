import os
import subprocess
import json
import sys

def run_tourney():
    result = subprocess.run([sys.executable, 'eval_engine.py'], capture_output=True, text=True)
    output_dict = json.loads(result.stdout)
    last_key = list(output_dict)[-1]
    print(last_key, end=" ")
    return (output_dict[last_key]["score"])

def setPlayers(strat1_path, strat2_path):
    with open(strat1_path, 'r') as strat1_file:
        strat1_code = strat1_file.read()
    with open(strat2_path, 'r') as strat2_file:
        strat2_code = strat2_file.read()

    with open('p1.py', 'w') as f:
        f.write(strat1_code)
    with open('p2.py', 'w') as f:
        f.write(strat2_code)


# loop through files in strategies/p1s and strategies/p2s
# Specify the path to the subdirectory
p1sPath = 'strategies/p1s'
p2sPath = 'strategies/p2s'

# excluded_files = ['agent.py', 'minotaur1.py','minotaur2.py', 'minotaur3.py', 'MS2.py', 'MS1.py', 'newMS.py', 'wrongMS.py', 'wrongMS1.py']
excluded_files = ['agent.py', 'minotaur3.py', 'minotaur4.py', 'MS2.py', 'MS3.py', 'wrongMS.py', 'wrongMS1.py', 'newMS.py']
tournament_results = {}

for strat1 in os.listdir(p1sPath):
    if (strat1 in excluded_files):
        continue
    for strat2 in os.listdir(p2sPath):
        if (strat2 in excluded_files):
            continue
        if (strat1 == strat2):
            continue
        setPlayers(os.path.join(p1sPath, strat1), os.path.join(p2sPath, strat2))
        results = run_tourney()
        print(strat1, strat2, results)
        # add result in dictionary with strat1 as key, results['1'] as value
        if (strat1 not in tournament_results):
            tournament_results[strat1] = results['1']
        else:
            tournament_results[strat1] += results['1']
        
        # add result in dictionary with strat2 as key, results['2'] as value
        if (strat2 not in tournament_results):
            tournament_results[strat2] = results['2']
        else:
            tournament_results[strat2] += results['2']
        # os.path.join(subdirectory_path, filename)

tournament_results = dict(sorted(tournament_results.items(), key=lambda item: item[1], reverse=True))

print("\n")
print(tournament_results)

# # Loop through each file in the subdirectory
# for filename in os.listdir(subdirectory_path):
#     # Construct the full path to the file
#     # file_path = os.path.join(subdirectory_path, filename)
    
#     # # Check if the path is a regular file (not a directory)
#     # if os.path.isfile(file_path):
#     #     # Process the file as needed

#     #     print("File:", file_path)
#     if (filename == "agent.py"):
#         continue
#     print(filename)