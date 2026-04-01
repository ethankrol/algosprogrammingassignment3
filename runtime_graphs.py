''' Helper file to time and graph test inputs
Meant to supplement Question 1'''

from main import find_alignment
from read_input import read_input
import time

def test_input_runtime(file_path):
    a, b, vals = read_input(file_path)
    start_time = time.time()
    res, string = find_alignment(a, b, vals)
    end_time = time.time()
    runtime = end_time - start_time
    return runtime

def test_inputs_runtime(file_paths):
    runtimes = []
    for file_path in file_paths:
        runtime = test_input_runtime(file_path)
        runtimes.append(runtime)
    return runtimes

def graph_runtimes(file_paths):
    import matplotlib.pyplot as plt
    runtimes = test_inputs_runtime(file_paths)
    x_axis = [f"{i*100+35}" for i in range(len(file_paths))]
    plt.plot(x_axis, runtimes)
    plt.xlabel('Size of input (length of a and b +- 5)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime of find_alignment on Different Inputs')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('graphs/runtime_graph.png')
    plt.show()

if __name__ == '__main__':
    file_paths = [f"inputs/test_input_{i}.txt" for i in range(20)]
    graph_runtimes(file_paths)
