from read_input import read_input

def find_alignment(a:str, b:str, vals:dict):
    # create a dp table where the rows are the indexes of b, and columns are indexes of a
    # if we look at dp[i_b][i_a], it will tell us the max value of subsequence alignment between a and b up to these indexes.
    # we will fill this up, and eventually dp[-1][-1] will give us the max value
    # we then need to recreate the specific subsequence using a helper function below
    # Note: we could also store a dp of the actual string, but it would be memory intensive, albiet more straightforward.

    # the rules for the dp: 
    # if a[i_a] == b[i_b], we will ALWAYS use this in some way (this is because the values are nonnegative)
    # we can add it to the max of the previous values, which is the max of the diagonal, up, and left.
    # We will add the value of the match to the diagonal, and not add anything to the up and left.
    dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
    for j in range(1, len(dp)):
        for i in range(1, len(dp[j])):
            a_idx, b_idx = i-1, j-1
            match_val = 0
            # in the case that there is no match, then we simply look at all immediate previous values and take the max
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
    # will reconstruct A VALID subsequence, but there may be multiple.
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
            # if the if statement above doesn't run, it just means we didn't match but still found a diagonal movement, so we just continue on.
            # If the If statement above doesn't run, up == max_val or left == max_val, so we will continue on to the next iteration of the loop and not add anything to the string.
            i -= 1
            j -= 1
        elif up == max_val:
            # this is because we only recreate if there was a diagonal movement (we used a match)
            # if there was an up movement, or left movement, we know there was no match so we continue on.
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
