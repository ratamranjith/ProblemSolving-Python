import timeit
import tracemalloc

def sample_function(n):
    # Example function whose complexity we want to analyze
    total = 0
    for i in range(n):
        total += i
    return total

def measure_time(func, *args, iterations=1000):
    # Measure execution time using timeit
    stmt = f"{func.__name__}(*{args})"
    setup = f"from __main__ import {func.__name__}"
    time = timeit.timeit(stmt, setup=setup, number=iterations) / iterations
    return time

def measure_memory(func, *args):
    # Measure memory usage using tracemalloc
    tracemalloc.start()
    func(*args)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current, peak

def analyze_complexity(func, *args, iterations=1000):
    # Measure both time and space complexity
    time = measure_time(func, *args, iterations=iterations)
    current_memory, peak_memory = measure_memory(func, *args)
    
    return {
        'time_per_run': time,
        'current_memory': current_memory,
        'peak_memory': peak_memory
    }

if __name__ == "__main__":
    n = 10000  # Example input size
    complexity = analyze_complexity(sample_function, n)
    print(f"Time per run: {complexity['time_per_run']} seconds")
    print(f"Current memory usage: {complexity['current_memory']} bytes")
    print(f"Peak memory usage: {complexity['peak_memory']} bytes")
