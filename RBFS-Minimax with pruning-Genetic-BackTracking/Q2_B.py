import Q2_A
import random

def fitness_function(state):
    return Q2_A.alpha_beta(0, 1, True, state, MIN, MAX)[0]

def create_individual():
    arrangement = [random.randint(0, list_range) for i in range(list_length)]
    return arrangement

def create_population(population_size):
    return [create_individual() for i in range(population_size)]

def selection(population):
    return random.choice(population)

def crossover(parent1, parent2):
    midpoint = random.randint(1, len(parent1)-1)
    child = parent1[:midpoint] + parent2[midpoint:]
    return child

def mutation(individual):
    index = random.randint(0, list_length-1)
    individual[index] += random.randint(-1, 1)
    if individual[index] < 0:
        individual[index] = 0
    if individual[index] > list_range:
        individual[index] = list_range
    return individual

def genetic_algorithm(population_size, generations):
    population = create_population(population_size)

    for i in range(generations):
        new_population = []
        for j in range(population_size):
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2)
            child = mutation(child)
            new_population.append(child)

        population = new_population

    best_individual = max(population, key=fitness_function)
    return best_individual, fitness_function(best_individual)


if __name__ == "__main__":
    MIN, MAX = float('-inf'), float('inf')

    list_length = 8
    list_range = 8

    population_size = 100
    generations = 100
    best_solution, best_fitness = genetic_algorithm(population_size, generations)
    print("Found solution:", best_solution)
    print("Solution fitness:", best_fitness)

