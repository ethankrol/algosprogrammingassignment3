from read_input import read_input

def find_alignment(a:str, b:str, vals:dict):
    dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
    for j in range(1, len(dp)):
        for i in range(1, len(dp[j])):
            a_idx, b_idx = i-1, j-1
            match_val = 0
            if a[a_idx] == b[b_idx]:
                match_val = vals[a[a_idx]]
            dp[j][i] = max(
                dp[j-1][i-1] + match_val,
                dp[j-1][i],
                dp[j][i-1]
            )

    res = str(dp[-1][-1])
    string = reconstruct(a, b, vals, dp)

    print(res)
    if string:
        print(string)

    return res, string

def reconstruct(a:str, b:str, vals:dict, dp):
    s = []
    j, i = len(a), len(b)
    while i > 0 and j > 0:
        diag = dp[i-1][j-1]
        up = dp[i-1][j]
        left = dp[i][j-1]
        max_val = max(diag, up, left)
        if diag == max_val:
            if a[j-1] == b[i-1] and vals[a[j-1]] != 0:
                s.append(a[j-1])
            i -= 1
            j -= 1
        elif up == max_val:
            i -= 1
        else:
            # left == max_val
            j -= 1

    s.reverse()
    return ''.join(s)

def print_output(res, string, file_path = None):
    if not file_path:
        file_path = input('Enter an output file path: ')
    with open(file_path, 'w') as f:
        f.write(res + '\n')
        if string:
            f.write(string)


if __name__ == '__main__':
    a, b, vals = read_input()
    res, string = find_alignment(a, b, vals)
    print_output(res, string)
