import random


# Returns list of selected parents, as list of tuples,
# by fitness-proportional selection
def select_parents(population, total_positive_fitness):
    parents = []

    #  Select one parent by the roulette wheel method.
    #  Code is taken from the pseudocode in Figure 3.5 (p. 48) in Evolutionary Optimization Algorithms, Simon.
    def select_one_parent():
        F = population[0].positive_fitness
        k = 0
        r = random.uniform(0, total_positive_fitness)
        while F < r:
            k += 1
            F += population[k].positive_fitness
        return population[k]

    while len(parents) < len(population) / 2:
        p1 = select_one_parent()
        p2 = select_one_parent()

        # prevent parent mating itself
        while p1.id == p2.id:
            p2 = select_one_parent()

        parents.append((p1, p2))

    return parents
