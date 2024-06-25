import random

bet = input("E type imong number Boss (3 numbers with spaces): ").split()
bet = [int(num) for num in bet]

result = [random.randint(1, 9) for i in range(3)]

print(f"The result is: {result}")

if bet == result:
    print("Perting daoga Boss!")
elif bet[1:] == result[31:]:
    print("Hapitan ka mo daog Boss!")
elif bet[0] == result[0] or bet[1] == result[1] or bet[2] == result[2]:
    print("Gamay nalang kulang Boss!")
else:
    print("Agooy pildi gyud Boss!")