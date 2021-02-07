from GA.utils import hamming_distance


# returns the replacement population
def select_survivors(population, population_size):
    # sort population by fitness
    population.sort(key=lambda x: x.positive_fitness, reverse=True)
    return population[:population_size]


# returns winners (pair) of local family tournament
def family_tournament(parents, offspring):
    duel_1 = (parents[0], offspring[0])
    duel_2 = (parents[1], offspring[1])
    total_hamming_distance = hamming_distance(
        parents[0].genotype, offspring[0].genotype) + hamming_distance(parents[1].genotype, offspring[1].genotype)
    
    # reset duelling pairs if total hamming distance can be reduced
    if hamming_distance(parents[0].genotype, offspring[1].genotype) + hamming_distance(parents[1].genotype, offspring[0].genotype) < total_hamming_distance:
        duel_1 = (parents[0], offspring[1])
        duel_2 = (parents[1], offspring[0])
        
        
    duels = [duel_1, duel_2]
    winners = []
    # deterministic crowding:
    for duel in duels:
        if duel[0].positive_fitness > duel[1].positive_fitness:
            winners.append(duel[0])
        else:
            winners.append(duel[1])
            
    return winners
    




