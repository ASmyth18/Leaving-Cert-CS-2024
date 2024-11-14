"""
This script solves the following problem:

Design an algorithm to solve the Traveling Salesman Problem (TSP) using dynamic programming.
Given a set of cities and the distances between them,
find the shortest possible route that visits each city exactly once and returns to the starting city.
"""

def tsp_dynamic_programming(distances):
    n = len(distances)
    all_cities = range(n)
    
    # Create a memo table to store the minimum cost for each subproblem
    memo = {}
    
    # Function to solve the subproblem
    def solve(current_city, visited_cities):
        # Base case: if all cities have been visited, return the cost to return to the starting city
        if len(visited_cities) == n:
            return distances[current_city][0]
        
        # Create a tuple key for memoization(This word looks stupid, english is stupid)
        key = (current_city, tuple(visited_cities))
        
        # Check if the subproblem has already been solved
        if key in memo:
            return memo[key]
        
        # Initialize the minimum cost to infinity
        min_cost = float('inf')
        
        # Iterate over all unvisited cities
        for next_city in all_cities:
            if next_city not in visited_cities:
                # Calculate the cost to visit the next city
                cost = distances[current_city][next_city] + solve(next_city, visited_cities + [next_city])
                min_cost = min(min_cost, cost)
        
        # Store the minimum cost in the memo table
        memo[key] = min_cost
        
        return min_cost
    
    # Start the TSP from city 0 and return the minimum cost
    return solve(0, [0])

# Example usage
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost = tsp_dynamic_programming(distances)
print("Minimum cost:", min_cost)


#Fibonacci sequence

n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()
