"""
Simple Darwin-Fuzz Example
===========================

This example demonstrates basic fuzzing of a simple function
that has algorithmic complexity issues.
"""

import random
import time

# Simulated target function with complexity vulnerability
def vulnerable_function(data):
    """
    A function that has O(n²) complexity in worst case.
    Darwin-Fuzz should evolve inputs that trigger this.
    """
    if len(data) < 2:
        return 0
    
    # Worst case: reversed sorted array
    comparisons = 0
    arr = list(data)
    
    # Bubble sort (intentionally inefficient)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return comparisons


def fitness_function(input_data):
    """
    Fitness function that rewards inputs causing more work.
    Higher fitness = more interesting input.
    """
    start_time = time.time()
    comparisons = vulnerable_function(input_data)
    execution_time = time.time() - start_time
    
    # Fitness based on execution time and work done
    return execution_time * comparisons


def simple_genetic_algorithm():
    """
    Simplified genetic algorithm (before C++ integration).
    This demonstrates the concept.
    """
    population_size = 50
    generations = 100
    mutation_rate = 0.1
    
    # Initialize population with random arrays
    population = []
    for _ in range(population_size):
        size = random.randint(5, 20)
        individual = [random.randint(0, 100) for _ in range(size)]
        population.append(individual)
    
    print("Starting Evolution...")
    print("=" * 60)
    
    for gen in range(generations):
        # Evaluate fitness
        fitness_scores = [(ind, fitness_function(ind)) for ind in population]
        fitness_scores.sort(key=lambda x: x[1], reverse=True)
        
        best_individual, best_fitness = fitness_scores[0]
        
        if gen % 10 == 0:
            print(f"Generation {gen:3d} | Best Fitness: {best_fitness:8.4f} | "
                  f"Array Size: {len(best_individual)}")
        
        # Selection (keep top 50%)
        population = [ind for ind, _ in fitness_scores[:population_size // 2]]
        
        # Reproduction
        while len(population) < population_size:
            # Select two parents
            parent1 = random.choice(population[:10])
            parent2 = random.choice(population[:10])
            
            # Crossover
            if len(parent1) > 1 and len(parent2) > 1:
                split = len(parent1) // 2
                child = parent1[:split] + parent2[split:]
            else:
                child = parent1[:]
            
            # Mutation
            if random.random() < mutation_rate:
                if len(child) > 0:
                    idx = random.randint(0, len(child) - 1)
                    child[idx] = random.randint(0, 100)
            
            population.append(child)
    
    print("=" * 60)
    print("Evolution Complete!")
    print(f"\nBest Input Found: {best_individual}")
    print(f"Fitness Score: {best_fitness:.4f}")
    print(f"\nNote: Darwin-Fuzz evolved an input that maximizes")
    print(f"      the algorithmic complexity of the target function!")


if __name__ == "__main__":
    print("\n🧬 Darwin-Fuzz Simple Example\n")
    simple_genetic_algorithm()
