import numpy as np


def get_avg_fitness(population):
    total_fitness = 0
    for individual in population:
        total_fitness += individual.fitness

    return total_fitness / len(population)


def get_total_positive_fitness(population):
    total_positive_fitness = 0
    for individual in population:
        total_positive_fitness += individual.positive_fitness
    return total_positive_fitness



# returns Hamming distance between two bitstrings
def hamming_distance(bitstring_1, bitstring_2):
    d = 0
    # assume bitstrings of equal length
    for i in range(len(bitstring_1)):
        if bitstring_1[i] != bitstring_2[i]:
            d += 1
    return d



def entropy(population):
    if len(population) == 0:
        return 0
    
    bitstring_length = len(population[0].genotype)
    bit_counts = np.zeros(bitstring_length)

    for individual in population:
        for i in range(bitstring_length):
            if individual.genotype[i] == "1":
                bit_counts[i] += 1
    
    # p_i = propbability of i-th bit being 1.
    p = bit_counts /len(population)
    
    # p * log_2 (p). Avoid diviion by zero error by adding 1*10^-6 before logarithm. Has very little effect on the entropy.
    p_log_p = p * np.log2(p + 0.000001)
    
    return - np.sum(p_log_p)