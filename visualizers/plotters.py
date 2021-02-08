import matplotlib.pyplot as plt
import numpy as np


# Plots a population's fitness distribution, together with an arbitrary number of supplied additional functions.
# Requires individual.decimal_value (phenotype) to map populaiton to real-valued number line.
def plot_population_fitness(population, interval, additional_functions=[]):
    for f in additional_functions:
        x = np.linspace(interval[0], interval[1], 10000)
        plt.plot(x, f(x))

    for individual in population:
        plt.plot(individual.decimal_value, individual.fitness, marker='o', color='#bf9215', markeredgecolor="#9c7713",
                 markeredgewidth=1, linewidth=0, markersize=10)

    plt.show()
    
    
    
def plot_evolution(values, y_label):
    x = np.arange(1, len(values) + 1)
    plt.plot(x, values) 
    plt.xlabel("Generation")
    plt.ylabel(y_label)
    plt.show()
    
    
def plot_and_compare_evolutions(values_1, label_1, values_2, label_2, y_label):
    # assume lists of same length
    x = np.arange(1, len(values_1) + 1)
    plt.plot(x, values_1, label=label_1)
    plt.plot(x, values_2, label=label_2)
    plt.xlabel("Generation")
    plt.ylabel(y_label)
    plt.legend(fontsize="large")
    plt.show()

