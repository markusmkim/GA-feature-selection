import random
from .population import Individual


# generates and returns offspring by crossover
def produce_offspring(parent_1, parent_2, crossover_rate, mutation_rate):
    # do crossover by chance, according to the crossover rate
    if random.random() > crossover_rate:
        # do not do crossover
        return (parent_1, parent_2)
    
    # crossover at random index
    crossover_index = random.randint(1, 100)
    offspring_1_genotype = parent_1.genotype[:crossover_index] + parent_2.genotype[crossover_index:]
    offspring_2_genotype = parent_2.genotype[:crossover_index] + parent_1.genotype[crossover_index:]

    # randomly mutate
    mutated_offspring_1_genotype = mutate_by_chance(offspring_1_genotype, mutation_rate)
    mutated_offspring_2_genotype = mutate_by_chance(offspring_2_genotype, mutation_rate)

    # create offspring objects
    offspring_1 = Individual(mutated_offspring_1_genotype)
    offspring_2 = Individual(mutated_offspring_2_genotype)

    return (offspring_1, offspring_2)


# mutates genotype with given mutation rate, returns mutated genotype
# as provided in the pseudocode in equation 3.6 in Evolutionary Optimization Algorithms, Simon.
def mutate_by_chance(genotype, mutation_rate):
    mutated_genotype = ""

    for index in range(len(genotype)):
        if random.random() >= mutation_rate:
            # keep bit
            mutated_genotype += genotype[index]
        else:
            # flip bit
            mutated_genotype += str((int(genotype[index]) + 1) % 2)

    return mutated_genotype
