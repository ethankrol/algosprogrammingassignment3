from read_input import read_input

def find_alignment(a:str, b:str, vals:dict) -> None:
    dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
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

    print(dp[-1][-1])




if __name__ == '__main__':
    a, b, vals = read_input('inputs/example1.in')
    find_alignment(a, b, vals)
