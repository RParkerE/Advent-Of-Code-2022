"""
    [W]         [J]     [J]        
    [V]     [F] [F] [S] [S]        
    [S] [M] [R] [W] [M] [C]        
    [M] [G] [W] [S] [F] [G]     [C]
[W] [P] [S] [M] [H] [N] [F]     [L]
[R] [H] [T] [D] [L] [D] [D] [B] [W]
[T] [C] [L] [H] [Q] [J] [B] [T] [N]
[G] [G] [C] [J] [P] [P] [Z] [R] [H]
 1   2   3   4   5   6   7   8   9 
"""

crates = {
 	'1': ['G', 'T', 'R', 'W'],
 	'2': ['G', 'C', 'H', 'P', 'M', 'S', 'V', 'W'],
 	'3': ['C', 'L', 'T', 'S', 'G', 'M'],
 	'4': ['J', 'H', 'D', 'M', 'W', 'R', 'F'],
 	'5': ['P', 'Q', 'L', 'H', 'S', 'W', 'F', 'J'],
 	'6': ['P', 'J', 'D', 'N', 'F', 'M', 'S'],
 	'7': ['Z', 'B', 'D', 'F', 'G', 'C', 'S', 'J'],
 	'8': ['R', 'T', 'B'],
 	'9': ['H', 'N', 'W', 'L', 'C']
 }

instructions = """move 3 from 4 to 3
move 3 from 8 to 6
move 2 from 3 to 8
move 3 from 7 to 2
move 1 from 1 to 3
move 6 from 2 to 7
move 5 from 3 to 6
move 1 from 8 to 6
move 4 from 4 to 3
move 2 from 1 to 2
move 10 from 7 to 3
move 1 from 7 to 2
move 6 from 5 to 8
move 1 from 1 to 4
move 7 from 6 to 3
move 22 from 3 to 4
move 3 from 2 to 8
move 4 from 6 to 8
move 5 from 2 to 1
move 3 from 9 to 4
move 2 from 4 to 3
move 1 from 9 to 2
move 1 from 5 to 3
move 1 from 2 to 6
move 1 from 5 to 2
move 1 from 2 to 7
move 4 from 4 to 5
move 2 from 1 to 9
move 1 from 1 to 3
move 2 from 5 to 9
move 5 from 9 to 8
move 1 from 5 to 9
move 1 from 7 to 2
move 1 from 9 to 4
move 5 from 6 to 7
move 1 from 5 to 2
move 2 from 2 to 4
move 2 from 7 to 4
move 2 from 7 to 8
move 21 from 8 to 6
move 6 from 3 to 1
move 1 from 7 to 9
move 1 from 1 to 7
move 7 from 6 to 8
move 3 from 1 to 9
move 24 from 4 to 8
move 3 from 1 to 3
move 10 from 6 to 8
move 1 from 4 to 5
move 1 from 3 to 9
move 5 from 9 to 8
move 11 from 8 to 3
move 1 from 5 to 7
move 1 from 1 to 8
move 1 from 6 to 1
move 19 from 8 to 1
move 1 from 7 to 9
move 10 from 3 to 1
move 3 from 3 to 8
move 1 from 7 to 3
move 1 from 9 to 2
move 23 from 1 to 7
move 1 from 1 to 9
move 1 from 3 to 6
move 2 from 6 to 9
move 7 from 8 to 1
move 8 from 8 to 1
move 11 from 7 to 2
move 2 from 6 to 8
move 1 from 6 to 8
move 7 from 8 to 6
move 1 from 9 to 4
move 1 from 8 to 1
move 10 from 7 to 1
move 6 from 2 to 5
move 5 from 2 to 9
move 4 from 5 to 8
move 1 from 5 to 8
move 13 from 1 to 6
move 1 from 2 to 4
move 1 from 4 to 5
move 2 from 9 to 4
move 3 from 9 to 4
move 2 from 5 to 3
move 1 from 3 to 9
move 2 from 8 to 5
move 2 from 5 to 7
move 2 from 8 to 6
move 2 from 7 to 3
move 2 from 7 to 8
move 4 from 1 to 3
move 3 from 8 to 4
move 8 from 4 to 9
move 1 from 9 to 8
move 3 from 3 to 6
move 4 from 3 to 9
move 1 from 8 to 2
move 12 from 1 to 5
move 9 from 6 to 8
move 1 from 4 to 8
move 3 from 1 to 3
move 12 from 5 to 8
move 1 from 2 to 6
move 1 from 3 to 1
move 1 from 3 to 2
move 1 from 1 to 2
move 16 from 6 to 1
move 1 from 6 to 3
move 2 from 3 to 8
move 7 from 8 to 5
move 1 from 2 to 6
move 1 from 2 to 1
move 2 from 9 to 4
move 1 from 6 to 7
move 8 from 9 to 8
move 5 from 5 to 6
move 9 from 8 to 7
move 12 from 1 to 3
move 2 from 6 to 3
move 6 from 8 to 9
move 5 from 1 to 4
move 2 from 5 to 7
move 11 from 7 to 3
move 1 from 7 to 4
move 2 from 6 to 8
move 7 from 4 to 6
move 3 from 8 to 7
move 3 from 8 to 2
move 19 from 3 to 2
move 4 from 8 to 7
move 2 from 9 to 8
move 1 from 4 to 5
move 1 from 6 to 8
move 1 from 5 to 7
move 8 from 9 to 4
move 1 from 8 to 5
move 1 from 5 to 6
move 4 from 2 to 7
move 8 from 6 to 9
move 6 from 7 to 3
move 4 from 3 to 8
move 5 from 8 to 7
move 15 from 2 to 8
move 8 from 3 to 4
move 7 from 9 to 7
move 3 from 2 to 4
move 2 from 7 to 4
move 2 from 4 to 3
move 1 from 9 to 4
move 9 from 7 to 5
move 4 from 5 to 9
move 2 from 5 to 3
move 2 from 9 to 1
move 3 from 5 to 2
move 4 from 3 to 1
move 7 from 7 to 4
move 3 from 2 to 6
move 4 from 4 to 5
move 2 from 1 to 6
move 8 from 4 to 1
move 1 from 8 to 2
move 1 from 2 to 8
move 11 from 8 to 7
move 3 from 5 to 9
move 1 from 5 to 9
move 11 from 7 to 1
move 7 from 8 to 9
move 11 from 1 to 3
move 6 from 4 to 5
move 8 from 1 to 7
move 4 from 6 to 5
move 3 from 5 to 8
move 8 from 7 to 3
move 7 from 4 to 7
move 7 from 5 to 6
move 3 from 3 to 8
move 2 from 4 to 9
move 16 from 3 to 1
move 7 from 7 to 1
move 2 from 8 to 7
move 2 from 8 to 1
move 1 from 8 to 4
move 1 from 7 to 4
move 2 from 4 to 2
move 1 from 8 to 7
move 1 from 2 to 3
move 1 from 2 to 4
move 1 from 7 to 8
move 8 from 6 to 7
move 1 from 3 to 5
move 15 from 1 to 2
move 4 from 9 to 1
move 1 from 8 to 1
move 11 from 9 to 2
move 21 from 2 to 6
move 1 from 4 to 2
move 4 from 2 to 7
move 1 from 5 to 9
move 1 from 9 to 4
move 19 from 1 to 2
move 5 from 2 to 4
move 8 from 7 to 6
move 10 from 6 to 2
move 5 from 7 to 5
move 2 from 4 to 1
move 3 from 6 to 9
move 3 from 9 to 2
move 1 from 5 to 2
move 13 from 6 to 3
move 2 from 6 to 9
move 17 from 2 to 3
move 1 from 6 to 2
move 2 from 2 to 1
move 2 from 1 to 5
move 5 from 5 to 3
move 2 from 2 to 8
move 10 from 2 to 1
move 18 from 3 to 8
move 13 from 8 to 1
move 7 from 8 to 2
move 2 from 2 to 1
move 4 from 3 to 8
move 1 from 2 to 7
move 1 from 2 to 8
move 2 from 4 to 1
move 1 from 5 to 4
move 1 from 9 to 6
move 1 from 1 to 7
move 11 from 3 to 4
move 1 from 6 to 2
move 7 from 1 to 2
move 5 from 8 to 5
move 1 from 7 to 5
move 3 from 5 to 1
move 7 from 1 to 6
move 6 from 1 to 6
move 6 from 1 to 8
move 2 from 1 to 3
move 5 from 2 to 5
move 1 from 7 to 6
move 1 from 4 to 2
move 4 from 2 to 4
move 1 from 1 to 9
move 1 from 3 to 8
move 7 from 8 to 5
move 1 from 9 to 7
move 1 from 9 to 4
move 8 from 5 to 7
move 5 from 4 to 1
move 4 from 1 to 6
move 3 from 1 to 6
move 3 from 3 to 6
move 1 from 5 to 6
move 3 from 7 to 5
move 15 from 6 to 7
move 12 from 7 to 4
move 8 from 5 to 2
move 3 from 4 to 9
move 3 from 9 to 7
move 1 from 6 to 2
move 9 from 4 to 9
move 4 from 9 to 1
move 2 from 1 to 7
move 3 from 6 to 4
move 3 from 6 to 4
move 2 from 1 to 2
move 1 from 5 to 6
move 2 from 9 to 4
move 13 from 4 to 2
move 22 from 2 to 3
move 3 from 7 to 8
move 1 from 9 to 6
move 1 from 9 to 3
move 2 from 8 to 9
move 3 from 9 to 8
move 5 from 6 to 4
move 2 from 8 to 6
move 4 from 7 to 8
move 2 from 2 to 5
move 4 from 8 to 7
move 2 from 5 to 7
move 7 from 7 to 2
move 9 from 4 to 7
move 4 from 2 to 1
move 3 from 7 to 6
move 12 from 3 to 5
move 5 from 2 to 5
move 1 from 8 to 2
move 1 from 3 to 5
move 4 from 3 to 1
move 2 from 6 to 1
move 11 from 5 to 3
move 3 from 6 to 1
move 8 from 1 to 9
move 5 from 9 to 8
move 2 from 9 to 7
move 1 from 1 to 8
move 4 from 7 to 6
move 6 from 3 to 1
move 1 from 9 to 7
move 5 from 7 to 4
move 3 from 8 to 3
move 1 from 6 to 5
move 2 from 2 to 1
move 4 from 7 to 9
move 3 from 8 to 6
move 6 from 3 to 8
move 6 from 8 to 7
move 4 from 6 to 5
move 6 from 5 to 8
move 2 from 9 to 5
move 2 from 9 to 8
move 4 from 7 to 4
move 1 from 6 to 3
move 5 from 8 to 4
move 1 from 6 to 9
move 1 from 7 to 3
move 7 from 3 to 8
move 6 from 1 to 4
move 6 from 1 to 2
move 17 from 4 to 6
move 4 from 8 to 5
move 3 from 3 to 1
move 5 from 4 to 1
move 5 from 2 to 7
move 7 from 8 to 1
move 7 from 7 to 2
move 4 from 6 to 3
move 6 from 1 to 8
move 2 from 4 to 9
move 2 from 5 to 4
move 1 from 4 to 3
move 1 from 4 to 7
move 2 from 7 to 5
move 4 from 5 to 3
move 1 from 9 to 1
move 5 from 5 to 3
move 1 from 8 to 5
move 7 from 6 to 1
move 6 from 6 to 8
move 11 from 3 to 7
move 2 from 9 to 1
move 8 from 8 to 2
move 5 from 7 to 5
move 5 from 7 to 4
move 1 from 2 to 6
move 2 from 4 to 6
move 1 from 7 to 5
move 2 from 6 to 4
move 10 from 2 to 6
move 3 from 4 to 5
move 1 from 6 to 4
move 4 from 6 to 4
move 6 from 6 to 9
move 3 from 3 to 8
move 19 from 1 to 8
move 23 from 8 to 9
move 1 from 8 to 1
move 1 from 1 to 7
move 1 from 7 to 1
move 1 from 1 to 6
move 5 from 9 to 5
move 1 from 8 to 5
move 5 from 4 to 5
move 4 from 5 to 4
move 1 from 9 to 1
move 6 from 9 to 3
move 2 from 2 to 8
move 1 from 1 to 3
move 1 from 6 to 7
move 1 from 7 to 3
move 1 from 2 to 5
move 6 from 9 to 8
move 5 from 4 to 5
move 10 from 5 to 2
move 10 from 5 to 2
move 11 from 9 to 1
move 4 from 2 to 6
move 18 from 2 to 9
move 2 from 6 to 9
move 3 from 3 to 9
move 1 from 4 to 3
move 1 from 6 to 8
move 6 from 8 to 4
move 6 from 5 to 7
move 19 from 9 to 4
move 7 from 1 to 3
move 1 from 6 to 8
move 4 from 8 to 7
move 2 from 3 to 6
move 3 from 1 to 8
move 1 from 1 to 5
move 7 from 7 to 3
move 8 from 3 to 1
move 1 from 5 to 7
move 2 from 6 to 2
move 3 from 1 to 8
move 1 from 2 to 6
move 3 from 1 to 7
move 4 from 8 to 9
move 4 from 7 to 6
move 3 from 9 to 7
move 3 from 9 to 3
move 6 from 7 to 3
move 13 from 3 to 1
move 5 from 3 to 4
move 1 from 8 to 7
move 1 from 7 to 9
move 1 from 8 to 5
move 1 from 9 to 4
move 1 from 5 to 2
move 2 from 9 to 2
move 3 from 6 to 2
move 1 from 3 to 7
move 13 from 4 to 8
move 14 from 1 to 5
move 6 from 2 to 7
move 4 from 8 to 7
move 1 from 1 to 3
move 1 from 2 to 6
move 5 from 4 to 2
move 4 from 8 to 4
move 12 from 5 to 4
move 1 from 3 to 8
move 9 from 4 to 2
move 9 from 4 to 5
move 1 from 4 to 5
move 6 from 4 to 3
move 5 from 8 to 4
move 9 from 4 to 7
move 4 from 2 to 3
move 8 from 7 to 1
move 2 from 7 to 1
move 2 from 2 to 9
move 1 from 6 to 7
move 2 from 6 to 3
move 1 from 2 to 3
move 2 from 7 to 3
move 3 from 3 to 7
move 8 from 1 to 2
move 9 from 5 to 3
move 15 from 2 to 7
move 20 from 7 to 5
move 23 from 5 to 6
move 20 from 6 to 8
move 1 from 6 to 4
move 2 from 9 to 7
move 1 from 4 to 6
move 3 from 7 to 6
move 2 from 7 to 5
move 13 from 3 to 5
move 3 from 7 to 1
move 13 from 5 to 4
move 3 from 1 to 4
move 5 from 6 to 1
move 6 from 4 to 3
move 1 from 7 to 4
move 11 from 8 to 6
move 1 from 8 to 6
move 2 from 1 to 5
move 2 from 5 to 3
move 11 from 6 to 5
move 3 from 8 to 3
move 4 from 3 to 5
move 15 from 5 to 1
move 1 from 3 to 5
move 3 from 8 to 5
move 1 from 5 to 9
move 1 from 5 to 3
move 9 from 4 to 6
move 7 from 6 to 8
move 2 from 4 to 6
move 2 from 5 to 1
move 8 from 8 to 7
move 6 from 6 to 2
move 1 from 5 to 2
move 4 from 3 to 4
move 6 from 1 to 5
move 7 from 3 to 4
move 2 from 3 to 2
move 2 from 8 to 9
move 9 from 2 to 5
move 9 from 5 to 4
move 2 from 3 to 6
move 14 from 1 to 7
move 15 from 7 to 2
move 1 from 1 to 7
move 7 from 5 to 1
move 2 from 9 to 2
move 2 from 1 to 7
move 1 from 1 to 4
move 2 from 6 to 8
move 7 from 2 to 8
move 1 from 9 to 6
move 7 from 8 to 3
move 1 from 6 to 4
move 1 from 8 to 2
move 6 from 4 to 6
move 9 from 2 to 1
move 1 from 3 to 9
move 3 from 7 to 5"""

#####################################
#									#
#				PART 1				#
#									#
#####################################

import re
steps = instructions.splitlines()
for step in steps:
	step = re.findall(r'\d+', step)
	quantity, stackFrom, stackTo = int(step[0]), crates[step[1]], crates[step[2]]
	tmpStack = stackFrom[len(stackFrom) - quantity:]
	tmpStack = tmpStack[::-1]
	stackFrom = stackFrom[: len(stackFrom) - quantity]
	for item in tmpStack:
		stackTo.append(item)
	crates[step[1]] = stackFrom
	crates[step[2]] = stackTo

print(crates)

#####################################
#									#
#				PART 2				#
#									#
#####################################

import re
steps = instructions.splitlines()
for step in steps:
	step = re.findall(r'\d+', step)
	quantity, stackFrom, stackTo = int(step[0]), crates[step[1]], crates[step[2]]
	tmpStack = stackFrom[len(stackFrom) - quantity:]
	stackFrom = stackFrom[: len(stackFrom) - quantity]
	for item in tmpStack:
		stackTo.append(item)
	crates[step[1]] = stackFrom
	crates[step[2]] = stackTo

print(crates)