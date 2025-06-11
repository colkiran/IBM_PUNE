
def fun(dct):
    print(f"Inside the function before :{dct}")
    dct['venue'] = 'GABBA'
    dct['year'] = 2023
    print(f"Inside the function after :{dct}")



player = {'name': 'Virat', 'age': 36, 'runs': 75, 'oppn': 'Aus'}

print(f"Before the function call :{player}")
# player1 = player.copy()  - pass by value

fun(player)

print(f"After the function call :{player}")
