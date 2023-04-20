import sys
f = open('input.txt')

DFA = {}

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

print()
for key in DFA.items():
    print(*key)
print()

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