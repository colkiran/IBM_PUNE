d1 = [(x, y) for x in range(3) for y in range(3)]
print(f"d1 :{d1}")

print("-" * 60)
d2 = [(x, y) for x in range(1, 6) for y in range(1, x+1)]
print(f"d2 :{d2}")

players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}