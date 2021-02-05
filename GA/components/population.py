import random


class Individual:
    counter = 1  # static variable for creating unique IDs

    def __init__(self, genotype):
        self.genotype = genotype  # bitstrings
        self.fitness = None

        # fitness scaled to positive number line
        self.positive_fitness = None

        # used for plotting
        self.phenotype = None

        self.id = Individual.counter
        Individual.counter += 1


def create_initial_population(population_size):
    # 101 columns means bitstrings of length = 101.
    population = []
    for i in range(population_size):
        s = ""
        for i in range(101):
            s += str(random.randint(0, 1))

        individual = Individual(s)
        population.append(individual)

    return population


# applies fitness to all individuals and returns total positive fitness of population
def apply_fitness(population, fitness_function):
    total_positive_fitness = 0

    for individual in population:
        fitness, positive_fitness, phenotype = fitness_function(individual.genotype)
        individual.fitness = fitness
        individual.positive_fitness = positive_fitness
        individual.phenotype = phenotype

        total_positive_fitness += positive_fitness

    return total_positive_fitness
