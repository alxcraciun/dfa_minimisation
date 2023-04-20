def merge_states(state1, state2):
    # Replace all occurences of state2 with state1 in table_finals
    for state in table_finals:
        for letter in alphabet:
            if table_finals[state].get(letter) == state2:
                table_finals[state][letter] = state1
    # Replace all occurences of state2 with state1 in table_nonfinals
    for state in table_nonfinals:
        for letter in alphabet:
            if table_nonfinals[state].get(letter) == state2:
                table_nonfinals[state][letter] = state1


def try_merging(table):
    for state1 in table.keys():
        for state2 in table.keys():
            if table[state1] == table[state2] and state1 != state2:
                table.pop(state2)
                merge_states(state1, state2)
                try_merging(table)
                return

DFA = {}
f = open('input.txt')

start_state = f.readline()
start_state = start_state.strip()
final_states = f.readline()
final_states = [elem.strip() for elem in final_states.split()]
alphabet = set()
all_states = set()

for line in f:
    table = [elem.strip() for elem in line.split()]
    all_states.add(table[0])
    all_states.add(table[2])
    alphabet.add(table[1])
    if DFA.get(table[0]) == None:
        DFA[table[0]] = {}
    DFA[table[0]].update({table[1]: table[2]})
f.close()

# Find reachable states
reachable_states = set()
reachable_states.add(start_state)

new_elements = True
while new_elements == True:
    new_elements = False
    aux = reachable_states.copy()
    for letter in alphabet:
        for state in reachable_states:
            if DFA[state][letter] not in reachable_states:
                aux.add(DFA[state][letter])
                new_elements = True
    reachable_states = aux.copy()

# Remove unreachable states
for elem in all_states.difference(reachable_states):
    DFA.pop(elem, None)

# Create transition tables
table_finals = {state: {letter: DFA[state][letter] for letter in alphabet}
                for state in DFA.keys() if state in final_states}
table_nonfinals = {state: {letter: DFA[state][letter] for letter in alphabet}
                   for state in DFA.keys() if state not in final_states}

try_merging(table_finals)
try_merging(table_nonfinals)

table = table_finals | table_nonfinals

print()
for key in DFA.items():
    print(*key)

print()

for key in table.items():
    print(*key)
print()

''' input.txt presentation
0 
5
0 1 2 
0 0 1
1 0 0
1 1 3
2 0 5
2 1 4
3 1 4
3 0 5
4 0 4 
4 1 4
5 0 5
5 1 4
'''

''' input.txt PDF
0 
6
0 a 1 
0 b 3
1 b 2
1 a 3
2 b 2
2 a 3
3 a 6
3 b 5
4 a 6
4 b 5
5 b 2
5 a 6
6 a 4
6 b 5
'''

''' input.txt https://www.javatpoint.com/minimization-of-dfa
0 
3 5
0 0 1
0 1 3
1 1 3
1 0 0
2 1 4 
2 0 1
3 0 5
3 1 5
5 0 5
5 1 5
4 0 3
4 1 3
'''
