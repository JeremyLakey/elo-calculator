import random
from elo import simulate_game, get_update


def runSim(n, k, g = 10000):

    true_values = [x * 20 + 1 for x in range(n)]
    values = [1500 for x in range(n)]

    for _ in range(g):
        a, b = getRandomPair(n)
        r = simulate_game(true_values[a], true_values[b])
        values[a], values[b] = get_update(values[a], values[b], k, r)

    error = (sum(values) - sum(true_values)) / n
    for i, x in enumerate(values):
        values[i] = x - error
    print(values)

def getRandomPair(n):
    a = random.randint(0, n - 1)
    b = random.randint(0, n - 1)
    while a == b:
        b = random.randint(0, n - 1)
    return a, b


runSim(100, 10, 1000000)