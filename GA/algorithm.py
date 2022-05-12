import numpy as np
from .components.population import create_initial_population, apply_fitness
from .components.selection import select_parents
from .components.crossover_mutation import produce_offspring
from .components.replacement import select_survivors, family_tournament
from .utils import get_avg_fitness, get_total_positive_fitness



def run_ga(n_features, population_size, generations, mutation_rate, crossover_rate, fitnesss_function, crowding=False, epoch_callback=None):
    # initialize population and evaluate fitness
    population = create_initial_population(population_size, n_features)
    total_positive_fitness = apply_fitness(population, fitnesss_function)

    if epoch_callback is not None:
        epoch_callback(population, 0)

    # run through generations:
    for i in range(generations):
        # select parents
        parents = select_parents(population, total_positive_fitness)
        
        
        if crowding:
            survivors = []
            # create offspring and decide replacement by "family" tournament
            for pair in parents:
                offspring_pair = produce_offspring(pair[0], pair[1], crossover_rate, mutation_rate)
                apply_fitness(offspring_pair, fitnesss_function)
                survivor_pair = family_tournament(pair, offspring_pair)
                survivors.append(survivor_pair[0])
                survivors.append(survivor_pair[1])
            
            population = survivors
            
            
        else:
            # create offspring and evaluate offspring fitness
            offspring = []
            for pair in parents:
                offspring_pair = produce_offspring(pair[0], pair[1], crossover_rate, mutation_rate)
                offspring.append(offspring_pair[0])
                offspring.append(offspring_pair[1])
            apply_fitness(offspring, fitnesss_function)

            # replacement: select survivors for next generation
            population = select_survivors(population + offspring, population_size)
            
        
        
        # evaluate fitness for next generation
        # total_positive_fitness = apply_fitness(population, fitnesss_function)
        
        total_positive_fitness = get_total_positive_fitness(population)
        
    
        if epoch_callback is not None:
            epoch_callback(population, i + 1)
            
    return population