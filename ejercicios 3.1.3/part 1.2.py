import os
os.system("cls")
matrices = [[ 3, 10, 4,	16],
	        [1, 7, 8, -7],
	        [9, -1, 3, 9]]
for row in matrices:
    for element in row:
        print(element, end=(" "))
    print()