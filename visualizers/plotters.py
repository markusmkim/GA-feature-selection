import matplotlib.pyplot as plt
import numpy as np


def plot_population_fitness(population, interval, additional_functions=[]):
    for f in additional_functions:
        x = np.linspace(interval[0], interval[1], 10000)
        plt.plot(x, f(x))

    for individual in population:
        plt.plot(individual.phenotype, individual.fitness, marker='o', color='#bf9215', markeredgecolor="#9c7713",
                 markeredgewidth=1, linewidth=0, markersize=10)

    plt.show()

