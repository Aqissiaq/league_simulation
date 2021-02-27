from random import randint, shuffle
from string import ascii_lowercase

# Prompted by a Matt Parker tweet
# What are the chances that the first n teams of a league have strictly descending scores?
# ie. 51, 50, 49...

def play_game():
    result = randint(0, 2)
    if result == 0:
        return 3, 0
    elif result == 1:
        return 0, 3
    else:
        return 1, 1

def strictly_descending(sequence: list):
    for a,b in zip(sequence, sequence[1:]):
        if a-b != 1:
            return False
    return True

def play_round(league : dict):
    teams = list(league.keys())
    shuffle(teams)
    pairings = [(teams[i], teams[i+1]) for i in range(0, len(teams), 2)]
    for t1, t2 in pairings:
        t1_score, t2_score = play_game()
        league[t1] += t1_score
        league[t2] += t2_score

if __name__ == "__main__":
    N = 1_000_000 # number of trials
    n_teams = 24
    n_sorted_after_g_games = {g:{n:0 for n in range(2, n_teams)} for g in range(1, n_teams*2)}
    for _ in range(N):
        league = {name:0 for name in ascii_lowercase[:n_teams]}
        for games in range(1, n_teams * 2):
            play_round(league)
            for n in range(2, n_teams):
                if strictly_descending(sorted(list(league.values()), reverse=True)[:n]):
                    n_sorted_after_g_games[games][n] += 1
    
    proportion_sorted = [{n:(p/N) for n, p in d.items()} for d in n_sorted_after_g_games.values()]
    with open("league_data.txt", "w+") as f:
        f.write(f"Games,n,percentage sorted\n")
        for g, res in enumerate(proportion_sorted):
            for key, value in res.items():
                f.write(f"{g+1},{key},{value*100}\n")