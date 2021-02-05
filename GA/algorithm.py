from .components.population import create_initial_population, apply_fitness
from .components.selection import select_parents
from .components.crossover_mutation import produce_offspring
from .components.replacement import select_survivors

from .utils import get_avg_fitness
import numpy as np


def run_ga(population_size, generations, mutation_rate, crossover_rate, fitnesss_function, verbose=0, epoch_callback=None):

    # initialize population and evaluate fitness
    population = create_initial_population(population_size)
    total_positive_fitness = apply_fitness(population, fitnesss_function)

    if epoch_callback is not None:
        epoch_callback(population, 0)

    # run through generations:
    for i in range(generations):
        # select parenst
        parents = select_parents(population, total_positive_fitness)

        # create offspring and evaluate offspring fitness
        offspring = []
        for pair in parents:
            offspring_pair = produce_offspring(pair[0], pair[1], mutation_rate)
            offspring.append(offspring_pair[0])
            offspring.append(offspring_pair[1])
        apply_fitness(offspring, fitnesss_function)

        # replacement: select survivors for next generation
        population = select_survivors(population + offspring, population_size)

        # evaluate fitness for next generation
        total_positive_fitness = apply_fitness(population, fitnesss_function)

        if epoch_callback is not None:
            epoch_callback(population, 1)
