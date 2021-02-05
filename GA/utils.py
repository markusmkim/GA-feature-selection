

def get_avg_fitness(population):
    total_fitness = 0
    for individual in population:
        total_fitness += individual.fitness

    return total_fitness / len(population)
