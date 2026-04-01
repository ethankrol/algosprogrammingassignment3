Students:
Hugo Liu - 46439406
Ethan Krol - 33541943

Main Functionality

- Example inputs located in inputs folder
- To run this project, git clone this repository to your computer, and then enter the new repository folder.
- Inside this folder, run python main.py (or python3 main.py, depending on your setup).
- In the terminal, specify the relative path to your input file. The algorithm will print the result, and then prompt you for a file path to save the result to.

Input Assumptions:

- This project assumes the following format for files:
Line 1: number of characters in the alphabet
Next K Lines: character and value, separated by space
Next line: String A (first string)
Next line: String B (second string)

ex.

3
a 2
b 4
c 5
aacb
caab

Output:
- After running python main.py and specifying your input file path, the algorithm will print two lines
First line: Value of HVLCS
Second line: Character subsequence for given value (there can be multiple answers for this, but our algorithm just returns one answer, usually the shortest one)

ex.

9
cb

### Question 1:

    Solved in runtime_graphs.py
    inputs generated using generate_files.py

    To generate 20 random files, with nontrivial, increasing input sizes for a and b, run in terminal:
    > python generate_files.py

    To graph the runtimes for generated 20 nontrivial inputs, run in terminal:
    > python runtime_graphs.py

    This will display and save the runtime of the graph into the graphs folder.

    Here is a generated graph

    ![Generated graph of 20 nontrivial inputs](graphs/runtime_graph.png)

### Question 2:

    TODO by Ethan

### Question 3:

    The following pseudocode revolves around keeping 2 DP arrays
    One DP array is for keeping track of the highest values
    The other DP array is for keeping track of the LENGTH of the highest values

    Pseudocode:
    ```
    dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
    dp_length = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

    vals = [map of character to value]

    for j in range(1, len(dp)):
        for i in range(1, len(dp[j])):

            a_idx, b_idx = i-1, j-1

            if a[a_idx] == b[b_idx]:
                # If they match, we MUST take this path to get the value
                dp[j][i] = dp[j-1][i-1] + vals[a[a_idx]]
                dp_length[j][i] = dp_length[j-1][i-1] + 1
            else:
                # If they don't match, we inherit from the "heavier" neighbor
                if dp[j-1][i] >= dp[j][i-1]:
                    dp[j][i] = dp[j-1][i]
                    dp_length[j][i] = dp_length[j-1][i]
                else:
                    dp[j][i] = dp[j][i-1]
                    dp_length[j][i] = dp_length[j][i-1]

    return dp_length[-1][-1]

    ```

    The Big-Oh of this solution is O(n^2)
    This is because we are iterating through essentially a len(a)+1 by len(b)+1 matrix and performing constant time operations within those iterations,
    If we assume the size of b and a are defined by n, we can say it is O(n^2)

    Otherwise, we can say the Big-Oh is O(ab)
