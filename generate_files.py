'''Helper file to generate larger input files
Meant to supplement Question 1'''

import random

def number_to_ascii(num):
    if num < 26:
        return chr(97+num)
    if num < 26+26:
        return chr(65+(num-26))
    else:
        raise ValueError("num is too large to convert to ascii, please keep k <= 52")

def generate_single_input(file_path, k, a_len, b_len):
    with open(file_path, 'w') as f:
        values = [random.randint(0, 100) for _ in range(k)]
        
        f.write(str(k) + '\n')
        for i in range(k):
            f.write(number_to_ascii(i) + ' ' + str(values[i]) + '\n')
        
        a = ''.join([number_to_ascii(random.randrange(k)) for _ in range(a_len)])
        b = ''.join([number_to_ascii(random.randrange(k)) for _ in range(b_len)])
        f.write(a + '\n')
        f.write(b + '\n')
    
if __name__ == '__main__':
    # Generates 20 files with increasing lengths of a and b
    # Adds some variability to the lengths of a and b using random function
    k_range = (10, 52)
    a_len_range = (30, 40)
    b_len_range = (30, 40)
    base_file_path = "inputs/test_input_{}.txt"
    for i in range(20):
        k = random.randint(k_range[0], k_range[1])
        a_len = random.randint(a_len_range[0], a_len_range[1])
        b_len = random.randint(b_len_range[0], b_len_range[1])
        a_len_range = (a_len_range[0]+100, a_len_range[1]+100)
        b_len_range = (b_len_range[0]+100, b_len_range[1]+100)
        generate_single_input(base_file_path.format(i), k, a_len, b_len)
    
