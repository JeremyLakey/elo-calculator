import random


def get_update(a, b, k, r):
    e = get_expected(a, b)
    u = k * (r - e)
    return a + u, b - u


def get_expected(a, b):
    return 1 / (get_odds(a,b) + 1)


def get_odds(a, b):
    return 10 ** ((b-a)/400)


def str_odds(a, b):
    return "1:" + str(get_odds(100, 900))


def simulate_game(a, b):
    return get_expected(a, b) > random.uniform(0, 1)

