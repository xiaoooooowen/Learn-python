from tokenize import Number


magics = ['alice','jack','malong']
for magic in magics:
    print(f"{magic.title()},you are very nb.")
    print(f"I can't wait to see your next trick,{magic.title()}.\n")
print(f"you are all very good!")
for value in range(1,10):
    print(value)
   
Numbers = list(range(1,6))
print(Numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
print(sum(squares))

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
for player in players[:4]:
    print(player.title())
   
heros = players[:]
print(heros)

dimens = 200,50         #ิชื้#
print(dimens[0])
print(dimens[1])
