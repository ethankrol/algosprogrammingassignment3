def read_input(file_name=None):
    if not file_name:
        file_name = input("Please enter a path to a file input: ")
    
    # read in format of file instructions
    with open(file_name, 'r') as f:
        k = f.readline()
        k = int(k)

        vals = {}
        for i in range(k):
            val_line = f.readline().split(' ')
            char, val = val_line[0], val_line[1]
            vals[char] = int(val)
        
        a = f.readline().strip()
        b = f.readline().strip()

        return a, b, vals