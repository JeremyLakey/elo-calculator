import random
from elo import simulate_game, get_update
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def runSim(n, k, f = 10000, u = 100):

    true_values = [x * 20 + 50 for x in range(n)]
    values = [random.randint(1000, 2000) for x in range(n)]

    fig = plt.figure()
    fig.set_facecolor("#000")
    sub = fig.add_subplot(1, 1, 1)
    total = 0

    def update(i):
        for _ in range(u):
            a, b = getRandomPair(n)
            r = simulate_game(true_values[a], true_values[b])
            values[a], values[b] = get_update(values[a], values[b], k, r)
        sub.clear()
        sub.scatter(true_values, values, color="green")
        sub.set_facecolor("#000")
        sub.set_xlabel("Actual Elo", color="green")
        sub.set_ylabel("Estimated Elo", color="green")
        sub.spines['bottom'].set_color('green')
        sub.spines['left'].set_color('green')
        # sub.set_facecolor('#00ff00')
        sub.axis(xmin=0, ymin=0, xmax=2200, ymax=2200)
        sub.tick_params(axis='x', colors='green')
        sub.tick_params(axis='y', colors='green')




    mov = anim.FuncAnimation(fig, update, frames=f, repeat=False)
    plt.show()




def getRandomPair(n):
    a = random.randint(0, n - 1)
    b = random.randint(0, n - 1)
    while a == b:
        b = random.randint(0, n - 1)
    return a, b


runSim(100, 20, 500, 50)