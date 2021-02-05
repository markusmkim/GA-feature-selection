

# returns the replacement population
def select_survivors(population, population_size):
    # sort population by fitness
    population.sort(key=lambda x: x.positive_fitness, reverse=True)
    return population[:population_size]

