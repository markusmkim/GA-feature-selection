import random
import numpy as np


class Individual:
    def __init__(self, genotype):
        self.genotype = genotype  # bitstring
        self.fitness = None

        # fitness shifted to positive number line
        self.positive_fitness = None

        # used for plotting
        self.decimal_value = None


def create_initial_population(population_size, n_features):
    population = []
    for i in range(population_size):
        s = ""
        for i in range(n_features):
            s += str(random.randint(0, 1))

        individual = Individual(s)
        population.append(individual)

    return population


# Evaluates population and applies fitness to all individuals and returns total positive fitness of population
def apply_fitness(population, fitness_function):
    total_positive_fitness = 0

    for individual in population:
        fitness, positive_fitness, decimal_value = fitness_function(individual.genotype)
        individual.fitness = fitness
        individual.positive_fitness = positive_fitness
        individual.decimal_value = decimal_value

        total_positive_fitness += positive_fitness

    return total_positive_fitness
    
