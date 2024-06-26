def initialize_pop(POP_SIZE, recycle_pop, high, low, dimensions):
    population = list()
    for i in range(recycle_pop):
        temp = list()
        for j in range(POP_SIZE):
            individual = [random.uniform(high, low) for _ in range(dimensions)]
            temp.append(individual)
        population.append(temp)
    return population

def calculate(values):
    result = 0
    x = []
    for value in values:
        result = sum(coord ** 2 for coord in value)
        x.append([value, result])
    return x

def calc_best_point(pop):
    all_results = [item[1] for sublist in pop for item in sublist]
    data = [item for sublist in pop for item in sublist]
    min_result = min(all_results)
    final_best_point = []
    for x in data:
        if min_result == x[1]:
            final_best_point = x[0]
    return final_best_point

def calc_min(pop, dimensions):
    averages = [0] * dimensions
    total_points = sum(len(x) for x in pop)
    
    for x in pop:
        for y in x:
            for i in range(dimensions):
                averages[i] += y[0][i]


                
    
    averages = [avg / total_points for avg in averages]
    print("Averages per dimension:", averages)
    return averages

def main(POP_SIZE, recycle_pop, agent, high, low, dimensions):
    population = []
    avg_value = []
    best = 0
    initial_population = initialize_pop(POP_SIZE, recycle_pop, high, low, dimensions)
    
    for _ in range(len(initial_population)):
        best = 0
        population.append(calculate(initial_population[_]))
        best = calc_best_point(population)
    
    avg_value = calc_min(population, dimensions)
    print("avg_value", avg_value)
    print("best point", best)
    print("population", population)

# Input parameters
POP_SIZE = int(input('population size: '))
rcycle_pop = int(input('cycle population: '))
high = int(input('high population: '))
low = int(input('low population: '))
agent = int(input('agent numbers: '))
dimensions = int(input('number of dimensions: '))

main(POP_SIZE, rcycle_pop, agent, high, low, dimensions)