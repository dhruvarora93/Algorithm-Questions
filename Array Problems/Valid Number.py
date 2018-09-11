def is_number(s):
    state = [{},
             {'blank':1,'digit':2,'sign':3,'.':4},
             {'digit':2,'e':6,'blank':9,'.':5},
             {'digit':2,'.':4},
             {'digit':5},
             {'digit':5,'blank':9,'e':6},
             {'sign':7,'digit':8},
             {'digit':8},
             {'digit':8,'blank':9},
             {'blank':9}]

    current_state = 1
    for char in s:
        if char == ' ':
            char = 'blank'
        if '0' <= char <= '9':
            char = 'digit'
        if char in ['+','-']:
            char = 'sign'
        if char not in state[current_state]:
            return False
        current_state = state[current_state][char]

    if current_state not in [2, 5, 8, 9]:
        return False
    return True


print(is_number('1245'))


## Draw a DFA of states