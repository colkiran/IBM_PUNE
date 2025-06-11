d1 = [(x, y) for x in range(3) for y in range(3)]
print(f"d1 :{d1}")

print("-" * 60)
d2 = [(x, y) for x in range(1, 6) for y in range(1, x+1)]
print(f"d2 :{d2}")

print("-" * 60)
players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}

print(f"players :{players}")

print("-" * 60)
print(f"Sachin :{players['sachin']}")

print("-" * 60)
print(f"Sachin :{sum(players['sachin'])}")

print("-" * 60)
scores = {k :sum(v) for k, v in players.items()}
print(f"scores :{scores}")

print("-" * 60)
plyr_scores = {k: (lambda scores : sum(scores) / len(scores))(v)
               for k, v in players.items()}
print(plyr_scores)

print("-" * 60)
def avgScr(scr):
    return sum(scr) / len(scr)

print(avgScr([1, 2, 3, 4, 5]))

print("-" * 60)
plyr_scores = {k: avgScr(v) for k, v in players.items()}
print(plyr_scores)

print("-" * 60)
basic1 = [{x: (lambda par: "Mr." + par)("Sachin {}".format(x))}
          for x in range(1, 6)]
print(basic1)

print("-" * 60)
scores = [score for score in players.values()]
print(scores)

print("-" * 60)
scores = [scr for score in players.values() for scr in score]
print(f"scores :{scores}")

print("-" * 60)
scores = [scr for score in players.values() for scr in score if scr > 200]
print(f"scores :{scores}")

print("-" * 60)
scores = {name : [scr for scr in score if scr > 200]
          for name, score in players.items()}
print(f"scores :{scores}")

