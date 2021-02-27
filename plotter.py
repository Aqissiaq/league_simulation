import matplotlib.pyplot as plt

def parse_line(line):
    l = line.split(',')
    return int(l[0]), int(l[1]), float(l[2])


def plot_ns(data, *ns):
    for n in ns:
        plt.plot([tpl[2] for tpl in filter(lambda x: x[1] == n, data)],
                label=f"n = {n}")
    plt.ylabel("% Chance")
    plt.xlabel("Number of games")
    plt.title("24 team league, 1_000_000 runs")
    plt.legend()
    plt.show()

with open("league_data.txt", "r") as f:
    data = [parse_line(line) for line in f.readlines()[1:]]

    plot_ns(data, 2, 3, 4)
    plot_ns(data, 10, 11, 12)